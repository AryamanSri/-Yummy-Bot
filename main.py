import discord
from discord.ext import commands
import os
import keep_alive

#prefix 
client = commands.Bot(command_prefix=['$'])


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'Cogs.{filename[:-3]}')

#to load cogs
@client.command(hidden=True)
@commands.is_owner()
async def load(ctx, extension):
    client.load_extension(f'Cogs.{extension}')
    await ctx.send('Succesfully loaded module')


@client.command(hidden=True)
@commands.is_owner()
async def unload(ctx, extension):
    client.unload_extension(f'Cogs.{extension}')
    await ctx.send('Succesfully unloaded module')


@client.command(hidden=True)
@commands.is_owner()
async def reload(ctx, extension):
    client.reload_extension(f'Cogs.{extension}')
    await ctx.send('Succesfully reloaded module')


class CogName(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


def setup(bot):
    bot.add_cog(CogName(bot))

#bot playing status
@client.event
async def on_ready():
        activity = discord.Game(name="Yummy", type=2)
        await client.change_presence(status=discord.Status.do_not_disturb, activity=activity)

#help command
class NewHelpName(commands.MinimalHelpCommand):
    async def send_pages(self):
        destination = self.get_destination()
        for page in self.paginator.pages:
            emby = discord.Embed(description=page, colour = discord.Colour.red(), title = ":bookmark_tabs: | Help Menu")
            await destination.send(embed=emby)

client.help_command = NewHelpName()

keep_alive.keep_alive()
client.run(os.environ["TOKEN"])
