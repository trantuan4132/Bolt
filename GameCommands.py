import discord
from discord.ext import commands
import random
import asyncio

class GameCommands(commands.Cog, name='Game Commands'):

    Katakana = {
'ア' : 'a',    'イ' : 'i',     'ウ' : 'u',     'エ' : 'e',      'オ' : 'o',
'カ' : 'ka',   'キ' : 'ki', 	 'ク' : 'ku',    'ケ' : 'ke',     'コ' : 'ko',     'キャ' : 'kya',   'キュ' : 'kyu',   'キョ' : 'kyo',
'サ' : 'sa',	  'シ' : 'shi', 	 'ス' : 'su',    'セ' : 'se',     'ソ' : 'so',     'シャ' : 'sha',   'シュ' : 'shu',   'ショ' : 'sho',
'タ' : 'ta',	  'チ' : 'chi', 	 'ツ' : 'tsu',   'テ' : 'te',     'ト' : 'to',     'チャ' : 'cha',   'チュ' : 'chu',   'チョ' : 'cho',
'ナ' : 'na',	  'ニ' : 'ni', 	 'ヌ' : 'nu',    'ネ' : 'ne',     'ノ' : 'no',     'ニャ' : 'nya',   'ニュ' : 'nyu',   'ニョ' : 'nyo',
'ハ' : 'ha',	  'ヒ' : 'hi', 	 'フ' : 'fu',    'ヘ' : 'he',     'ホ' : 'ho',     'ヒャ' : 'hya',   'ヒュ' : 'hyu',   'ヒョ' : 'hyo',
'マ' : 'ma',	  'ミ' : 'mi',    'ム' : 'mu',    'メ' : 'me',     'モ' : 'mo',     'ミャ' : 'mya',   'ミュ' : 'myu',   'ミョ' : 'myo',
'ヤ' : 'ya',                   'ユ' : 'yu',	                  'ヨ' : 'yo',
'ラ' : 'ra',	  'リ' : 'ri',    'ル' : 'ru',    'レ' : 're',     'ロ' : 'ro',     'リャ' : 'rya',   'リュ' : 'ryu',   'リョ' : 'ryo',
'ワ' : 'wa',	                                                   'ヲ' : 'wo',
'ン' : 'n',
'ガ' : 'ga',	  'ギ' : 'gi',    'グ' : 'gu',    'ゲ' : 'ge',	    'ゴ' : 'go',	    'ギャ' : 'gya',   'ギュ' : 'gyu',   'ギョ' : 'gyo',
'ザ' : 'za',	  'ジ' : 'ji',    'ズ' : 'zu',    'ゼ' : 'ze',	    'ゾ' : 'zo',	    'ジャ' : 'ja',    'ジュ' : 'ju',    'ジョ' : 'jo',
'ダ' : 'da',	  'ヂ' : 'ji',    'ヅ' : 'zu',    'デ' : 'de',	    'ド' : 'do',	    'ヂャ' : 'ja',    'ヂュ' : 'ju',    'ヂョ' : 'jo',
'バ' : 'ba',	  'ビ' : 'bi',    'ブ' : 'bu',    'ベ' : 'be',	    'ボ' : 'bo',	    'ビャ' : 'bya',   'ビュ' : 'byu',   'ビョ' : 'byo',
'パ' : 'pa',	  'ピ' : 'pi',    'プ' : 'pu',    'ペ' : 'pe',	    'ポ' : 'po',	    'ピャ' : 'pya',   'ピュ' : 'pyu',   'ピョ' : 'pyo'
}

    Hiragana = {
'あ' : 'a',    'い' : 'i',     'う' : 'u',     'え' : 'e',      'お' : 'o',
'か' : 'ka',   'き' : 'ki',    'く' : 'ku',    'け' : 'ke',     'こ' : 'ko',     'きゃ' : 'kya',   'きゅ' : 'kyu',   'きょ' : 'kyo',
'さ' : 'sa',   'し' : 'shi',   'す' : 'su',    'せ' : 'se',     'そ' : 'so',     'しゃ' : 'sha',   'しゅ' : 'shu',   'しょ' : 'sho',
'た' : 'ta',   'ち' : 'chi',   'つ' : 'tsu',   'て' : 'te',     'と' : 'to',     'ちゃ' : 'cha',   'ちゅ' : 'chu',   'ちょ' : 'cho',
'な' : 'na',   'に' : 'ni',    'ぬ' : 'nu',    'ね' : 'ne',     'の' : 'no',     'にゃ' : 'nya',   'にゅ' : 'nyu',   'にょ' : 'nyo',
'は' : 'ha',   'ひ' : 'hi',    'ふ' : 'fu',    'へ' : 'he',     'ほ' : 'ho',     'ひゃ' : 'hya',   'ひゅ' : 'hyu',   'ひょ' : 'hyo',
'ま' : 'ma',   'み' : 'mi',    'む' : 'mu',    'め' : 'me',     'も' : 'mo',     'みゃ' : 'mya',   'みゅ' : 'myu',   'みょ' : 'myo',
'ら' : 'ra',   'り' : 'ri',    'る' : 'ru',    'れ' : 're',     'ろ' : 'ro',     'りゃ' : 'rya',   'りゅ' : 'ryu',   'りょ' : 'ryo',
'や' : 'ya',	                  'ゆ' : 'yu',                     'よ' : 'yo',
'わ' : 'wa',                                                    'を' : 'wo',
'ん' : 'n',
'が' : 'ga',   'ぎ' : 'gi',    'ぐ' : 'gu',    'げ' : 'ge',     'ご' : 'go',     'ぎゃ' : 'gya',  'ぎゅ' : 'gyu',   'ぎょ' : 'gyo',
'ざ' : 'za',   'じ' : 'ji',    'ず' : 'zu',    'ぜ' : 'ze',     'ぞ' : 'zo',     'じゃ' : 'ja',   'じゅ' : 'ju',    'じょ' : 'jo',
'だ' : 'da',   'ぢ' : 'ji',    'づ' : 'zu',    'で' : 'de',     'ど' : 'do',     'ぢゃ' : 'ja',   'ぢゅ' : 'ju',    'ぢょ' : 'jo',
'ば' : 'ba',   'び' : 'bi',    'ぶ' : 'bu',    'べ' : 'be',     'ぼ' : 'bo',     'びゃ' : 'bya',  'びゅ' : 'byu',   'びょ' : 'byo',
'ぱ' : 'pa',   'ぴ' : 'pi',    'ぷ' : 'pu',    'ぺ' : 'pe',     'ぽ' : 'po',     'ぴゃ' : 'pya',  'ぴゅ' : 'pyu',   'ぴょ' : 'pyo'
}

    def __init__(self, bot):
        self.bot = bot

    async def matching_pronunciation(self, ctx, game, alias, dictionary, example, guide=None):
        if guide == '-guide' or guide == '-g':
            guide = f"""```prolog
            'WELCOME TO {game.upper()}'

- This game is about typing the 'corresponding pronunciation' to the given {game} character.

Ex: {example}

- Each correct pronunciation will be given 100 points.
- The maximum time to answer will be reduced by 0.5 seconds for each {game} character.
- This game will be over when an 'incorrect pronunciation' is typed or the time runs out, or there is 'no more questions left'.

- Finally, type /{game} or /{alias} to start the game```
"""
            await ctx.send(guide)
        else:
            bank = list(dictionary.items())
            random.shuffle(bank)
            score = 0
            for i in range(20, 0, -1):
                try:
                    question, answer = bank[i-1]
                    await ctx.send(f'{question}   ({i/2} seconds left)')
                    reply = await self.bot.wait_for('message', timeout=i/2, check=lambda reply: reply.author == ctx.author)
                    if reply.content == answer:
                        await reply.add_reaction(emoji = '✅')
                        score += 100
                        await asyncio.sleep(1)
                    else:
                        await reply.add_reaction(emoji = '❌')
                        await ctx.send(f'Correct answer: {answer}')
                        await asyncio.sleep(1)
                        break
                except:
                    await ctx.send('Time out!')
                    await ctx.send(f'Correct answer: {answer}')
                    break
            await ctx.send(f'Total score: {score}')
            await ctx.send(f'Fastest response time: {i/2}s')

    @commands.command(name='katakana', help="Type /katakana -g (or /kata -g) for more info", aliases=['kata'])
    async def katakana(self, ctx, guide=None):
        await self.matching_pronunciation(ctx=ctx,
                                          game='katakana',
                                          alias='kata',
                                          dictionary=self.Katakana,
                                          example='カ --> ka',
                                          guide=guide)

    @commands.command(name='hiragana', help="Type /hiragana -g (or /hira -g) for more info", aliases=['hira'])
    async def hiragana(self, ctx, guide=None):
        await self.matching_pronunciation(ctx=ctx,
                                          game='hiragana',
                                          alias='hira',
                                          dictionary=self.Hiragana,
                                          example='ひ --> hi',
                                          guide=guide)
