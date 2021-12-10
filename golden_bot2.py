import discord
import random
from discord.ext import commands

app = commands.Bot(command_prefix='골든봇아 ')


@app.event
async def on_ready():
    print('다음으로 로그인합니다: ')
    print(app.user.name)
    print('connection was successful')
    await app.change_presence(status=discord.Status.online, activity=None)

@app.command()
async def 골든봇아(ctx):
    await ctx.send('네!')

@app.command()
async def 냥(ctx):
    await ctx.send('골든봇은 고양이가 아니다**냥!**')

@app.command()
async def 에브맨션도배(ctx):
    while True:
        await ctx.send('@everyone 도배시작! 도! 도! 도! 도배시작! 도! 도! 도! 도배시작!')

@app.command()
async def 도배(ctx):
    while True:
        await ctx.send('도배시작! 도! 도! 도! 도배시작! 도! 도! 도! 도배시작!')

embed = discord.Embed(title='도움말',description='골든봇, 냥, 에브맨션도배(매우 위험함), 도배(위험함), 도움말, 바보, 뭐해, 랜덤뽑', color = 0x00ff00)

@app.command()
async def 도움말(ctx):
    await ctx.send(embed=embed(embed))

@app.command()
async def 바보(ctx):
    await ctx.send('||너나||')

@app.command()
async def 뭐해(ctx):
    await ctx.send('네!')

@app.command()
async def 램덤뽑기(ctx):
    ran = random.randint(1, 100)
    await ctx.send(ran)

app.run('ODI5MTkzNjk1MDQzMzg3Mzky.YG0kzg.mRMsdObaU9FDMSMvU7MMwtRhc90')