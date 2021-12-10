import discord
from discord.ext import commands
import random

app = commands.Bot(command_prefix='T ')


@app.event
async def on_ready():
    print('다음으로 로그인합니다: ')
    print(app.user.name)
    print('connection was successful')
    await app.change_presence(status=discord.Status.idle, activity=discord.Game("T commands"))


@app.command()
async def 토크봇(ctx):
    await ctx.send('네, 저에요! 같이 이야기해요! 너ㅐ모렫조랴ㅐㅓㅑ너배ㅑㅍ롭대ㅑ어ㅐ냐머차무로야ㅗㅁ너로어류ㅜ처ㅠㅋ트츄마ㅓ롸ㅓㄷ보ㅕㄱ롸버ㅗ러ㅗ리버ㅔㄹ야ㅗ랴ㅐㅍㅇ...')

@app.command()
async def 토크(ctx, *text):
    txt = ""
    for x in text:
        txt += x
        txt += ", "
    if txt == "내, 이름이, 뭐게?, ":
        await ctx.send('당신의 이름은 {} 입니다!'.format(ctx.author.mention))
    if txt == "금지어, 설정, ":
        if ctx.author == "기타#5955":
            await ctx.send('금지어 설정 : ')

    if txt == "모두, 불러, ":
        await ctx.send('@everyone 이리 와요!')
    if txt == "도움말, ":
        await ctx.send(
            ' 도움말을 알려드릴게요!\n\n\n -------기본 방식-------\n\n T 명령어 로 사용합니다! \n\n\n -------명령어-------\n -----토크-----\n 내 이름이 뭐게? : 당신의 디코 이름(닉네임)을 맞춥니다!\n 모두 불러 : 에브멘션을 던집니다.\n 도움말 : 말 그대로 도움말입니다.\n 지금 기분 어때? : 지금 기분을 말합니다.\n ex)T 토크 도움말 => 도움말을 던져줍니다!'
        )
    if txt == "지금, 기분, 어때?, ":
        a = random.randint(1, 7)
        if a == 1:
            await ctx.send('기분 최고에요!')
        elif a == 2:
            await ctx.send('음...좋아요!')
        elif a == 3:
            await ctx.send('글쎼요?')
        elif a == 4:
            await ctx.send('음...그럭저럭...')
        elif a == 5:
            await ctx.send('그리 좋지는 않아요...')
        elif a == 6:
            await ctx.send('안좋아요...')
        elif a == 7:
            await ctx.send('기분 최악이에요!')
    if txt == "하지마, ":
        await ctx.send('너나')
    if txt == "도배, ":
        await ctx.send('저는 도배따위는 하지 않는 신선한 봇이랍니다!')

app.run('ODQzNzM1Njg3MTEwMzI4MzIw.YKIMFw.iyu6tpGoORCaET2fnNFD9bRZqSc')