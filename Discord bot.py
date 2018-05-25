import discord
from discord.ext import commands
from discord.voice_client import VoiceClient

startup_extensions = ["Music"]
bot = commands.Bot("$")


@bot.event
async def on_ready():
    print("Bot online")

class Main_commands():
        def __init__(self, bot):
         self.bot = bot


@bot.command(pass_context=True)
async def ping(ctx):
     await bot.say("Pong :ping_pong:")


@bot.command(pass_context=True)
async def hello(ctx):
    await bot.say("Hello :wave:")


@bot.command(pass_context=True)
async def status(ctx):
    await bot.say("@everyone The bot is currently up")



@bot.command(pass_context=True)
async def creator(ctx):
    await bot.say("This bot was created by DioN")


                  
if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
             exc = ' {}: {}' .format(type(e).__name__, e)
             print('Failed to load extension {}\n{}'.format(extension, exc))



bot.run("NDQ5NTYzNzk0ODI2MzMwMTEz.Demggw.WMIEQfn2F4yMuI6HdPQtmt4OOQk")
    


