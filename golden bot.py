import discord
from discord.ext import commands
import random

app = commands.Bot(command_prefix='G ')


@app.event
async def on_ready():
    print('다음으로 로그인합니다: import discord')
from discord.ext import commands
import random

app = commands.Bot(command_prefix='G ')


@app.event
async def on_ready():
    print('다음으로 로그인합니다: ')
    print(app.user.name)
    print('connection was successful')
    await app.change_presence(status=discord.Status.idle, activity=discord.Game("G commands"))


@app.command()
async def 골든봇(ctx):
    await ctx.send('네, 저에요!')

@app.command()
async def 자기소개(ctx):
    await ctx.send('저는 세계최강 봇이에요! 누구도 제 실력을 따라올수 없어요! 저는 언제나 AI처럼 행동해요! 그리고 오류도 없죠! 뭐 설명하자면 많지만...여기서 그만할게요!')

@app.command()
async def 냥(ctx):
    await ctx.send('냥!')

@app.command()
async def 뭐해(ctx):
    await ctx.send('놀고 있어요!')

@app.command()
async def 안녕(ctx):
    await ctx.send('안녕하세요!')

@app.command()
async def ㅋㅋㅋ(ctx):
    await ctx.send('크득크득!')

ct = 0
ss = 0
rsp = 0
a = 0
@app.command()
async def 놀자(ctx, *text):
    txt = ""
    global a
    for x in text:
        txt += x
        txt += ", "
    if txt == "":
        embed1 = discord.Embed(title="놀자 도움말 / 명령어", description="놀자 도움말", color=0x62c1cc)
        embed1.set_footer(
            text=''' -----퀴즈-----\n 초성 : 초성퀴즈\n -----놀이-----\n 냥냥 : 냥냥이 소리 내기\n -----게임-----\n 가위바위보 : 가위바위보 하기''')
        await ctx.send(embed=embed1)
    if txt == "퀴즈, 초성, ":
        global ct
        a = random.randint(1, 10)

        ct = 1
        if a == 1:
            await ctx.send('ㄱㅇㅇ')
        if a == 2:
            await ctx.send('ㄱㅇㅈ')
        if a == 3:
            await ctx.send('ㄱㅌ')
        if a == 4:
            await ctx.send('ㄷㅅㅋㄷ')
        if a == 5:
            await ctx.send('ㅍㅇㅆ')
        if a == 6:
            await ctx.send('ㅅㅍㄱ')
        if a == 7:
            await ctx.send('ㄱㄷㅂ')
        if a == 8:
            await ctx.send('ㅋㅍㅌ')
        if a == 9:
            await ctx.send('ㅈㅇ')
        if a == 10:
            await ctx.send('ㄴㅌㅂ')
        await ctx.send('정답 000으로 말해 주세요.')
    elif txt == "놀이, 냥냥, ":
        global ss
        ss = 1
        a = random.randint(1, 100)
        b = ""
        for x in range(a):
            b += "냥"
        await ctx.send(b)
        ss = 0
    elif txt == "게임, 가위바위보, ":
        global rsp
        rsp = 1
        a = random.randint(1, 3)
        await ctx.send("게임 시작! 가위바위보 00으로 입력해 주세요.")

@app.command()
async def 가위바위보(ctx, *text):
    global rsp, a
    txt = ""
    for x in text:
        txt += x
        txt += ", "

    if rsp == 1:
        my = 0
        if txt == "가위, ":
            my = 1
        elif txt == "바위, ":
            my = 2
        elif txt == "보, ":
            my = 3
        else:
            my = 0
            await ctx.send("게임이 진행되지 않았습니다.")
        if my == 0:
            pass
        elif my == a:
            await ctx.send("비겼습니다!")
        elif my == a + 1 or my == a - 2:
            await ctx.send("제가 이겼어요!")
        elif my == a - 1 or my == a + 2:
            await ctx.send("제가 졌어요...")
        rsp = 0
''''@app.command()
async def 도배(ctx):
    while True:
        await ctx.send('@everyone 도배입니다 삐삐삐삐삐삐삐삐삐삐 당장 달려드십시오 이 도배는 100번 반복됩니다.')
'''

