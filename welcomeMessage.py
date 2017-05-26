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
import discord
client = discord.Client()

@client.event
async def on_member_join(member):
    server = member.server
    fmt = 'Welcome {0.mention} to {1.name} !'
    fmt2 = 'Welcome to {1.name}, {0.mention}. Use !help to ping for commands!'
    await client.send_message(server,  fmt.format(member, server) )
    await client.send_message(member, fmt2.format(member, server) )

client.run('MzEyNTg5MTAxMDA0MDk1NDkw.C_9GOQ.9SU_T7roFuaCVnVEM3a6h2ybo74')
