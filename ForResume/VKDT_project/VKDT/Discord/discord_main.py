import discord
# from discord.ext import commands
import os
import asyncio
from dotenv import load_dotenv
from discord_settings.settings import Settings
from discord_commands.CommandSettings import commands
from VKDT.Discord.discord_commands.CommandSettings import test as test
load_dotenv()
settings = Settings()


class DiscordBot:

    def __init__(self):
        self.intents = settings.get_intents()
        self.commands = commands.Bot(command_prefix=settings.get_prefix(), intents=self.intents)
        self.client = self.commands


client = DiscordBot().client
# client.load_extension(f'discord_commands.{test}')
# @client.command(name='play')
# async def play(ctx, *, args):
#     vc = await ctx.message.author.voice.channel.connect()
#
#     with ytdl as ydl:
#         if 'https://' in args:
#             info = ydl.extract_info(args, download=False)
#             await ctx.send(f'Проигрывается: {args}')
#         else:
#             info = ydl.extract_info(f'ytsearch:{args}', download=False)['entries'][0]
#
#         link = info['formats'][0]['url']
#
#         vc.play(discord.FFmpegPCMAudio(executable='ffmpeg\\bin\\ffmpeg.exe', source=link, **ffmpeg_options))
#
#
#
# @client.command(name='pause', help='This command pauses the song')
# async def pause(ctx):
#     voice_client = ctx.message.guild.voice_client
#     if voice_client.is_playing():
#         await voice_client.pause()
#     else:
#         await ctx.send("The bot is not playing anything at the moment.")
#
#
# @client.command(name='resume', help='Resumes the song')
# async def resume(ctx):
#     voice_client = ctx.message.guild.voice_client
#     if voice_client.is_paused():
#         await voice_client.resume()
#     else:
#         await ctx.send("The bot was not playing anything before this. Use play_song command")
#
#
# @client.command(name='stop', help='Stops the song')
# async def stop(ctx):
#     voice_client = ctx.message.guild.voice_client
#     if voice_client.is_playing():
#         await voice_client.stop()
#     else:
#         await ctx.send("The bot is not playing anything at the moment.")

# No corrected
# @client.command()
# async def volume(ctx, *, args):
#     args = YTDLSource.volume
#
#
# @client.command()
# async def Test(ctx):
#     await ctx.send(f'{ctx.message.author} Test')
#     print(f'{client.user.name}: Test')
#


#
# @client.command()
# async def ping(ctx):
#     ping = client.ws.latency
#     await ctx.send((ping))
#     print(ping)
#
#
# @client.command()
# @commands.is_owner()
# async def shutdown(context):
#     print('Бот выключен.')
#     exit()
#
#
# @client.event
# async def on_ready():
#     print('Logged in as:\n{0.user.name}\n{0.user.id}'.format(client))
for filename in os.listdir('./discord_commands/cogs'):

    if filename.endswith('.py'):
        print(filename)
        client.load_extension(f'./discord_commands/cogs.{filename[:-3]}')

client.run(os.getenv('Discord_key'))
