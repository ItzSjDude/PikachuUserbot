from pikabot.utils import ItzSjDude
from telethon.tl.types import Channel, Chat, User


@ItzSjDude(outgoing=True, pattern=r"stats")
async def _(event):
    if event.fwd_from:
        return
    start = pikatime.now()
    u = 0
    g = 0
    c = 0
    bc = 0
    b = 0
    dialogs = await event.client.get_dialogs(limit=None, ignore_migrated=True)
    for d in dialogs:
        currrent_entity = d.entity
        if isinstance(currrent_entity, User):
            if currrent_entity.bot:
                b += 1
            else:
                u += 1
        elif isinstance(currrent_entity, Chat):
            g += 1
        elif isinstance(currrent_entity, Channel):
            if currrent_entity.broadcast:
                bc += 1
            else:
                c += 1
        else:
            print(d)
    end = pikatime.now()
    ms = (end - start).seconds
    await event.edit(
        """`Your Stats Obtained in {} seconds`
`You have {} Private Messages`
`You are in {} Groups`
`You are in {} Super Groups`
`You Are in {} Channels`
`And finally Bots = {}`""".format(
            ms, u, g, c, bc, b
        )
    )
