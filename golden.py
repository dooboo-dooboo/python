import discord
token = "2e869b579e7271f5e681e3cfde1147ff5e2d2d52cbee3dfa85ab740282ca6d6f"
client = discord.Client()

@client.event
async def on_ready():
    print("봇 준비 완료!")