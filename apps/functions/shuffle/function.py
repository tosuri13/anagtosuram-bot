import os

from anagtosuram.bot import AnagtosuramBot
from anagtosuram.utils.discord import DiscordClient

DISCORD_BOT_TOKEN = os.environ["DISCORD_BOT_TOKEN"]
DISCORD_CHANNEL_ID = os.environ["DISCORD_CHANNEL_ID"]

client = DiscordClient(DISCORD_BOT_TOKEN)
bot = AnagtosuramBot(client, DISCORD_CHANNEL_ID)


def handler(event, context):
    bot.shuffle()
