"""Congrats Module
{i}congo"""

from . import _congo


@ItzSjDude(outgoing=True, pattern="congo")
@ItzSjDude(sudo=True, pattern="congo")
async def _(event):
    await _congo(event)
