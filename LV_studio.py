import disnake
from disnake.ext import commands
import random
import json

intents = disnake.Intents.default()

bot = commands.Bot(intents=intents)
bot.command_prefix = "!lv ", "!ㅣㅍ "

@bot.event
async def on_ready():
    print("성공적으로 로그인되었습니다.")

@bot.command()
async def 안녕(ctx):
    await ctx.channel.send("안녕하세요!")

@bot.command()
async def 뭐해(ctx):
    await ctx.channel.send("딱히 무엇을 하진 않아요. 도움만 드리고 있어요.")

@bot.command()
async def 잘가(ctx):
    await ctx.channel.send("안녕히가세요!")

@bot.command()
async def 어디감(ctx):
    Beta = "695240465020223499"
    await ctx.channel.send("<@{}>".format(Beta))

@bot.command()
async def 제작자(ctx):
    Guitar = "734574613387935860"
    await ctx.channel.send("<@{}>".format(Guitar))

botchannel = 918769897163595786

@bot.command()
async def 학습(ctx, *text):
    if ctx.channel.id == botchannel:
        txt = []
        for x in text:
            txt.append(x)
        if len(txt) == 2:
            with open("data.json", "r")as f:
                contents = f.read()
                data = json.loads(contents)
                data[txt[0]] = txt[1]
                print(data)
            f.close()
            with open("data.json", "w") as f:
                json.dump(data, f, ensure_ascii=False)

            f.close()
        else:
            await ctx.send("학습 명령어는 !lv, 학습, (입력), (출력)으로 구성되야해요!(입력과 출력은 띄어쓰기가 있으면 안되요!)")
    else:
        await ctx.channel.send("lv.studio의 봇방에서만 사용 가능합니다.")

@bot.command()
async def 말해(ctx, *text):
    if ctx.channel.id == botchannel:
        txt = text[0]
        with open("data.json", "r")as f:
            contents = f.read()
            data = json.loads(contents)
            try:
                say = data[txt]
                await ctx.channel.send(say)
            except:
                await ctx.channel.send("그 명령어는 학습하지 못했어요! **!lv 학습 (명령어) (대답)**으로 학습시켜주세요!")
        f.close()

bot.run("OTE4NDQ3NzE4NzgxODIwOTY4.YbHZGA.I4a7a_1SsmWHoUpdjxCpADrCskA")

# '''