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
import requests
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
        stats_panel = await stat_panel(url, temp)
        await client.send_message(message.channel, embed=stats_panel)
async def stat_panel(url, message): # Forms the message
    # Find page+tree
    page = requests.get(url)
    tree = html.fromstring(page.content)
    # Assemble Variables
    iconUrl = get_icon_url(page, tree)
    srIconUrl = get_sr_icon_url(page, tree)
    sr = get_sr(page, tree)
    srstr = getsrstr(sr)
    level = get_level(page, tree)
    mowurl = await make_mow_url(message)s
    # Construct message
    embed = discord.Embed(title='Master Overwatch', colour=discord.Colour(0xe91e63), url=mowurl) # creation of the embed message
    embed.set_thumbnail(url=iconUrl)
    embed.set_author(name=message, url=url, icon_url=srIconUrl)
    # embed.add_field(name="**Level**", level)
    fmtsr = '**Skill Rating:** {}'
    fmtsrstr = 'Current Tier: {}'
    embed.add_field(name=fmtsr.format(sr), value = fmtsrstr.format(srstr)) # field for SR
    return embed
def get_sr(page, tree):
    sr = tree.xpath(".//div[@class='competitive-rank']/div/text()")[0]
    return sr  
def get_icon_url(page, tree):
    url = tree.xpath('.//img[@class="player-portrait"]/@src')[0]
    return url
def get_sr_icon_url(page, tree):
    url = tree.xpath('.//div[@class="competitive-rank"]/img/@src')[0]
    return url
def get_level(page, tree):
    level = 1
async def make_url(message): # gets the URL
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
def getsrstr(sr): # brute force if-else if-else staement b/c i'm lazy
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
        
client.run('MzEyNTg5MTAxMDA0MDk1NDkw.DAC0sQ.ch4djGO-YZlvyzHB40Ov57ehMUI')


