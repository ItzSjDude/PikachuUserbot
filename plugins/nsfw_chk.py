"""To check nudity of a pic
{i}boobs <reply to image>
{i}butts <reply to image>"""


import asyncio
import os
import urllib

import requests


@ItzSjDude(pattern=r"boobs")
async def boobs(event):
    if not os.path.isdir(Var.TEMP_DOWNLOAD_DIRECTORY):
        os.makedirs(Var.TEMP_DOWNLOAD_DIRECTORY)
    pic_loc = os.path.join(Var.TEMP_DOWNLOAD_DIRECTORY, "bobs.jpg")
    a = await event.reply("`Finding some big bobs 🧐...`")
    await asyncio.sleep(0.5)
    await a.edit("`Sending some big bobs 🌚...`")
    nsfw = requests.get("http://api.oboobs.ru/noise/1").json()[0]["preview"]
    urllib.request.urlretrieve("http://media.oboobs.ru/{}".format(nsfw), pic_loc)
    await event.client.send_file(event.chat_id, pic_loc, force_document=False)
    os.remove(pic_loc)
    await event.delete()
    await a.delete()


@ItzSjDude(pattern=r"butts")
async def butts(event):
    if not os.path.isdir(Var.TEMP_DOWNLOAD_DIRECTORY):
        os.makedirs(Var.TEMP_DOWNLOAD_DIRECTORY)
    pic_loc = os.path.join(Var.TEMP_DOWNLOAD_DIRECTORY, "butts.jpg")
    a = await event.reply("`Finding some beautiful butts 🧐...`")
    await asyncio.sleep(0.5)
    await a.edit("`Sending some beautiful butts 🌚...`")
    nsfw = requests.get("http://api.obutts.ru/noise/1").json()[0]["preview"]
    urllib.request.urlretrieve("http://media.obutts.ru/{}".format(nsfw), pic_loc)
    await event.client.send_file(event.chat_id, pic_loc, force_document=False)
    os.remove(pic_loc)
    await event.delete()
    await a.delete()
