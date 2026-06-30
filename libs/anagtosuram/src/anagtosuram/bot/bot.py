import os
import random

from anagtosuram.utils.discord import DiscordClient


class AnagtosuramBot:
    def __init__(self, client: DiscordClient, channel_id: str):
        self.client = client
        self.channel_id = channel_id

    def shuffle(self):
        source_text = os.environ["SOURCE_TEXT"]

        text_list = list(source_text)
        random.shuffle(text_list)
        shuffled_text = "".join(text_list)

        self.client.send_channel_message(self.channel_id, shuffled_text)
