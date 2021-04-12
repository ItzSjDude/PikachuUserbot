""" Google Translate
Available Commands:
.tr LanguageCode as reply to a message
.tr LangaugeCode | text to translate"""

import emoji
from googletrans import Translator
from pikabot.utils import ItzSjDude


@ItzSjDude(outgoing=True, pattern="tr")
async def _(event):
    if event.fwd_from:
        return
    if "trim" in event.raw_text:
        # https://t.me/c/1220993104/192075
        return
    input_str = event.text[4:6]
    txt = event.text[7:]
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        text = previous_message.message
        lan = input_str or "en"

    elif input_str:
        text = txt
        lan = input_str or "en"
    else:
        await event.edit("`.tr LanguageCode` as reply to a message")
        return
    text = emoji.demojize(text.strip())
    lan = lan.strip()
    translator = Translator()
    translated = translator.translate(text, dest=lan)
    after_tr_text = translated.text
    # TODO: emojify the :
    # either here, or before translation
    output_str = """**Translated By Pikabot**\n\nSource **( {} )**\n\nTranslation **( {} )**
         {}""".format(
        translated.src, lan, after_tr_text
    )
    await event.edit(output_str)
