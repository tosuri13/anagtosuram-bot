import requests

from anagtosuram.config import Config


class DiscordClient:
    def __init__(self, bot_token: str):
        self.bot_token = bot_token

        self._headers = {
            "Authorization": f"Bot {self.bot_token}",
            "Content-Type": "application/json",
        }

    def send_channel_message(self, channel_id: str, content: str):
        response = requests.post(
            f"{Config.DISCORD_API_BASEURL}/channels/{channel_id}/messages",
            headers=self._headers,
            json={"content": content},
        )

        if response.status_code != 200:
            raise ValueError(f"Discord API failed: {response.text}")
