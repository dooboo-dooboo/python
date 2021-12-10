import discord
from discord.ext import commands

app = commands.Bot(command_prefix='게')


@app.event
async def on_ready():
    print('다음으로 로그인합니다: ')
    print(app.user.name)
    print('connection was successful')
    await app.change_presence(status=discord.Status.idle, activity=discord.Game("게임봇아 도움말"))

@app.command()
async def 임봇아(ctx, *text):
    txt = ""
    for x in text:
        txt += x
        txt += ", "
    if txt == "도움말, ":
        await ctx.send(" : ")
    if txt == "가위바위, 보가위":
        await ctx.send(" : ")
app.run('ODQ1MjExNzE2NTQyMjY3Mzkz.YKdqwA._r8FMPXFWk1nImJDpVv7Y6q-jLs')