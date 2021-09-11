import asyncio

import discord
from discord.ext import commands

from scrape_curve_pool import get_cvxCRV_discount_rate, init_contract

from dotenv import dotenv_values

config = dotenv_values(".env")
print(config)

bot = commands.Bot(command_prefix=".")
token = config["BOT_TOKEN"]
guild_id = int(config["GUILD_ID"])
crv_in = 10000

curve_cvxcrv_factory_pool = init_contract(
    "0x9D0464996170c6B9e75eED71c68B99dDEDf279e8"
)


async def send_update():

    discount_rate = get_cvxCRV_discount_rate(
        curve_cvxcrv_factory_pool, crv_in=crv_in * 1e18
    )
    nickname = (
        f"{round(crv_in*(1+discount_rate/100), 2)} ({round(discount_rate, 2)}%)"
    )
    activity_status = "cvxCRV discount"
    await bot.get_guild(guild_id).me.edit(nick=nickname)
    await bot.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.watching, name=activity_status
        )
    )
    await asyncio.sleep(60)  # in seconds


@bot.event
async def on_ready():
    """
    When discord client is ready
    """
    while True:
        await send_update()


bot.run(token)
