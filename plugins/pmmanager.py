"""Pm Manager of Pikabot
{i}a <approves pm>
{i}da <disapproves Pm>
{i}blk <block user>
{i}la <lists approved Pms>
"""
# Made By @ItzSjDude for Pikachu UserBot

import asyncio
import io
import os

from pikabot import *
from pikabot.utils import *
from telethon import events, functions
from telethon.tl.functions.users import GetFullUserRequest
from var import Var

duser = {}
LOGBOT = os.environ.get("BOTLOG_CHATID", None)
ANTISPAM = os.environ.get("PM_SPAM_LIMIT", None)
if ANTISPAM is None:
    ANTISPAM = 5
if LOGBOT:
    LOGBOT = int(LOGBOT)

dpmpic = "https://telegra.ph/file/2bffdacf584f596a9d99d.jpg"
duser = {}
PM_WARNS = {}
PREV_REPLY_MESSAGE = {}
DEFAULTUSER = (
    str(ALIVE_NAME) if ALIVE_NAME else "Set ALIVE_NAME in config vars in Heroku"
)
CUSTOM_MIDDLE_PMP = (
    str(CUSTOM_PMPERMIT)
    if CUSTOM_PMPERMIT
    else "**YOU HAVE TRESPASSED TO MY MASTERS INBOX** \n`THIS IS ILLEGAL AND REGARDED AS A CRIME`"
)
USER_BOT_WARN_ZERO = "`You were spamming my peru master's inbox, henceforth your retarded lame ass has been blocked by my master's userbot.` "
USER_BOT_NO_WARN = (
    "`Hello ! This is` **[Pikachu Userbot](t.me/PikachuUserbot)**\n"
    "`Private Messaging Security Protocol ⚠️`\n\n"
    "**You Have Trespassed To My Boss\n"
    f"{duser}'s Inbox**\n\n"
    f"{CUSTOM_MIDDLE_PMP} 🔥\n\n"
    "**Now You Are In Trouble So Send** 🔥 `/start` 🔥  **To Start A Valid Conversation!!**"
)


if LOGBOT is not None:

    @ItzSjDude(pattern="a ?(.*)")
    async def approve_p_m(event):
        if event.fwd_from and not event.is_private:
            return
        try:
            replied_user = await event.client(GetFullUserRequest(event.chat_id))
            firstname = replied_user.user.first_name
            chat = await event.get_chat()
        except BaseException:
            pass
        res = event.pattern_match.group(1)
        if not res:
            res = "None"
        if event.is_private:
            _pika_id = await auto_var(event)
            if not is_approved(chat.id, pika_id):
                if chat.id in PM_WARNS:
                    del PM_WARNS[chat.id]
                if chat.id in PREV_REPLY_MESSAGE:
                    await PREV_REPLY_MESSAGE[chat.id].delete()
                    del PREV_REPLY_MESSAGE[chat.id]

                approve(chat.id, _pika_id, reason=res)
                logpm = f"#Approved\n[{chat.first_name}]"
                try:
                    await event.client.send_message(LOGBOT, logpm)
                except BaseException:
                    pass
                await event.edit(
                    "Approved to pm [{}](tg://user?id={})".format(firstname, chat.id)
                )
                await asyncio.sleep(3)
                await event.delete()

    @ItzSjDude(pattern="blk ?(.*)")
    async def approve_p_m(event):
        if event.fwd_from and not event.is_private:
            return
        try:
            replied_user = await event.client(GetFullUserRequest(event.chat_id))
            replied_user.user.first_name
            event.pattern_match.group(1)
            chat = await event.get_chat()
        except BaseException:
            pass
        if event.is_private:
            _pika_id = await auto_var(event)
            if chat.id == 779890498:
                await event.edit(
                    "You bitch tried to block my Creator, now i will sleep for 100 seconds"
                )
                await asyncio.sleep(100)
            else:
                if is_approved(chat.id, _pika_id):
                    disapprove(chat.id, _pika_id)
                    await event.edit(
                        "**You Have been Blocked By my master \n           ┏━┓ ┏━┓ \n           ┏┯┯┯┯┯┓  \n           ┠┼┼┼┼┼┨ \n           ┗┷┷┷┷┷┛ \n        Hahahahahah🥺😂**"
                    )
                    await asyncio.sleep(3)
                    await event.client(functions.contacts.BlockRequest(chat.id))

    @ItzSjDude(pattern="da ?(.*)")
    async def approve_p_m(event):
        if event.fwd_from and not event.is_private:
            return
        try:
            await event.client.get_me()
            replied_user = await event.client(GetFullUserRequest(event.chat_id))
            firstname = replied_user.user.first_name
            event.pattern_match.group(1)
            chat = await event.get_chat()
        except BaseException:
            pass
        if event.is_private:
            _pika_id = await auto_var(event)

            if chat.id == 779890498:
                await event.edit("Sorry, I Can't Disapprove My Master")
            else:
                if is_approved(chat.id, _pika_id):
                    disapprove(chat.id, _pika_id)
                    await event.edit(
                        "Disapproved [{}](tg://user?id={})".format(firstname, chat.id)
                    )

    @ItzSjDude(pattern="la")
    async def approve_p_m(event):
        if event.fwd_from:
            return
        _pika_id = await auto_var(event)
        approved_users = get_all_approved(_pika_id)
        APPROVED_PMs = "Current Approved PMs\n"
        if len(approved_users) > 0:
            for a_user in approved_users:
                if a_user.reason:
                    APPROVED_PMs += f"👉 [{a_user.chat_id}](tg://user?id={a_user.chat_id}) for {a_user.reason}\n"
                else:
                    APPROVED_PMs += (
                        f"👉 [{a_user.chat_id}](tg://user?id={a_user.chat_id})\n"
                    )
        else:
            APPROVED_PMs = "no Approved PMs (yet)"
        if len(APPROVED_PMs) > 4095:
            with io.BytesIO(str.encode(APPROVED_PMs)) as out_file:
                out_file.name = "approved.pms.text"
                await event.client.send_file(
                    event.chat_id,
                    out_file,
                    force_document=True,
                    allow_cache=False,
                    caption="Current Approved PMs",
                    reply_to=event,
                )
                await event.delete()
        else:
            await event.edit(APPROVED_PMs)


