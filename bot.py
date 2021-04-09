import json

import discord

with open('config/config.json', 'r') as cjson:
    config = json.load(cjson)

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name=config["status"]))

    print("   ___                 ____        _   \n"
          "  / _ \__   _____ _ __| __ )  ___ | |_ \n"
          " | | | \ \ / / _ \ '__|  _ \ / _ \| __|\n"
          " | |_| |\ V /  __/ |  | |_) | (_) | |_ \n"
          "  \___/  \_/ \___|_|  |____/ \___/ \__|")


bot.run(config["token"])
