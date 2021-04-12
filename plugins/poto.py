import logging

from pikabot.utils import ItzSjDude

logger = logging.getLogger(__name__)
if 1 == 1:
    name = "Profile Photos"

    @ItzSjDude(outgoing=True, pattern="poto(.*)")
    async def potocmd(event):
        id = "".join(event.raw_text.split(maxsplit=2)[1:])
        user = await event.get_reply_message()
        chat = event.input_chat
        if user:
            photos = await event.client.get_profile_photos(user.sender)
        else:
            photos = await event.client.get_profile_photos(chat)
        if id.strip() == "":
            try:
                await event.client.send_file(event.chat_id, photos)
            except a:
                photo = await event.client.download_profile_photo(chat)
                await event.client.send_file(event.chat_id, photo)
        else:
            try:
                id = int(id)
                if id <= 0:
                    await event.edit("`ID number you entered is invalid`")
                    return
            except BaseException:
                await event.edit("`Are you Comedy Me ?`")
                return
            if int(id) <= (len(photos)):
                send_photos = await event.client.download_media(photos[id - 1])
                await event.client.send_file(event.chat_id, send_photos)
            else:
                await event.edit("`No photo found of that Nigga , now u Die`")
                return
