#By Ineub
#Edit only
#Undeployable, revised and left undeployable


import discord


client = discord.Client()

@client.event
async def on_ready():
    print(client.user.id)
    print("no god plese no!!!!! no!!!!!")
    game = discord.Game("이늡 바부")
    await client.change_presence(status=discord.Status.idle, activity=game)



@client.event
async def on_message(message):
    if message.content.startswith("크림 안녕"):
        await message.channel.send("안녕~!")
    if message.content.startswith("크림 명령어"):
        await message.channel.send("```cream_E 명령어:크림 안녕,크림 바바, 크림 바부, 크림 찬양해(하면 좋은일이 있을지도...?)```")
    if message.content.startswith("크림 욕해봐"):
        await message.channel.send("||ㅆ1발||")
    if message.content.startswith("크림 찬양해"):
        await message.channel.send("나도 널 찬양한다!!!")
    if message.content.startswith("크림 바바"):
        await message.channel.send("잘하...힝")
    if message.content.startswith("크림 바부"):
        await message.channel.send("응 자기소개 잘~한다")


client.run(Njc2Njg4MDA1NDE4OTc1MjUy.XkQR-w.upIpbc2pY6eCzvTrjoq0n7_uKIU)
