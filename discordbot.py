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
#312598338077720577 bot testing general
#266789197132595220 fighting mongooses general

# git init # to init the git repo
# http://rogerdudler.github.io/git-guide/
# git remote add heroku  https://linkgiven by heroku #to be done only once
# git remote add github https://github.com/saikpr/
# git commit -a -m "Some message"
# git push github
# git push heroku 

@client.event
async def on_ready():
    print(client.user.name + " connected")
    await client.send_message(discord.Object(id='312598338077720577'), 'Ready To Serve <3 ')
    await client.send_message(discord.Object(id='312598338077720577'), 'Type !help for bot commands')

@client.event
async def on_member_join(member):
    server = member.server
    client.start_private_message(member)
    fmt = 'Welcome {0.mention} to {1.name} !'
    fmt2 = 'Welcome to {1.name}, {0.mention}. Use !help to ping for commands, and !subrole if you are a sub for us.'
    await client.send_message(server,  fmt.format(member, server) )
    await client.send_message(member, fmt2.format(member, server) )
    fmt = """Commands:
         !help = Sends this message to you
         !subrole = Sets your role as sub. Please only use if actually a sub. 
         !ytsearch(keyword) = Prints the first result from a youtube search with keyword. Keyword must be in parenthesis.
         !gisearch(keyword) = Attaches the first result from a google-image search with keyword. Keyword must be in parenthesis.
         !queue(keyword) = Queues the first youtube-video result in the music channel. Keyword must be in parenthesis.
         CALENDAR COMMANDS
     """
    await client.send_message(member, fmt)

@client.event
async def on_message(message):
    temp = message.content.lower()
    if temp.startswith('!help'):
        fmt = """Commands:
                   !help = Sends this message to you
                   !subrole = Sets your role as sub. Please only use if actually a sub. 
                   !ytsearch(keyword) = Prints the first result from a youtube search with keyword. Keyword must be in parenthesis.
                   !gisearch(keyword) = Attaches the first result from a google-image search with keyword. Keyword must be in parenthesis.
                   !queue(keyword) = Queues the first youtube-video result in the music channel. Keyword must be in parenthesis.
                   CALENDAR COMMANDS
         """
        await client.send_message(message.author, fmt)
        await client.delete_message(message)
    elif temp.startswith('!subrole'):
      subrole = discord.utils.get(message.server.roles, name='Substitute')
      await client.add_roles(message.author, subrole)  
      await client.delete_message(message)
      fmt = 'You have now the \'Substitute\' role, {0.mention}.'
      await client.send_message(message.server, fmt.format(message.author))
#
        
client.run('MzEyNTg5MTAxMDA0MDk1NDkw.DAC0sQ.ch4djGO-YZlvyzHB40Ov57ehMUI')