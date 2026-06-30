import aws_cdk as cdk

from stacks.app import AnagtosuramBotAppStack

app = cdk.App()

AnagtosuramBotAppStack(app, "anagtosuram-bot-app")

app.synth()