@app.command()
async def 멈춰(ctx):
    await ctx.send('https://tenor.com/view/%EB%A9%88%EC%B6%B0-stop-gif-21048386')
# https://discord.com/api/oauth2/authorize?client_id=829219556915413033&permissions=2151152192&scope=bot
@app.command()
async def 도움말(ctx):
    embed = discord.Embed(title="도움말 / 명령어", description="기본 도움말", color=0x62c1cc)
    embed.set_footer(
        text=''' 골든봇 : 골든봇을 불러요!\n 냥 : 고양이!\n 뭐해 : 골든봇이 뭐할까요?\n 안녕 : 인사해요!\n ㅋㅋㅋ:웃어요!\n 놀자 : 놀아요!\n 멈춰 : 웃긴 멈춰 gif!\n 도움말 : 도움말\n''')
    await ctx.send(embed=embed)


@app.command()
async def 정답(ctx, *text):
    txt = ""
    global ct, a
    for x in text:
        txt += x
        txt += ", "
    if txt == "고양이, " and a == 1:
        await ctx.send('정답입니다!')
    elif txt == "강아지, " and a == 2:
        await ctx.send('정답입니다!')
    elif txt == "기타, " and a == 3:
        await ctx.send('정답입니다!')
    elif txt == "디스코드, " and a == 4:
        await ctx.send('정답입니다! 제가 있는 곳이죠!')
    elif txt == "파이썬, " and a == 5:
        await ctx.send('정답입니다! 제가 만들어진 곳이죠!')
    elif txt == "선풍기, " and a == 6:
        await ctx.send('정답입니다!')
    elif txt == "골든봇, " and a == 7:
        await ctx.send('정답입니다! 저죠!')
    elif txt == "컴퓨터, " and a == 8:
        await ctx.send('정답입니다!')
    elif txt == "종이, " and a == 9:
        await ctx.send('정답입니다!')
    elif txt == "노트북, " and a == 10:
        await ctx.send('정답입니다!')
    elif a == 0:
        await ctx.send('퀴즈가 생성되지 않았습니다.')
    else:
        await ctx.send('제가 원하는 답안이 아닙니다!')
    a = 0
    ct = 0


    print(app.user.name)
    print('connection was successful')
    await app.change_presence(status=discord.Status.idle, activity=discord.Game("G commands"))

@app.command()
async def 골든봇(ctx):
    await ctx.send('네, 저에요!')

@app.command()
async def 자기소개(ctx):
    await ctx.send('저는 세계최강 봇이에요! 누구도 제 실력을 따라올수 없어요! 저는 언제나 AI처럼 행동해요! 그리고 오류도 없죠! 뭐 설명하자면 많지만...여기서 그만할게요!')

@app.command()
async def 냥(ctx):
    await ctx.send('냥!')

@app.command()
async def 뭐해(ctx):
    await ctx.send('놀고 있어요!')

@app.command()
async def 안녕(ctx):
    await ctx.send('안녕하세요!')

@app.command()
async def ㅋㅋㅋ(ctx):
    await ctx.send('크득크득!')

ct = 0
ss = 0
rsp = 0
a = 0
@app.command()
async def 놀자(ctx, *text):
    txt = ""
    global a
    for x in text:
        txt += x
        txt += ", "
    if txt == "":
        embed1 = discord.Embed(title="놀자 도움말 / 명령어", description="놀자 도움말", color=0x62c1cc)
        embed1.set_footer(
            text=''' -----퀴즈-----\n 초성 : 초성퀴즈\n -----놀이-----\n 냥냥 : 냥냥이 소리 내기\n -----게임-----\n 가위바위보 : 가위바위보 하기''')
        await ctx.send(embed=embed1)
    if txt == "퀴즈, 초성, ":
        global ct
        a = random.randint(1, 10)

        ct = 1
        if a == 1:
            await ctx.send('ㄱㅇㅇ')
        if a == 2:
            await ctx.send('ㄱㅇㅈ')
        if a == 3:
            await ctx.send('ㄱㅌ')
        if a == 4:
            await ctx.send('ㄷㅅㅋㄷ')
        if a == 5:
            await ctx.send('ㅍㅇㅆ')
        if a == 6:
            await ctx.send('ㅅㅍㄱ')
        if a == 7:
            await ctx.send('ㄱㄷㅂ')
        if a == 8:
            await ctx.send('ㅋㅍㅌ')
        if a == 9:
            await ctx.send('ㅈㅇ')
        if a == 10:
            await ctx.send('ㄴㅌㅂ')
        await ctx.send('정답 000으로 말해 주세요.')
    elif txt == "놀이, 냥냥, ":
        global ss
        ss = 1
        a = random.randint(1, 100)
        b = ""
        for x in range(a):
            b += "냥"
        await ctx.send(b)
        ss = 0
    elif txt == "게임, 가위바위보, ":
        global rsp
        rsp = 1
        a = random.randint(1, 3)
        await ctx.send("게임 시작! 가위바위보 00으로 입력해 주세요.")

