"""Send Chat Actions
Syntax: .sca <option> <time in sec>
        sca options: Options for sca

typing
contact
game
location
voice
round
video
photo
document
cancel"""

import asyncio

from pikabot.utils import ItzSjDude


@ItzSjDude(outgoing=True, pattern="sca ?(.*)")
async def _(event):
    if event.fwd_from:
        return
    await event.delete()
    input_str = event.pattern_match.group(1)
    action = "typing"
    if input_str:
        action = input_str
    async with event.client.action(event.chat_id, action):
        await asyncio.sleep(86400)  # type for 10 seconds
