import json

import requests

from anagtosuram_bot.common.aws.ssm import get_parameter


def send_message(content: str) -> None:
    channel_id = get_parameter(key="/ANAGTOSURAM_BOT/DISCORD/CHANNEL_ID")

    requests.post(
        url=f"https://discord.com/api/v10/channels/{channel_id}/messages",
        data=json.dumps(
            {
                "content": content,
            }
        ),
        headers={
            "Authorization": f"Bot {get_parameter(key='/ANAGTOSURAM_BOT/DISCORD/BOT_TOKEN')}",
            "Content-Type": "application/json",
        },
    )

    return None
