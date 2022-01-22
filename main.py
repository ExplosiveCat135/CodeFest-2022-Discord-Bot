import discord
import random
import os 

Websites = ["https://www.energy.gov/ne/articles/advantages-and-challenges-nuclear-energy#:~:text=Nuclear%20energy%20protects%20air%20quality,medical%20field%20to%20space%20exploration.","https://www.eia.gov/energyexplained/nuclear/","https://www.eia.gov/energyexplained/nuclear/nuclear-power-plants.php","https://energyeducation.ca/encyclopedia/Nuclear_power_plant","https://en.wikipedia.org/wiki/Nuclear_power_plant#:~:text=A%20nuclear%20power%20plant%20(sometimes,a%20generator%20that%20produces%20electricity."]

my_secret = os.environ['FishySecret']

client = discord.Client()

@client.event
async def on_ready():

  print("Le educational bot is online and being fishy (as always)")

  print("---------------------------------------------")
  print("The prefix is &\n\n&website: to show websites about nuclear energy\n&history: to show glimphs of history about nuclear power plants.")
  #Prefixes Commands ^^^
  print("---------------------------------------------")

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  
  if message.content.startswith("&website"):
    
    await message.channel.send(Websites[random.randint(0,4)])

  if message.content.startswith("&basic"):
    await message.channel.send()

  
    




client.run(my_secret)

