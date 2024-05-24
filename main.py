
import discord
import vk
import vk_api

import Config
from discord.ext import commands
from youtube_dl import YoutubeDL
from vk_api.audio import VkAudio


YDL_OPTIONS = {'format': 'worstaudio/best', 'noplaylist': 'False', 'simulate': 'True', 'preferredquality': '192', 'preferredcodec': 'mp3', 'key': 'FFmpegExtractAudio'}
FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
client = commands.Bot(intents=discord.Intents.all(), command_prefix='<')

@client.event
async def help(ctx):
    print('New massage')
    @client.command(alias=['help'])
    async def helper(ctx,* , text):
        await ctx.send('<play is plaing music from youtube, <stop stops if it plays')


@client.command()
async def play(ctx, link):
    if ctx.voice_client is None:
        vc = await ctx.message.author.voice.channel.connect()
        with YoutubeDL(YDL_OPTIONS) as ydl:
            if 'https://' in link:
                info = ydl.extract_info(link, download=False)
            else:
                info = ydl.extract_info(f"ytsearch:{link}", download=False)['entries'][0]

            link = info['formats'][0]['url']
        await ctx.send(f"Now plying {info.get('title')}")
        vc.play(discord.FFmpegPCMAudio(executable="C:ffmpeg/ffmpeg.exe ", source=link, **FFMPEG_OPTIONS))
    else:
        with YoutubeDL(YDL_OPTIONS) as ydl:
            if 'https://' in link:
                info = ydl.extract_info(link, download=False)
            else:
                info = ydl.extract_info(f"ytsearch:{link}", download=False)['entries'][0]

            link = info['formats'][0]['url']
        await ctx.send(f"Now plying {info.get('title')}")
        ctx.voice_client.play(discord.FFmpegPCMAudio(executable="C:ffmpeg/ffmpeg.exe ", source=link, **FFMPEG_OPTIONS))

@client.command(pass_context=True)
async def stop(ctx):
    await ctx.voice_client.disconnect()

@client.command()
async def Vplay(ctx, url):
    if ctx.voice_client is None:
        await ctx.send('Ввелите <Vplay 1.ваш номер телевона 2.пароль от аккаунта ВК')
        d = ctx.message.content
        b = str.removeprefix(d, "<Vplay")
        v = ctx.message.content
        w = str.removeprefix(v, "<Vplay").strip()
        t_b = b[3:14:1]
        t_p = w[16:44:1]
        print(b[3:14:1])
        print(w[16:44:1])
        f = open('password_login.txt', 'w')
        f.write(t_b)
        f.write('\n')
        f.write(t_p)
        vk_session = vk_api.VkApi(t_b, t_p)

        try:
            vk_session.auth()
        except vk_api.AuthError as error_msg:

            print(error_msg)
            return
        i = 0
        vkaudio = VkAudio(vk_session)
        for track in vkaudio.get_iter():
            if i <= 15:
                i += 1
                print(i)
                print(f"Исполнитель : {track.get('artist')}")
                print(f"Название трека : {track.get('title')}")
                print(f"Ссылка на трек(url) : {track.get('url')}")
                print('--------------------------------------------')
                url = track.get('url')

            else:
                break
        vc = await ctx.message.author.voice.channel.connect()
        vc.play(discord.FFmpegPCMAudio(executable="C:ffmpeg/ffmpeg.exe ", source=url, **FFMPEG_OPTIONS))


client.run(Config.token)

'ctx.send'
''' info2 = ydl.extract_info(f"ytsearch:{link}", download=False)['entries'][0]
                info3 = ydl.extract_info(f"ytsearch:{link}", download=False)['entries'][0]
                print(len(info), print(info))

            link = info['formats'][0]['url']
            link2 = info2['formats'][6]['url']
            link3 = info3['formats'][15]['url']
            g = info.get("title", link)
            g2 = info2.get("title", link2)
            g3 = info3.get("title", link3)

            print([g, g2, g3])'''
'-vn -fflags +discardcorrupt -guess_layout_max 0 -i'