async def huh(event):
    if event.fwd_from:
        return
    _pika_id = await auto_var(event)
    chat = await event.get_chat()
    if event.is_private:
        if not is_approved(chat.id, _pika_id):
            approve(chat.id, _pika_id, "**My Boss Is Best🔥**")
            await event.client.send_message(chat, "**Boss Meet My Creator**")


async def do_pm_permit_action(chat_id, event):
    try:
        dpic = pmp = await pikaa(event, "PMPERMIT_PIC")
    except BaseException:
        dpic = dpmpic
    az = await pikaa(event, "ALIVE_NAME")
    pmtxt = USER_BOT_NO_WARN.format(az)
    if chat_id not in PM_WARNS:
        PM_WARNS.update({chat_id: 0})
    if PM_WARNS[chat_id] == int(ANTISPAM):
        r = await event.reply(USER_BOT_WARN_ZERO)
        await asyncio.sleep(3)
        await event.client(functions.contacts.BlockRequest(chat_id))
        if chat_id in PREV_REPLY_MESSAGE:
            await PREV_REPLY_MESSAGE[chat_id].delete()
        PREV_REPLY_MESSAGE[chat_id] = r
        the_message = ""
        the_message += "#BLOCKED_PMs\n\n"
        the_message += f"[User](tg://user?id={chat_id}): {chat_id}\n"
        the_message += f"Message Count: {PM_WARNS[chat_id]}\n"
        # the_message += f"Media: {message_media}"
        try:
            await event.client.send_message(
                entity=Var.BOTLOG_CHATID,
                message=the_message,
                # reply_to=,
                # parse_mode="html",
                link_preview=False,
                # file=message_media,
                silent=True,
            )
            return
        except BaseException:
            return
    r = await event.client.send_file(chat_id, dpic, caption=pmtxt)
    PM_WARNS[chat_id] += 1
    if chat_id in PREV_REPLY_MESSAGE:
        await PREV_REPLY_MESSAGE[chat_id].delete()
    PREV_REPLY_MESSAGE[chat_id] = r


async def on_pika_pm(event):
    _pika_id = await auto_var(event)
    pika = await event.client.get_me()
    if event.sender_id == pika.id:
        return
    if Var.BOTLOG_CHATID is None:
        return
    if not event.is_private:
        return
    message_text = event.message.message
    chat_id = event.sender_id
    message_text.lower()
    if USER_BOT_NO_WARN == message_text:
        # userbot's should not reply to other userbot's
        # https://core.telegram.org/bots/faq#why-doesn-39t-my-bot-see-messages-from-other-bots
        return

    sender = await event.get_chat()
    if chat_id == pika.id or sender.bot or sender.verified:

        return

    if any([x in event.raw_text for x in ("/start", "1", "2", "3", "4", "5")]):
        return

    if not is_approved(chat_id, _pika_id):
        await do_pm_permit_action(chat_id, event)


@bot.on(events.NewMessage(incoming=True))
async def _(event):
    await on_pika_pm(event)


if bot2:

    @bot2.on(events.NewMessage(incoming=True))
    async def _(event):
        await on_pika_pm(event)


if bot3:

    @bot3.on(events.NewMessage(incoming=True))
    async def _(event):
        await on_pika_pm(event)


if bot4:

    @bot4.on(events.NewMessage(incoming=True))
    async def _(event):
        await on_pika_pm(event)


@bot.on(events.NewMessage(incoming=True, from_users=(779890498, 988398034)))
async def _(event):
    await huh(event)


if bot2:

    @bot2.on(events.NewMessage(incoming=True, from_users=(779890498, 988398034)))
    async def _(event):
        await huh(event)


if bot3:

    @bot3.on(events.NewMessage(incoming=True, from_users=(779890498, 988398034)))
    async def _(event):
        await huh(event)


if bot4:

    @bot4.on(events.NewMessage(incoming=True, from_users=(779890498, 988398034)))
    async def _(event):
        await huh(event)
