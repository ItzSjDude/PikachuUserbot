"""DA.GD helpers
Available Commands:
{i}isup URL
{i}dns google.com
{i}url <long url>
{i}unshort <short url>"""
# Credits @UniBorg


@ItzSjDude(outgoing=True, pattern="dns (.*)")
@ItzSjDude(sudo=True, pattern="dns (.*)")
async def _(event):
    await dns(event)


@ItzSjDude(outgoing=True, pattern="url (.*)")
@ItzSjDude(sudo=True, pattern="url (.*)")
async def _(event):
    await urlx(event)


@ItzSjDude(outgoing=True, pattern="unsort (.*)")
@ItzSjDude(sudo=True, pattern="unsort (.*)")
async def _(event):
    await unshort(event)
