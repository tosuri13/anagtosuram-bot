import os

import aws_cdk as cdk
from aws_cdk import Stack
from aws_cdk import aws_events as events
from aws_cdk import aws_events_targets as events_targets
from aws_cdk import aws_iam as iam
from aws_cdk import aws_lambda as _lambda
from constructs import Construct

DISCORD_BOT_TOKEN = os.environ["DISCORD_BOT_TOKEN"]
DISCORD_CHANNEL_ID = os.environ["DISCORD_CHANNEL_ID"]
SOURCE_TEXT = os.environ["SOURCE_TEXT"]

ANAGTOSURAM_ASSET_PATH = "../../dist"


class AnagtosuramBotAppStack(Stack):
    def __init__(self, scope: Construct, id: str, **kwargs):
        super().__init__(scope, id, **kwargs)

        # 🐧 IAM Roles 🐧

        anagtosuram_function_role = iam.Role(
            self,
            "AnagtosuramFunctionRole",
            assumed_by=iam.ServicePrincipal("lambda.amazonaws.com"),  # type: ignore
            managed_policies=[
                iam.ManagedPolicy.from_aws_managed_policy_name(
                    "service-role/AWSLambdaBasicExecutionRole",
                )
            ],
            role_name="anagtosuram-bot-function-role",
        )

        # 🐧 Lambda Functions 🐧

        anagtosuram_shuffle_function = _lambda.Function(
            self,
            "AnagtosuramShuffleFunction",
            runtime=_lambda.Runtime.PYTHON_3_14,
            code=_lambda.Code.from_asset(path=f"{ANAGTOSURAM_ASSET_PATH}/shuffle"),
            handler="function.handler",
            architecture=_lambda.Architecture.ARM_64,
            function_name="anagtosuram-bot-shuffle-function",
            memory_size=128,
            role=anagtosuram_function_role,  # type: ignore
            timeout=cdk.Duration.minutes(5),
            environment={
                "DISCORD_BOT_TOKEN": DISCORD_BOT_TOKEN,
                "DISCORD_CHANNEL_ID": DISCORD_CHANNEL_ID,
                "SOURCE_TEXT": SOURCE_TEXT,
            },
        )

        # 🐧 EventBridge Rules 🐧

        events.Rule(
            self,
            "AnagtosuramShuffleRule",
            rule_name="anagtosuram-bot-shuffle-rule",
            schedule=events.Schedule.cron(hour="23", minute="50"),
            targets=[  # type: ignore
                events_targets.LambdaFunction(anagtosuram_shuffle_function),  # type: ignore
            ],
        )
