import discord
from discord.ext.commands
import Bot
from discord.ext
import commands

    Client = discord.Client()
    bot_prefix = "s."
    client = commands.Bot(command_prefix = bot_prefix)
    @client.event
    aasync def on_ready();
        print('Bot is up')
        print('Name: {}'.format(client.user.name))
        print("ID: {}".format(client.user.id))

@client.command(pass_context = True)
async def ping(ctx):

    await client.say('pong')
    
client.run('')
s.ping