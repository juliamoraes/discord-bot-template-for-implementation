from reprlib import db
import discord 
import os
#----------- import discord client------------
client = discord.Client()

#------------ registering client event using fuction call back
# ----------- bot get the user name client 
@client.event 
async def on_ready():

print(" {0.user}".format(client)) # 0 gets replace by client 

# ----------------- event when the bot is ready and working display message
@client.event  
async def on_message():
 if message.author == client.user: # bot response to author just return no response
     return
   


if message.content.startswith(""): # user text display here
  await mesage.channel.send("")


if message.content.startswith("user input"): # condition to bot response
   await message.channel.send("bot input") 

client.run(os.getenv("TOKEN")) # token should be put on .env file as security reasons

