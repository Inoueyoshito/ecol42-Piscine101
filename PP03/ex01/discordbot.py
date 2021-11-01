import discord
from PIL  import Image, ImageDraw
import os

TOKEN = "OTAzMjk5NzE1MzM5Mjg0NTcw.YXq9ag.0Vr_ctqP26pN3L0W7cHiWZ_ZBHQ"

client = discord.Client()

@client.event
async def on_ready():
    print("ROGIN SUCCESSFULLY")

@client.event
async def on_message(message):
    if message.author.bot:
        return 
    if "!draw " in message.content:
        message.content = message.content.removeprefix("!draw ")
        img = Image.new("RGB",(100,100),color = 'Black')
        d = ImageDraw.Draw(img)
        d.text((0,45),"{}".format(message.content),fill=(255,255,255))
        img.save("img.png")
        image = discord.File("/Users/hyoshida/git@vogsphere-v2.42tokyo.jp:vogsphere/intra-uuid-bfa8e15c-64c8-48bb-a942-825d41367530-3856008/python03/ex01/img.png",filename="img.png")
        await message.channel.send(file=image)

        
client.run(TOKEN)

