import discord , json , asyncio
from datetime import datetime
from discord.ext import commands
file = open('config.json','r')
data = file.read()
config = json.loads(data)
GUILD = config['GUILD_ID']
STAFF = config['STAFF_ROLE']
CAT = config['PRIVATE_CATEGORY_NAME']


class FromUser(commands.Cog):
    def __init__(self,bot):        
        self.bot = bot
        
      
    @commands.Cog.listener()
    async def on_message(self,message):
        if str(message.channel.type) == 'private':
            if message.author == self.bot.user:
                return
            else:
                guild = self.bot.get_guild(GUILD)
                channels =await guild.fetch_channels()
                channel = discord.utils.get(channels,name = str(message.author.id))
                
                if channel is None:
                    category = discord.utils.get(guild.categories,name = CAT)
                    channel = await guild.create_text_channel((message.author.id),category = category)
                    await message.add_reaction('✅')
                    p = discord.Embed(description = 'Thread has been created sucessfully.\nSupport team will be reach you as soon as possible!',
                                      timestamp = datetime.utcnow(),
                                      colour = discord.Color.red())
                    p.set_author(name = f'Hello{message.author}',icon_url=message.author.avatar_url)
                    await message.author.send(message.author.mention,embed = p)
                    em = discord.Embed(
                        description = message.content,
                        timestamp = datetime.utcnow(),
                        colour = discord.Colour.red()                   
                    )
                    em.set_author(name = f'{message.author}Created a ticket!',icon_url=message.author.avatar_url)
                    await channel.send(F'[ {STAFF} ]',embed = em)                               
                else:   
                    await message.add_reaction("✅")                
                    em = discord.Embed(
                        description = message.content,
                        timestamp = datetime.utcnow(),
                        colour = discord.Colour.red()                
                    )
                    em.set_author(name=f"From {message.author}",icon_url = message.author.avatar_url)
                    await channel.send(embed = em)
def setup(bot):	
	bot.add_cog(FromUser(bot))


