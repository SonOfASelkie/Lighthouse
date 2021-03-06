'''
Created on May 15, 2017

@author: Ronan
'''
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)
#Basic logging code
import asyncio
import aiohttp
from lxml import html
import schedule
import time
import datetime
import discord
client = discord.Client()
#312598338077720577 bot testing general
#266789197132595220 fighting mongooses general

@client.event # This is purely a message I have to tell me that the bot has come online. Will remove in 100% final version as it gets spammy
async def on_ready():
    print(client.user.name + " connected")
    await client.send_message(discord.Object(id='312598338077720577'), 'Ready To Serve <3 ')
    await client.send_message(discord.Object(id='312598338077720577'), 'Type !help for bot commands')

@client.event # This detects when a new member joins the server 
async def on_member_join(member):
    server = member.server
    client.start_private_message(member)
    embed = discord.Embed(colour=discord.Colour(0x860075))
    embed.set_description(title="Welcome to the Fighting Mongooses!")
    embed.set_thumbnail(ulr=message.server.icon_url)
    embed.add_field(name="**Commands:**", value="**!help**: Resends this message to you\n**!subrole**: Sets your role as sub. Only useful if subbing for us\n**!links**: Sends you a message with a heap of useful links\n**!purge NUM**: Purges that many of *your* messages from the channel")
    await client.send_message(message.author, embed=embed)   

@client.event # bulk message detection method, and some of the simpler message "re-sends" are done here
async def on_message(message):
    temp = message.content.lower()
    if  temp.startswith('!help'): # sends a user a DM with the help message
        embed = discord.Embed(colour=discord.Colour(0x860075))
        embed.set_thumbnail(url=message.server.icon_url)
        embed.add_field(name="**Commands:**", value="**!help**: Resends this message to you\n**!subrole**: Sets your role as sub. Only useful if subbing for us\n**!links**: Sends you a message with a heap of useful links\n**!purge NUM**: Purges that many of *your* messages from the channel")
        await client.send_message(message.author, embed=embed) 
        await client.delete_message(message)
    elif temp.startswith('!subrole'): # sets a user's role as a self-role\
        subrole = discord.utils.get(message.server.roles, name='Substitute') # gets the Object value of the role
        await client.add_roles(message.author, subrole)  
        await client.delete_message(message)
        fmt = 'You have now the \'Substitute\' role, {0.mention}.'
        await client.send_message(message.server, fmt.format(message.author))
    elif temp.startswith('!adminpurge'): # purge-messages from channel, admin only
        temp = temp.replace('!adminpurge', '') # reformats message
        num = int(temp) 
        if message.author.permissions_in(message.channel).administrator: # checks if they have permission
            if num < 2: # discord requires at least 2 messages for the purge_from command
                fmt = '{0.mention}, that is too few messages!'
                await client.send_message(fmt.format(message.author))
            elif num > 25: # discord's limit is 100, I wanted an artificial limit of 50
                fmt = '{0.mention}, that is too many messages!'
                await client.send_message(message.channel, fmt.format(message.author))
            else:
                 channel = message.channel
                 await client.purge_from(channel, limit=num)
        else:
            fmt = 'You aren\'t an admin {0.mention}, so you can\'t do that.' # message if conditions aren't met
            await client.send_message(message.channel, fmt.format(message.author))
    elif temp.startswith('!purge'): # standard purge
        temp = temp.replace('!purge ', '') 
        num = int(temp)
        if num < 2:
            fmt = '{0.mention}, that is too few messages!'
            await client.send_message(fmt.format(message.author))
        elif num > 25:
            fmt = '{0.mention}, that is too many messages!'
            await client.send_message(fmt.format(message.author))
        else:
            channel = message.channel
            await client.purge_from(channel, limit=num, check=lambda x: x.author==message.author) # only will delete messages from of the person who sent the command
    elif temp.startswith('!userpurge'): # purge message from a specific user
        temp = temp.replace('!userpurge ', '')
        loc = temp.find(' ')
        num = int(temp[0:loc:1])
        temp = temp[loc+1::]   # this is all breaking the string down into the parts I can actually use
        if num < 2: 
            fmt = '{0.mention}, that is too few messages!'
            await client.send_message(fmt.format(message.author))
        elif num > 25:
            fmt = '{0.mention}, that is too many messages!'
            await client.send_message(fmt.format(message.author))
        else:
            user = discord.utils.get(message.server.members, id=temp)  # creates a new 'user' object with the ID that matches the one entered
            await client.purge_from(message.channel, limit=num, check=lambda x: x.author==user) # deletes those user messages
            await client.delete_message(message)
    elif temp.startswith('!links'): # easy bulk-link command
        if message.channel == '299936518213074954':
           embed = discord.Embed(colour=discord.Colour(0x860075))
           embed.set_author(name="Fighting Mongooses", icon_url=client.user.avatar_url)
           embed.add_field(name="**Useful Links**", value="Instant Invite For this server: http://discord.gg/Q62QeTx \nOWUNI Discord: https://discord.gg/owuniversity \nOWUNI website: https://www.owuniversity.com/\nOWUNI twitch: https://www.twitch.tv/owuniversity\nOWUNI rosters: https://www.owuniversity.com/narosters\nOWUNI brackets: https://www.owuniversity.com/nabracketn\nOWUNI rules: https://www.owuniversity.com/rules\nTeam Google Doc: https://docs.google.com/document/d/1D2nXKPqL_bqCm7EoiSMSwlWhag-w2FyynMAurMuOm8U/edit?usp=sharing")
           await client.send_message(message.author, embed=embed)   
        else:
            embed = discord.Embed(colour=discord.Colour(0x860075))
            embed.set_author(name="Lighthouse", icon_url=client.user.avatar_url)
            embed.add_field(name="**Useful Links**", value="Instant Invite For this server: http://discord.gg/Q62QeTx \nOWUNI Discord: https://discord.gg/owuniversity \nOWUNI website: https://www.owuniversity.com/\nOWUNI twitch: https://www.twitch.tv/owuniversity\nOWUNI rosters: https://www.owuniversity.com/narosters\nOWUNI brackets: https://www.owuniversity.com/nabracketn\nOWUNI rules: https://www.owuniversity.com/rules")
            await client.send_message(message.author, embed=embed)
    elif temp.startswith('!playerstats'): # gets the playtime, level and heros for a user 
        temp = message.content.replace('!playerstats ', '')
        url = await make_url(temp)
        serverURL = message.server.icon_url
        stats_panel = await stat_panel(url, temp, serverURL)
        await client.send_message(message.channel, embed=stats_panel)
    elif temp.startswith('!forced'):
        await dailyUpdateSr()
