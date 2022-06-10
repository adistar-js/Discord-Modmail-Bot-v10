
import datetime , json
from datetime import datetime
import discord
import asyncio
from discord.ext import commands 
file = open('config.json','r')
data = file.read()
config = json.loads(data)

PREFIX = config['PREFIX']

class mods(commands.Cog):
    def __init__(self,bot):        
        self.bot = bot
        
    
    @commands.Cog.listener()
    async def on_message(self,message):
        try:
            if f'{PREFIX}close' in message.content:
                pass
            else:
                if str(message.channel.type) == "private":
                    return
                else:
                    if message.author == self.bot.user:
                        return
                    else:
                        user = await message.guild.fetch_member(int(message.channel.name))
                        emb = discord.Embed(
                            description = message.content,
                            timestamp = datetime.utcnow(),
                            colour = discord.Colour.green()                   
                        )
                        emb.set_author(name = f'[Support] {message.author}',icon_url = message.author.avatar_url)
                        try:
                            await message.add_reaction('✅')                         
                            await user.send(embed = emb)
                        except:
                            await message.channel.send('User is not in server!')
        except Exception as e:
            print(e)
            pass
                    
                    
    @commands.command()
    async def close(self,ctx):
        user = await ctx.guild.fetch_member(int(ctx.channel.name))
        emd = discord.Embed(title = f'Ticket has beed closed by {ctx.author}!',
                            description=f'• Thank you to contacting us.\n• If you need more help or assistance simply message me.',
                            colour = discord.Colour.blue())
        emd.set_footer(text='Made by Adistar💘')
        bb = await user.send(user.mention,embed = emd)
        await bb.add_reaction('💛')
        await ctx.reply('Ticket has been closed! `[Channel will be deleted after few seconds]`')
        await asyncio.sleep(8)
        await ctx.channel.delete()
                    
  

def setup(bot):	
	bot.add_cog(mods(bot))



