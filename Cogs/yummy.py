import discord
from discord.ext import commands
from utils.decorators import command, cooldown
import aiohttp
import json
import decimal


class CryptoCurrency(commands.Cog):
  def __init__(self,client):
    self.client = client

  @command("crypto")  
  async def Yummy(self,ctx):
    async with aiohttp.ClientSession() as r:
      async with r.get("https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=yummy") as r:
        data = await r.json()
        price = decimal.Decimal(data[0]["current_price"])
        high = decimal.Decimal(data[0]["high_24h"])
        low = decimal.Decimal(data[0]["low_24h"])
        pc =  decimal.Decimal(data[0]["price_change_24h"])

        embed = discord.Embed(title = "Yummy Coin Stats", description = 'Recent Stats of Yummy Coin', colour = discord.Colour.blue()) 
        embed.set_image(url='https://assets.coingecko.com/coins/images/15589/large/yummy.png?1621291883')
        embed.add_field(name= 'Current Price', value = f"```{round(price, 7)}```", inline = True)
        embed.add_field(name= 'Market Cap', value = f'```{data[0]["market_cap"]}```', inline = True) 
        embed.add_field(name= 'High 24hrs🔼', value = f"```{round(high, 7)}```", inline = True) 
        embed.add_field(name= 'Low 24hrs 🔽 ', value = f"```{round(low, 7)}```", inline = True) 
        embed.add_field(name= 'Price Change', value = f"```{round(pc, 6)}```", inline = True) 
        embed.add_field(name= 'Price Change %', value = f'```{data[0]["price_change_percentage_24h"]}```', inline = True) 
        embed.add_field(name= 'Market Cap Change', value = f'```{data[0]["market_cap_change_24h"]}```', inline = True) 
        embed.add_field(name= 'Total Supply', value = f'```{data[0]["total_supply"]}```', inline = True) 
        embed.add_field(name= 'Ath', value = f'```{data[0]["ath"]}```', inline = True)
        embed.add_field(
        name="Links",
        value=
        "[Check Stats](https://www.coingecko.com/en/coins/yummy) \n[Invite The Bot](https://discord.com/api/oauth2/authorize?client_id=851362554931445780&permissions=273017959&scope=bot) ",

        inline=False)
   
    await ctx.send(embed = embed)


def setup(client):
    client.add_cog(CryptoCurrency(client))
