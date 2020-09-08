import discord
from discord.ext import commands

client = commands.Bot(commands_prefix = '.')
@client.event
async def on_ready(ctx):
    print(f'{client.user} has connected to Discord!')




client.run('NzUyODQwOTU5NzYyNjI4NjQ5.X1dfxw.kzI7uslnpcsEHeMM6y3vGNXoGkY')
