"""
Pornhub downloader by @anubisxx
Syntax: .phd link
"""


import asyncio

import requests
from bs4 import BeautifulSoup
from pikabot.utils import ItzSjDude
from telethon.errors.rpcerrorlist import (
    UserAlreadyParticipantError,
    YouBlockedUserError,
)
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.messages import ImportChatInviteRequest


@ItzSjDude(outgoing=True, pattern="phd ?(.*)")
async def _(event):

    if event.fwd_from:

        return

    d_link = event.pattern_match.group(1)

    r = requests.get(d_link)

    soup = BeautifulSoup(r.content, "html.parser")

    temporary_variable = soup.find("span", {"class": "inlineFree"})

    title = temporary_variable.text

    temp = soup.find("div", {"class": "thumbnail"})

    view = soup.find("span", {"class": "count"})

    views = view.text

    temporary_variable_to_use = temp.find("img")

    temporary_variable_to_use["data-src"]

    if "pornhub" not in d_link:

        await event.edit("` I need a link to download something pro.`**(._.)**")

    else:

        await event.edit(
            "**💦Preparing to upload Video💦 **\n**Title**:  `{}`\n**Total Views**: `{}`".format(
                title, views
            )
        )

    await asyncio.sleep(2)

    async with event.client.conversation("@phsavebot") as conv:

        try:

            await conv.send_message("/start")

            oop = await conv.get_response()

            if "language" in oop.text:

                await event.client.send_message(
                    event.chat_id,
                    "**Please go to** @phsavebot **and select your language**",
                )

            await asyncio.sleep(2)

            me = await event.client.get_me()

            me.id

            # Necessary for the bot to work ;-;

            try:

                await event.client(JoinChannelRequest("Allsavernews"))

                await event.client(ImportChatInviteRequest("AAAAAFZPuYvdW1A8mrT8Pg"))

            except UserAlreadyParticipantError:

                await asyncio.sleep(0.00000069420)

            await conv.send_message(d_link)

            response = await conv.get_response()

            if "Downloading" in response.text:

                video_hehe = await conv.get_response()

                await event.client.send_file(
                    event.chat_id,
                    video_hehe,
                    caption="`🤤 Video Uploaded by` [Pikachu Userbot](t.me/PikachuUserbot)!🤤\n**Title:** `{}`".format(
                        title
                    ),
                )

            elif "Unfortunately" in response.text:

                await event.edit(
                    "`Woops, Incorrect link!`\n**Please check and try again.**"
                )

            elif "correct" in response.text:

                await event.client.send_message(event.chat_id, response.text)

        except YouBlockedUserError:

            await event.reply("**Please unblock** @phsavebot **and try again**")

            return
