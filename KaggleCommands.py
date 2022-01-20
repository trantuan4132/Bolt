import discord
from discord.ext import commands
from bs4 import BeautifulSoup
import requests
from urllib.request import urlopen
import json
import re
# from PIL import Image
import matplotlib.pyplot as plt

class KaggleCommands(commands.Cog, name = "Kaggle Commands"):

    courses = ['python',
               'pandas',
               'data-visualization',
               'data-cleaning',
               'intro-to-machine-learning',
               'intermediate-machine-learning',
               'intro-to-deep-learning',
               'feature-engineering',
               'intro-to-sql',
               'advanced-sql',
               'computer-vision',
               'geospatial-analysis',
               'machine-learning-explainability',
               'natural-language-processing',
               'intro-to-game-ai-and-reinforcement-learning',
               'microchallenges']

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='kaggle', help = 'List all certificate from user')
    async def kaggle(self, ctx, username='/'):
        try:
            profile = requests.get('https://www.kaggle.com/' + username)
            soup = BeautifulSoup(profile.text, "html.parser")
            attrs = soup.find_all('script', attrs={'class' : 'kaggle-component'})[1]
            img_pro_url = json.loads(re.findall('Kaggle.State.push\((.*?)\);', str(attrs))[0])['userAvatarUrl']

            url = 'https://www.kaggle.com/learn/certification/'
            count = 0
            cert_lst = []

            for course in self.courses:
                r = requests.get(url + username + '/' + course)
                soup = BeautifulSoup(r.text, "html.parser")
                img = 'No image found'
                try:
                    img_url = soup.find('meta', attrs={'property' : 'og:image'})['content']
                    # img = Image.open(urlopen(img_url))
                    cert_lst.append(course.replace('-', ' ').title())
                    count += 1
                except:
                    # print(img)
                    continue

            embed = discord.Embed(title="Username: ", description=username, color=0x04d9ff)
            embed.set_thumbnail(url=img_pro_url)
            embed.add_field(name="Total certificates:", value=count, inline=False)
            embed.add_field(name="List of certificates:", value='\n'.join(cert_lst) or 'No certificate found', inline=False)
            await ctx.send(embed=embed)
        except:
            await ctx.send('Username not found')
