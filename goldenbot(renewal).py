import disnake
from disnake.ext import commands
import random

description = """golden bot is coming new!"""

intents = disnake.Intents.default()

bot = commands.Bot(command_prefix="골든아 ", description=description, intents=intents)

@bot.event
async def on_ready():
    print("성공적으로 로그인되었습니다.")

@bot.command()
async def 초대(ctx):
    await ctx.send("https://discord.com/api/oauth2/authorize?client_id=909391326200619048&permissions=8&scope=bot%20applications.commands")

@bot.slash_command(name="golden_bot", description="골든봇 명령어입니다.")
async def golden_bot(ctx):
    pass

@golden_bot.sub_command(name="test", description="작동확인하는 명령어입니다.")
async def test(ctx):
    await ctx.response.send_message("작동되었습니다.")

@golden_bot.sub_command(name="golden_bot", description="골든봇에 대한 정보입니다.")
async def golden_bot(inter):
    await inter.response.send_message("11/15일 제작 시작!")

@golden_bot.sub_command(name="random_int", description="1~100 사이의 랜덤 수를 뽑아 줍니다.")
async def random_int(inter):
    a = random.randint(1, 2)
    await inter.response.send_message("{}이(가) 뽑혔습니다!".format(a))

bot.run("OTA5MzkxMzI2MjAwNjE5MDQ4.YZDmqw.0-3u4buHujovfTMMUZaB-G-h2r8")

# '''