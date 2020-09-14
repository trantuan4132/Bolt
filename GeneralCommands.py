import discord
from discord.ext import commands
import random
from googletrans import Translator, LANGUAGES

class GeneralCommands(commands.Cog, name = "General Commands"):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='hi', help = 'Just say \'hi\' in response')
    async def hi(self, ctx):
        quotes = [
            'Konnichiwa!',
            'Hello!',
            'Hola!',
            'Bonjour!',
            'Hallo!',
            'Hei!',
            'Xin chào',
        ]

        response = random.choice(quotes)
        await ctx.send(response)

    @commands.command(name='bolt', help = 'Respond with random bolt gif')
    async def bolt(self, ctx):
        try:
            url = [
                "https://giphy.com/gifs/quiksilver-young-guns-youngguns-ygsnow-t76nQLeG6IAJiq8uAk",
                "https://giphy.com/gifs/quiksilver-young-guns-youngguns-ygsnow-1xONa8rsMAuGBdkPCK",
                "https://giphy.com/gifs/trippy-abstract-pi-slices-fwo7bzEVxbYS4eSNVd",
                "https://giphy.com/gifs/storm-tornado-clouds-xaZCqV4weJwHu",
                "https://giphy.com/gifs/artists-on-tumblr-trippy-pbvJD67ZL7NyE",
                "https://giphy.com/gifs/thunder-livalskare-c64m96xIm0ECc"
            ]
            await ctx.send(random.choice(url))
        except:
            await ctx.send("Sorry, no connection found or some errors occurred.")

    @commands.command(name='detect', help = 'Detect language inside quote \"\"')
    async def detect(self, ctx, sentence):
        try:
            code = Translator().detect(sentence).lang
            await ctx.send(LANGUAGES[code])
        except:
            await ctx.send('Sorry, invalid input found!')
        return

    @commands.command(name='trans', help = 'Translate anything inside quote \"\" into a chosen language')
    async def trans(self, ctx, sentence, dest='en', src='auto'):
        try:
            trans = Translator().translate(sentence, dest=dest, src=src)
            if trans.pronunciation is None:
                await ctx.send(trans.text)
            else:
                await ctx.send(f"{trans.text}   ({trans.pronunciation})")
        except:
            await ctx.send('Sorry, invalid input found!')
        return
