import random

from anagtosuram_bot.common.aws.ssm import get_parameter
from anagtosuram_bot.common.discord import send_message


def handler(event: dict, context: dict) -> None:
    source_text = get_parameter("/ANAGTOSURAM_BOT/SOURCE_TEXT")
    shuffled_text = _shuffle_string(source_text)
    send_message(shuffled_text)

    return None


def _shuffle_string(text: str) -> str:
    text_list = list(text)
    random.shuffle(text_list)

    return "".join(text_list)
