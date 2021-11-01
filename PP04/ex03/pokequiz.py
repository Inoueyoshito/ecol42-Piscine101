from pokeapi import PokeWiki
from requests.exceptions import RequestException
import discord
from discord.ext import commands

is_test_started: bool = False
count = 0

bot = commands.Bot(command_prefix="!")


@bot.command()
async def pokemontest(ctx):
    global is_test_started
    try:
        pokewiki = PokeWiki()
        pokewiki.fetch_pokemon_info(pokewiki.random_pokemon_name)
        is_test_started = True
        pokeimage = "tmp.png"
        file = discord.File(pokeimage)
        await ctx.send(file=file)

    except RequestException as e:
        print(e)
        await ctx.send("Sorry... I'm not feeling well now...")


BOT_TOKEN = "< Fill in Discord Bot Token here! >"
bot.run(BOT_TOKEN)
