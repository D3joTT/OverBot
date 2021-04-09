import json

import discord
from discord.ext import commands

with open('config/config.json', 'r') as cjson:
    config = json.load(cjson)

bot = commands.Bot(command_prefix=config["prefix"])
bot.remove_command('help')

png = config["img"]


@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name=config["status"]))

    print("   ___                 ____        _   \n"
          "  / _ \__   _____ _ __| __ )  ___ | |_ \n"
          " | | | \ \ / / _ \ '__|  _ \ / _ \| __|\n"
          " | |_| |\ V /  __/ |  | |_) | (_) | |_ \n"
          "  \___/  \_/ \___|_|  |____/ \___/ \__|")


@bot.command(name='test')
async def test(ctx):
    await ctx.message.delete()


bot.run(config["token"])
