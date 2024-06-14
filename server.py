#Class Libraries 
import discord
import os
import random 
from dotenv import load_dotenv
from ec2_metadata import ec2_metadata


#Initializing Variables
load_dotenv()

client = discord.Client()
token = os.getenv('TOKEN')

#Initializing Bot
@client.event
async def on_ready():
    print("Logged in as a bot {0.user}".format(client))

#Setting up bot responses
@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    channel = str(message.channel.name)
    user_message = str(message.content)

    print(f'Message {user_message} by {username} on {channel}')

    if message.author == client.user:
        return
    
    if channel == "random":
        if user_message.lower() == "hello" or user_message.lower() == "hi":
            await message.channel.send(f'Hi {username}')
        #Other string options
        elif user_message.lower() == "ring":
            await message.channel.send(f'Green green yellow {username}')
        #Other string options
        elif user_message.lower() == "hey pookie":
            await user_message.channel.send(f'Purr {username}')
        #Returning instance data
        elif user_message.lower() == "ec2 data":
            await message.channel.send(f'Your instance data is {ec2_metadata.instance} Your EC2 Data: {ec2_metadata.region}')
        else:
            await message.channel.send("Error")

#Run the bot w/token
client.run(token)

