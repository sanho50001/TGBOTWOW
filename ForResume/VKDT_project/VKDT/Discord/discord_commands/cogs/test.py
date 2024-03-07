import discord
from discord.ext import commands


class Bot(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Logged in as:\n{0.user.name}\n{0.user.id}'.format(self.client))

    @commands.command(aliases=['Test'])
    async def Test(self, ctx):
        await ctx.send(f'{ctx.message.author} Test')
        print(f'{self.client.user.name}: Test')


def setup(client):
    client.add_cog(Bot(client))
