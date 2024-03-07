# import discord
# from VKDT.Discord.discord_main import client
# from discord.ext import commands
#
# bot = commands.Bot(command_prefix='>', self_bot=True, intents=discord.Intents().all())
#
#
# @client.command()
# async def Test(ctx):
#     await ctx.send(f'{ctx.message.author} Test')
#     print(f'{client.user.name}: Test')
#
#
# @bot.command(pass_context=True, aliases=['Test'])
# async def Test(ctx):
#     await ctx.send(f'{ctx.message.author} Test')
#     print(f'{client.user.name}: Test')