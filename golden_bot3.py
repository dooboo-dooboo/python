import discord
import random
from discord.ext import commands

app = commands.Bot(command_prefix='골든아 ', status=discord.Status.online, activity=discord.Game(name="골든아 명령어"))


@app.event
async def on_ready():
    print('다음으로 로그인합니다: ')
    print(app.user.name)
    print('connection was successful')
    await app.change_presence(status=discord.Status.online, activity=discord.Game("'골든아 도움말'을 쳐서 도움말을 얻어 보세요!"))
embed1 = discord.Embed(title='도움말',description='기본 도움말', color=0x00ff00)
embed1.add_field(name='골든아',value='명령어의 시작 부분입니다. 이걸 써야지 명령어가 나옵니다.', inline=True)
embed1.add_field(name='놀자',value='놀기 명령어입니다. 골든아 뒤에 붙이고 놀이 이름을 써 주세요.(찍기, 냥냥놀이)', inline=True)
# embed1.add_field(name='심심해',value='골든봇이 놀이를 추천합니다.', inline=True)
# embed1.add_field(name='재밌는거',value='재밌는거를 보여줍니다.', inline=True)
embed1.add_field(name='도배',value='도배...?', inline=True)

@app.command()
async def 도움말(ctx):
    await ctx.send('주문하신 도움말이에요!')
    await ctx.send(embed=embed1)

@app.command()
async def 놀자(ctx, *text):
    txt = ""
    for x in text:
        txt += x
        txt += ", "
    if txt == "찍기, ":
        await ctx.send("찍기 뒤에 1~100의 수를 입력하세요!")
    elif "찍기, " in txt:
        a = str(random.randint(1, 100))
        if txt[4:-2] == a:
            await ctx.send("당신은 찍신입니다!")
        else:
            await ctx.send("당신은 찍신이 아닙니다...정답은 {} 입니다".format(a))
    elif txt == "냥냥놀이, ":
        a = ""
        for y in range(1, random.randint(2, 100)):
            a += "냥"
        await ctx.send(a)

@app.command()
async def 도배(ctx):
    await ctx.send("저는 도배따위는 하지 않는다고요!")

@app.command()
async def 기타(ctx):
    await ctx.send('저를 만드신 분을 감히... **님** 자 안붙여요?')

@app.command()
async def 기타님(ctx):
    await ctx.send('(만족~) 기타님은 절 만들어주신 분이죠! 하지만 지금은...기타님이 아니라 Starcraft Intermediate님이 되어 버렸죠...')

@app.command()
async def 제작자(ctx):
    await ctx.send('Starcraft Intermediate#5955')

@app.command()
async def Starcraft(ctx, *text):
    txt = ""
    for x in text:
        txt += x
        txt += ", "
    if txt == "Intermediate, ":
        await ctx.send('지금의 기타님!(근데 **님**자는 어디갔어요?)')
    if txt == ("Intermediate님, " or "Intermediate, 님, "):
        await ctx.send('제작자에요! 저는 자랑스럽네요!')


app.run('ODY0NzI1OTAwMjQyNzE0NjY1.YO5owA.9JcC2dorPB_d7ZZBxw1a5TFBwU4')
# 864725900242714665