@app.command()
async def 가위바위보(ctx, *text):
    global rsp, a
    txt = ""
    for x in text:
        txt += x
        txt += ", "

    if rsp == 1:
        my = 0
        if txt == "가위, ":
            my = 1
        elif txt == "바위, ":
            my = 2
        elif txt == "보, ":
            my = 3
        else:
            my = 0
            await ctx.send("게임이 진행되지 않았습니다.")
        if my == 0:
            pass
        elif my == a:
            await ctx.send("비겼습니다!")
        elif my == a + 1 or my == a - 2:
            await ctx.send("제가 이겼어요!")
        elif my == a - 1 or my == a + 2:
            await ctx.send("제가 졌어요...")
        rsp = 0
''''@app.command()
async def 도배(ctx):
    while True:
        await ctx.send('@everyone 도배입니다 삐삐삐삐삐삐삐삐삐삐 당장 달려드십시오 이 도배는 100번 반복됩니다.')
'''

@app.command()
async def 멈춰(ctx):
    await ctx.send('https://tenor.com/view/%EB%A9%88%EC%B6%B0-stop-gif-21048386')
# https://discord.com/api/oauth2/authorize?client_id=829219556915413033&permissions=2151152192&scope=bot
@app.command()
async def 도움말(ctx):
    embed = discord.Embed(title="도움말 / 명령어", description="기본 도움말", color=0x62c1cc)
    embed.set_footer(
        text=''' 골든봇 : 골든봇을 불러요!\n 냥 : 고양이!\n 뭐해 : 골든봇이 뭐할까요?\n 안녕 : 인사해요!\n ㅋㅋㅋ:웃어요!\n 놀자 : 놀아요!\n 멈춰 : 웃긴 멈춰 gif!\n 도움말 : 도움말\n''')
    await ctx.send(embed=embed)


@app.command()
async def 정답(ctx, *text):
    txt = ""
    global ct, a
    for x in text:
        txt += x
        txt += ", "
    if txt == "고양이, " and a == 1:
        await ctx.send('정답입니다!')
    elif txt == "강아지, " and a == 2:
        await ctx.send('정답입니다!')
    elif txt == "기타, " and a == 3:
        await ctx.send('정답입니다!')
    elif txt == "디스코드, " and a == 4:
        await ctx.send('정답입니다! 제가 있는 곳이죠!')
    elif txt == "파이썬, " and a == 5:
        await ctx.send('정답입니다! 제가 만들어진 곳이죠!')
    elif txt == "선풍기, " and a == 6:
        await ctx.send('정답입니다!')
    elif txt == "골든봇, " and a == 7:
        await ctx.send('정답입니다! 저죠!')
    elif txt == "컴퓨터, " and a == 8:
        await ctx.send('정답입니다!')
    elif txt == "종이, " and a == 9:
        await ctx.send('정답입니다!')
    elif txt == "노트북, " and a == 10:
        await ctx.send('정답입니다!')
    elif a == 0:
        await ctx.send('퀴즈가 생성되지 않았습니다.')
    else:
        await ctx.send('제가 원하는 답안이 아닙니다!')
    a = 0
    ct = 0

app.run('ODI2MDQ5NjE2MDM0MDA1MDAy.YGG0pw.cGSQ3qAIc5PxDZTim5Fnmwho4fc')