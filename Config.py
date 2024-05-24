token = '' ''' <-- paste your token here'''

'''
# -*- coding: utf-8 -*-

import discord
from discord.ext import commands
from Config import token as tykn
import youtube_dl
import os
@bot.event
async def on_message(ctx):
    print('New massage')
    @bot.command(alias=['Hello', 'Hi', 'Sap', 'Whatsapp', 'Hey', 'Welcome', 'Good evening', 'Good afternoon', 'Good morning'])
async def say_hi(ctx,* , text):
    print('Hello')

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='<', intents=intents)
@bot.event
async def on_ready():
    print('Im ready')


domains = ['https://www.youtube.com/', 'http://www.youtube.com/', 'https://youtu.be/', 'http://youtu.be/']
async def check_domains(link):
    for x in domains:
        if link.startswith(x):
            return True
        else:
            return False


@bot.command()
async def play(ctx, *, command=None):
    global server, server_id, name_channel
    author = ctx.author
    if command==None:
        server = ctx.guild
        name_channel = author.voice.channel.name
        voice_channel = discord.utils.get(server.voice_channels, name=name_channel)
    params =command.split(' ')
    if len(params) == 1:
        file_name = params[0]
        server = author.voice.channel.name
        voice_channel = discord.utils.get(server.voice_channels, name=name_channel)
        print('param 1')
    elif len(params) == 3:
        server_id = params[0]
        voice_id = params[1]
        file_name = params[2]
        try:
            server_id = int(server_id)
            voice_id = int(voice_id)
        except:
            await ctx.chanell.send(f'{author.mention}, server or voice id isnt integer!')
            return
        print('params 3')
        server = bot.get_guild(server_id)
        voice_channel = discord.utils.get(server.voice_channels, id=voice_id)
    else:
        await ctx.chanell.send(f'{author.mention}, aint got it')
        return

    voice = discord.utils.get(bot.voice_clients, guild=server,)
    if voice is None:
        await voice_channel.connect()
        voice = discord.utils.get(bot.voice_clients, guild=server,)


    if file_name == None:
        pass
    elif file_name.startswith('http'):
        if not check_domains(file_name):
            await ctx.channel.send(f'{author.mention},link doesnt correct')
            return
        song_there = os.path.isfile('music/song.mp3')
        try:
            if song_there:
                os.remove('song.mp3')
        except PermissionError:
            await ctx.channel.send('we have no key to this door')
            return

        ydl_opt = {
            'format': 'bestaudio/best',
            'postprocessors': [
                {
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192'
                }
            ],
        }

        with youtube_dl.YoutubeDL(ydl_opt) as ydl:
            ydl.download([file_name])
        for file in os.listdir('music/'):
            if file.endswith('.mp3'):
                os.rename(file, 'song.mp3')
        voice.play(discord.FFmpegPCMAudio('music/song.mp3'))
    else:
        voice.play(discord.FFmpegPCMAudio(f'music/{file_name}'))


bot.run(tykn)
'''
'''if (message.guild.me.voice.channel):
    message.channel.send("бот находится в голосовом канале")
else:
    message.channel.send("бот не находится в голосовом канале")'''

'''info = ydl.extract_info(f"ytsearch:{link}", download=False)['entries'][0]
                info2 = ydl.extract_info(f"ytsearch:{link}", download=False)['entries'][0, 1]
                info3 = ydl.extract_info(f"ytsearch:{link}", download=False)['entries'][0, 2]
                print(len(info), print(info))

        link = info['formats'][0]['url']
        link2 = info2['formats'][0]['url']
        link3 = info3['formats'][0]['url']
        g = info.get("title", link)
        g2 = info2.get("title", link2)
        g3 = info3.get("title", link3)

        print([g, g2, g3])
        vc.play(discord.FFmpegPCMAudio(executable="C:ffmpeg/ffmpeg.exe ", source=link, **FFMPEG_OPTIONS))'''


'''s = "1" * 2022
while "11111" or "555" in s:
    if "11111" in s:
        s = s.replace("11111", "555", 1)
    elif "555" in s:
        s = s.replace("555", "5", 1)
print(s)'''

