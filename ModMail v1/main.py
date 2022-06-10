import discord , json , os
from discord.ext import commands
from alive import online

file = open('config.json','r')
data = file.read()
config = json.loads(data)
PREFIX = config['PREFIX']
TOKEN = config['TOKEN']

bot = commands.Bot(command_prefix = PREFIX,case_insensitive = True)

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    elif '<@983294613433507920>' in message.content.lower():
        await message.channel.send(f' Hey! {message.author.mention} Do you need help? dm me ')
        await bot.process_commands(message)     
    else:
        await bot.process_commands(message)
        
       
@bot.command()
async def ping(ctx):
    await ctx.send(round(bot.latency*1000))

@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.do_not_disturb,activity = discord.Activity(type=discord.ActivityType.watching, name = f"My dm's | for help "))
    print('--------------------------------\n Your Modmail bot is ready.\nLogin as {0.user}\n--------------------------------'.format(bot))

for filename in os.listdir('./commands'):
		if filename.endswith('.py'):
			bot.load_extension(f'commands.{filename[:-3]}')

online()
bot.run(TOKEN)