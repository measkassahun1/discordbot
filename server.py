#Import Class Libraries
import discord
import os
import random
from ec2_metadata import ec2_metadata 

#Print EC2 instance metadata for verification
print('ec2_metadata.region', ec2_metadata.region)
print('ec2_metadata.instance_id', ec2_metadata.instance_id)

#Set up Discord intents to enable message content access
intents = discord.Intents.default()
intents.messages = True
intents.message_content = True

#Create a Discord client instance with the specified intents
client = discord.Client(intents=intents)

#Retrieve the bot token from environment
token = str(os.getenv('TOKEN'))

#Initializing bot and handler for when the bot is ready and logged in
@client.event
async def on_ready():
    print("Logged in as a bot {0.user}".format(client))

#Event handler for when a message is sent in a channel
@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    channel = str(message.channel.name)
    user_message = str(message.content)

    #Log the message details to the console
    print(f'Message {user_message} by {username} on {channel}')

#Ignore messages sent by the bot itself
    if message.author == client.user:
        return
#Messages and response to messages in the "general" channel  
    if channel == "general":
        if user_message.lower() == "hello" or user_message.lower() == "hi":
            await message.channel.send(f'Hi {username}')
        elif user_message.lower() == "ring":
            await message.channel.send(f'Green green yellow {username}')
        elif user_message.lower() == "hey pookie":
            await message.channel.send(f'Purr {username}')
        elif user_message.lower() == "ec2 data":
            await message.channel.send(f'Your instance data is {ec2_metadata.region} + {ec2_metadata.instance_id}')
        else:
            await message.channel.send("Error") #If unknown/error message is sent, bot respond with 'error'
      

# Run the bot with token
client.run(token)
