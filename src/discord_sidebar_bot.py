import asyncio
import os

import discord
from discord.ext import commands

from scrape_curve_pool import get_cvxCRV_discount_rate, init_contract

bot = commands.Bot(command_prefix=".")
token = os.getenv("BOT_TOKEN")
guild_id = int(os.getenv("GUILD_ID"))

sushiswap_router_contract = init_contract(
        "0xd9e1cE17f2641f24aE83637ab66a2cca9C378B9F"
    )


async def send_update():

    discount_rate = get_cvxCRV_discount_rate(sushiswap_router_contract)
    nickname = (
        f"{round(1000*(1+discount_rate/100), 2)} ({round(discount_rate, 2)}%)"
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
