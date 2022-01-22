import discord
import random
import os 

Websites = ["https://www.energy.gov/ne/articles/advantages-and-challenges-nuclear-energy#:~:text=Nuclear%20energy%20protects%20air%20quality,medical%20field%20to%20space%20exploration.","https://www.eia.gov/energyexplained/nuclear/","https://www.eia.gov/energyexplained/nuclear/nuclear-power-plants.php",]

my_secret = os.environ['FishySecret']

client = discord.Client()

@client.event
async def on_ready():

  print("Le educational bot is online and being fishy (as always)")

  print("---------------------------------------------")
  print("The prefix is &\n\n&source: to show creditable websites of nuclear energy")
  #Prefixes Commands ^^^
  print("---------------------------------------------")

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith("prefix"):
    cycle = 0
    await message.channel.send(Websites[cycle])
    cycle = cycle + 1
    if cycle == 2:
      cycle = 1




client.run(my_secret)

