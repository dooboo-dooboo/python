import discord
from discord.ext import commands
bot = commands.Bot(command_prefix='', activity=discord.Game(name="N도움/업데이트 완료"))
TOKEN = 'ODgzNzA2NTYwNjg4MzA0MTU4.YTN13g.VGEiGONgMA1AcffuUUIRqAfUEuo'

@bot.event
async def on_message(msg):
    if msg.author.bot:
        return None
    if msg.content == "N도움":
        dm_channel = await msg.author.create_dm()
        await dm_channel.send("도움말!\n\n명령어는 서버 관리자만 실행 가능해요!\nN공지 라는 주제가 적힌 채널에\n메시지를 보낼 수 있어요!\n\nN공지 공지내용 으로 작성하면\nN공지 라는 주제의 채널에\n메시지가 가요!\nC공지 공지내용으로 입력하면 N 공지내용과\n같지만 체크박스 반응 표시되요!\n\n업데이트 내역 보려면 UpDate 입력\n\n\n\n개발 : Starcraft Intermediate(SI)")
    elif msg.content == "UpDate":
        await msg.channel.send("1.0.0 생성(9/5)\n1.1.0 C 명령어와 업데이트 내역 생성(9/6)\n1.1.1 UpDate 명령어에 날짜 추가(9/6)\n1.1.2 관리자가 아닌 유저가 공지를 보내는 오류 해결(9/13)\n1.2.1 접두사 변경(N, C=>N공지, C공지)(10/21)")
    channels = msg.guild.text_channels
    for ch in channels:
        if ch.topic is not None and "N공지" in ch.topic and msg.content[0:3] == "N공지" and msg.content[3] == " ":
            if msg.author.guild_permissions.administrator:
                await ch.send(msg.content[4:])
        elif ch.topic is not None and "N공지" in ch.topic and msg.content[0:3] == "C공지" and msg.content[3] == " ":
            if msg.author.guild_permissions.administrator:
                m = await ch.send(msg.content[4:])
                await m.add_reaction("\U00002705")

bot.run(TOKEN)
# msg.author.guild_permissions.administrator
# msg.author.guild_permissions.manage_messages