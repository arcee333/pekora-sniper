import discord
import re
import subprocess
from discord.ext import commands
import configparser

config = configparser.ConfigParser()
config.read('config.ini')
bottoken = config.get('General', 'bottoken')

TOKEN = bottoken

SERVER_ID = 1307760060470001664
CHANNEL_ID = 1392921856616697926

bot = commands.Bot(command_prefix='!', self_bot=True)

URL_PATTERN = re.compile(r'https?://\S+|www\.\S+')

NUMBER_PATTERN = re.compile(r'https?://www\.pekora\.zip/catalog/(\d+)/')

@bot.event
async def on_ready():
    print(f'logged in as {bot.user.name}')

@bot.event
async def on_message(message):
    if message.guild and message.guild.id == SERVER_ID and message.channel.id == CHANNEL_ID:
        url_match = URL_PATTERN.search(message.content)
        if url_match:
            url = url_match.group()
            print(f'detected URL: {url}')
            number_match = NUMBER_PATTERN.search(url)
            if number_match:
                number = number_match.group(1)
                with open("id.txt", "w") as file:
                    file.write(str(number))
                print(f'extracted id: {number}')
                subprocess.run(["python", "snipe.py"])   
            else:
                print('no id in url')
    
    await bot.process_commands(message)

bot.run(TOKEN)