import discord
TOKEN = "OTAzMjk5NzE1MzM5Mjg0NTcw.YXq9ag.0Vr_ctqP26pN3L0W7cHiWZ_ZBHQ"

client = discord.Client() 

@client.event
async def on_ready():
    print("ROGIN IS READY")

@client.event
async def on_message(message):
    if message.author.bot:
        return 
    if message.content ==  "Hello":
        await message.channel.send("Hello!")


client.run(TOKEN)
