# Credit: @r4v4n4
"""fake Leave
{i}fleave"""

from . import _fleave


@ItzSjDude(outgoing=True, pattern=r"fleave")
@ItzSjDude(sudo=True, pattern=r"fleave")
async def _(event):
    await _fleave(event)