async def stat_panel(url, message, serverURL): # Forms the message
    # Find page+tree
    page = await makePage(url)     # I use all these URLs for different uses depending on how easy it is to grab the info from each respectively
    tree = html.fromstring(page)   # they all utilize a function that utilizes aiohttp to get the web page, and lxml's html import to convert it to a tree
    mowurl = await make_mow_url(message)
    mowpage = await makePage(mowurl)
    mowtree = html.fromstring(mowpage)
    oburl = await make_buff_url(message)
    obpage = await makePage(oburl)
    obtree = html.fromstring(message)
    # Assemble Variables
    iconUrl = get_icon_url(page, tree)
    srIconUrl = get_sr_icon_url(page, tree)
    sr = get_sr(page, tree)
    srstr = getsrstr(sr)
    playerLevel = get_level(mowpage, mowtree)
    print(playerLevel)
    # Construct FMT messages
    fmtpageurls = '[Master Overwatch]({}) ~|~ [Overbuff]({})'
    fmtlevel = '*{}*'
    fmtsr = '**Skill Rating:** {}'
    fmtsrstr = 'Current Tier: {}'
    # Construct message
    embed = discord.Embed(title='Links:', colour=discord.Colour(0xe91e63), description=fmtpageurls.format(mowurl, oburl), timestamp=datetime.datetime.utcnow()) #creation of the embed message
    embed.set_thumbnail(url=iconUrl)
    embed.set_footer(text='Fighting Mongooses', icon_url=serverURL)
    embed.set_author(name=message, url=url, icon_url=srIconUrl)
    embed.add_field(name="**Level:**", value=fmtlevel.format(playerLevel))
    embed.add_field(name=fmtsr.format(sr), value = fmtsrstr.format(srstr)) # field for SR
    return embed

def get_sr(page, tree): # get the Skill Rating value f/ the playoverwatch webpage
    sr = tree.xpath(".//div[@class='competitive-rank']/div/text()")[0]
    return sr 
 
def get_icon_url(page, tree): # get the player icon f/ the playeroverwatch webpage
    url = tree.xpath('.//img[@class="player-portrait"]/@src')[0]
    return url

def get_sr_icon_url(page, tree): # get the sr icon f/ the playoverwatch webpage
    url = tree.xpath('.//div[@class="competitive-rank"]/img/@src')[0]
    return url

def get_level(page, tree): # get the user-level f/ the masteroverwatch webpage
    level = tree.xpath('.//div[@class="header-avatar"]/span/text()')[0]
    return level

async def make_url(message): # gets the URL for playeroverwatch
    url = 'https://playoverwatch.com/en-us/career/pc/us/'
    message = message.replace(' ', '')
    url = url+message
    url = url.replace("#", "-")
    return url

async def make_mow_url(message): # figures out the URL for masteroverwatch
    url = 'https://masteroverwatch.com/profile/pc/us/'
    url = url+message
    url = url.replace('#', '-')
    return url

async def make_buff_url(message): # figures out the URL for overbuff
    url = 'https://www.overbuff.com/players/pc/'
    url = url+message
    url = url.replace('#', '-')
    return url

def getsrstr(sr): # brute force if-else if-else statements b/c i'm lazy
    sr = int(sr)
    if sr < 1500:
        return 'Bronze'
    elif sr < 2000:
        return 'Silver'
    elif sr < 2500:
        return 'Gold'
    elif sr < 3000:
        return 'Platinum'
    elif sr < 3500:
        return 'Diamond'
    elif sr < 4000:
        return 'Master'
    else:
        return 'Grand Master'
    
async def dailyUpdateSr():
    tempchannel = client.get_channel('317334084613570581')
    await client.purge_from(tempchannel, limit=20)
    serverURL = client.get_channel('317334084613570581').server.icon_url
    members = ['lafon#1272', 'SonOfASelkie#1524', 'CrispyMD#1678', 'Pillz#11316', 'limedrop#1111', 'Trafficcone#1832']
    for name in members:
        url = await make_url(name)
        stats_panel = await stat_panel(url, name, serverURL)
        await client.send_message(tempchannel, embed=stats_panel)
        
    schedule.every().day.at("00:00").do(dailyUpdateSr) # runs the dailyUpdateSr command at that time each day
    while 1:
        schedule.run_pending()
        time.sleep(1)
    
async def makePage(url): # uses aiohttp to get the webpage. aiohttp > requests b/c aiohttp doesn't freeze the code while making the request
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            return (await resp.text())
        
        
client.run('MzEyNTg5MTAxMDA0MDk1NDkw.DAC0sQ.ch4djGO-YZlvyzHB40Ov57ehMUI') # This token is my bot's specific token that I use to call it


