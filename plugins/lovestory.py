"""COMMAND : .lovestory"""


import asyncio

from pikabot.utils import ItzSjDude


@ItzSjDude(outgoing=True, pattern="lovestory")
async def _(event):

    if event.fwd_from:

        return

    animation_interval = 3

    animation_ttl = range(0, 103)

    # input_str = event.pattern_match.group(1)

    # if input_str == "lovestory":

    await event.edit("Starting asf")

    animation_chars = [
        "1 ❤️ love story",
        r"  😐             😕 \n/👕\         <👗\ \n 👖               /|",
        r"  😉          😳 \n/👕\       /👗\ \n  👖            /|",
        r"  😚            😒 \n/👕\         <👗> \n  👖             /|",
        r"  😍         ☺️ \n/👕\      /👗\ \n  👖          /|",
        r"  😍          😍 \n/👕\       /👗\ \n  👖           /|",
        r"  😘   😊 \n /👕\/👗\ \n   👖   /|",
        r" 😳  😁 \n /|\ /👙\ \n /     / |",
        r"😈    /😰\ \n<|\      👙 \n /🍆    / |",
        r"😅 \n/(),✊😮 \n /\         _/\\/|",
        "😎 \n/\\_,__😫 \n  //    //       \\",
        "😖 \n/\\_,💦_😋  \n  //         //        \\",
        r"  😭      ☺️ \n  /|\   /(👶)\ \n  /!\   / \ ",
        "The End 😂...",
    ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)

        await event.edit(animation_chars[i % 103])
