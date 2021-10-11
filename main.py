import discord
import os
import requests
import json
from keep_alive import keep_alive

client = discord.Client()

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  
  if message.content.startswith('>fb'):  #fb page
    await message.channel.send('歡迎追蹤我的粉絲專頁!!!\n每周末開播~~\nhttps://www.facebook.com/streamerjasonwu')
  
  if message.content.startswith('>twitch'):  #Twitch
    await message.channel.send('歡迎追蹤我的Twitch!!!\n每周末開播~~\nhttps://www.twitch.tv/jasonwu5')

  if message.content.startswith('>help'):  #help
    await message.channel.send('>fb    粉絲專頁連結\n>twitch    Twitch頻道連結')


keep_alive()

client.run(os.environ['TOKEN'])