# bot.py

# Bot Name: Roboross (name created by David Miller)
import asyncio
import discord

from discord.ext import commands

# Constants
PREFIX = '~'
TOKEN = 'NTg4NDk2MjA0MzU1MDc2MDk5.XgVVQg.o92A-bYcpiHP1QhG23zT0k5OO0U'


class AudioCmds(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def insult(self, ctx):
        # Joins Voice Channel
        channel = ctx.message.author.voice.channel
        if ctx.voice_client is not None:
            return await ctx.voice_client.move_to(channel)

        await channel.connect()

        source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio('C:\\Roboross_Bot\\audio_luke\\luke_clip_0.mp3'))
        ctx.voice_client.play(source, after=lambda e: print("Player error: %s" % e) if e else None)

        await ctx.send('Now Insulting')

    @commands.command()
    async def stop(self, ctx):
        await ctx.voice_client.disconnect()

    @commands.command()
    async def hello(self, ctx):
        if ctx.message.author == bot.user:
            return

        elif 'kyle' in ctx.message.content:
            await ctx.message.channel.send('Wagwannnn! What?')

        elif 'david' in ctx.message.content:
            channel = ctx.message.author.voice.channel
            if ctx.voice_client is not None:
                return await ctx.voice_client.move_to(channel)

            await channel.connect()

            source = discord.PCMVolumeTransformer(
                discord.FFmpegPCMAudio('C:\\Roboross_Bot\\audio_hello\\david_hello_0.mp3'))
            ctx.voice_client.play(source, after=lambda e: print("Player error %s" % e) if e else None)

        elif 'luke' in ctx.message.content:
            channel = ctx.message.author.voice.channel
            if ctx.voice_client is not None:
                return await ctx.voice_client.move_to(channel)

            await channel.connect()

            source = discord.PCMVolumeTransformer(
                discord.FFmpegPCMAudio('C:\\Roboross_Bot\\audio_hello\\luke_hello_0.mp3'))
            ctx.voice_client.play(source, after=lambda e: print("Player error %s" % e) if e else None)

        if not ctx.voice_client.is_playing():
            print("Not Playing audio right now")



    @commands.command()
    async def damn(self, ctx):

        channel = ctx.message.author.voice.channel
        if ctx.voice_client is not None:
            return await ctx.voice_client.move_to(channel)

        await channel.connect()

        source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio('C:\\Roboross_Bot\\audio_misc\\damm_bro.mp3'))

        ctx.voice_client.play(source, after=lambda e: print("Player error %s" % e) if e else None)


bot = commands.Bot(command_prefix=PREFIX, description='Plays funny audio clips')


@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))


bot.add_cog(AudioCmds(bot))
bot.run(TOKEN)
