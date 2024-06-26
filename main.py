import discord

dc = discord.Client()


@dc.event
async def on_ready():
    print('We have logged in as {0.user}'.format(dc))
