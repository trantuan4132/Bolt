import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
from googletrans import Translator
from GeneralCommands import *
#from PythonCommands import *
from GameCommands import *
from KaggleCommands import *

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='/')

@bot.event
async def on_ready():
    bot.add_cog(GeneralCommands(bot))
    #bot.add_cog(PythonCommands(bot))
    bot.add_cog(GameCommands(bot))
    bot.add_cog(KaggleCommands(bot))
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="/help"))
    print(f'{bot.user.name} has connected to Discord!')

@bot.event
async def on_message(message):
    if message.author.bot: return
    if message.content.startswith(':') and message.content.endswith(':'): return

    if message.content.lower() == "good bot":
        await message.channel.send("Thank you.")

    # if not message.content.startswith('/'):
    #     trans = Translator().detect(message.content)
    #     if trans.lang in ['ja', 'ru', 'vi'] and trans.confidence == 1.0:
    #         trans = Translator().translate(message.content)
    #         await message.channel.send(trans.text)

    await bot.process_commands(message)

@bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )

bot.run(TOKEN)
