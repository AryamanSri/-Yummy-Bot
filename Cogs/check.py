import discord
from discord.ext import commands
from utils.decorators import command, cooldown
import aiohttp
import json
import decimal


class CheckCoin(commands.Cog):
  def __init__(self,client):
    self.client = client

  @command("c")  
  async def check(self,ctx, coin):
    async with aiohttp.ClientSession() as r:
      async with r.get(f"https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids={coin}") as r:
        data = await r.json()
        price = decimal.Decimal(data[0]["current_price"])
        high = decimal.Decimal(data[0]["high_24h"])
        low = decimal.Decimal(data[0]["low_24h"])
        pc =  decimal.Decimal(data[0]["price_change_24h"])

        embed = discord.Embed(title = f" Stats", description = f'Recent Stats of {coin}  ', colour = discord.Colour.blue()) 
        embed.add_field(name= '💸 Price', value = f"{round(price, 10)} $", inline = False)
        embed.add_field(name= '💷 Market Cap', value = f'{data[0]["market_cap"]}$', inline = False) 
        embed.add_field(name= '📈 High 24hrs', value = f"{round(high, 10)}$", inline = False) 
        embed.add_field(name= '📉 Low 24hrs 🔽 ', value = f"{round(low, 10)}$", inline = False) 
        embed.add_field(name= 'Price Change', value = f"{round(pc, 10)}$", inline = False) 
        embed.add_field(name= 'Price Change %', value = f'{data[0]["price_change_percentage_24h"]}%', inline = True) 
        embed.add_field(name= 'Market Cap Change', value = f'{data[0]["market_cap_change_24h"]}$', inline = True) 
        embed.add_field(name= 'Total Supply', value = f'{data[0]["total_supply"]}', inline = True) 

        
        await ctx.send(embed = embed)


  


def setup(client):
    client.add_cog(CheckCoin(client))
