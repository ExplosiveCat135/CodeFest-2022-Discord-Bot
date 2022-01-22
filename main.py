import discord
import random
import os 

Websites = ["https://www.energy.gov/ne/articles/advantages-and-challenges-nuclear-energy#:~:text=Nuclear%20energy%20protects%20air%20quality,medical%20field%20to%20space%20exploration.","https://www.eia.gov/energyexplained/nuclear/","https://www.eia.gov/energyexplained/nuclear/nuclear-power-plants.php","https://energyeducation.ca/encyclopedia/Nuclear_power_plant","https://en.wikipedia.org/wiki/Nuclear_power_plant#:~:text=A%20nuclear%20power%20plant%20(sometimes,a%20generator%20that%20produces%20electricity.","https://www.encyclopedie-energie.org/en/nuclear-energy-brief-history/"]

my_secret = os.environ['FishySecret']

client = discord.Client()

@client.event
async def on_ready():

  print("Le educational bot is online and being fishy (as always)")

  print("---------------------------------------------")
  print("The prefix is &\n\n&website: to show websites about nuclear energy\n&history: to show glimpses of history about nuclear power plants.")
  #Prefixes Commands ^^^
  print("---------------------------------------------")

def readQuotes(fileName):
  myFile = open(fileName,"r")
  Very_Fishy_Quotes = []
  for line in myFile:
    if (line != '\n'):
      Very_Fishy_Quotes.append(line.strip('\n'))

  return Very_Fishy_Quotes
  myFile.close()

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  
  if message.content.startswith("&website"):
    
    await message.channel.send(Websites[random.randint(0,len(Websites-1))

  if message.content.startswith("&history"):
    my_fishy = readQuotes("history_about_nuclear_energy.txt") 
    await message.channel.send(random.choice(my_fishy))

  
    




client.run(my_secret)

