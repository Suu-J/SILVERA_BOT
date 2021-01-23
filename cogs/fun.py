import discord
import random
import asyncio
from discord.ext import commands
from asyncio import sleep

class Funstuff(commands.Cog):


    def __init__(self, client):
        self.client = client


    @commands.command(aliases=['vote'])
    async def poll(self, ctx,*,msg):
        channel = ctx.channel
        text=msg

        embed = discord.Embed(title = "POLL TIME!", description = text, color = discord.Color.green())
        embed.set_footer(text="👍 Yes - 👎 No - ⭕ Neutral")
        message_ = await channel.send(embed=embed)
        await message_.add_reaction("👍")
        await message_.add_reaction("👎")
        await message_.add_reaction("⭕")
        await ctx.message.delete()


    @commands.command(aliases=['s'])
    async def say(self, ctx, *,msg):
        await ctx.message.delete()
        await ctx.send(msg)

    @commands.command(aliases=['q'])
    async def quote(self, ctx, *,msg):
        await ctx.message.delete()
        embed = discord.Embed(title = msg, colour = discord.Color.lighter_gray())
        embed.set_footer(text=f'Quote by {ctx.author}', icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

    @commands.command(aliases = ['8ball'])
    async def ask(self, ctx,*, question):
        responses = ["https://media.giphy.com/media/3o7abKhOpu0NwenH3O/giphy.gif", 
                     "I asked Prax, he said Yes",
                     "Why are you even asking? Obviously!!",
                     "Even a kid would know that's a yes!",
                     "You can trust yourself here",
                     "Hell yeah!",
                     "That's right",
                     "yes yes yes yes yes yes yes yes yes",
                     "Silvera says yes",
                     "Certainly",
                     "I don't wanna answer",
                     "I won't tell you",
                     "Concentrate and ask again",
                     "I don't like your tone 😠",
                     "Beep Boop Bop Beep 🤖",
                     "Uh sorry, I wasn't listening",
                     "Aw hell nawww",
                     "Would you really rely on a bot?",
                     "Nah I don't think so",
                     "Very doubtful",
                     "I asked Prax, he said No",
                     "https://media.giphy.com/media/lgcUUCXgC8mEo/giphy.gif"]
        await ctx.send(random.choice(responses))
   

    @commands.command()
    async def who(self, ctx):
        response =  ["https://tenor.com/bf7e2.gif",
                     "https://tenor.com/bme1o.gif",
                     "https://tenor.com/bgLFB.gif",
                     "https://tenor.com/bpbcM.gif",
                     "https://tenor.com/bkBUx.gif",
                     "https://tenor.com/boUYX.gif",
                     "https://tenor.com/bn6VE.gif",
                     "https://tenor.com/bjTHD.gif",
                     "https://tenor.com/TiMO.gif",
                     "https://tenor.com/bkuQR.gif",
                     "https://tenor.com/bfrtP.gif"]
        await ctx.send(random.choice(response))

    
    @commands.command(aliases=['coinflip'])
    async def coin(self, ctx):
        side = ['Heads','Tails']

        await ctx.send(random.choice(side))


    @commands.command()
    async def exit(self,ctx):
        message = await ctx.send("🚪                🚶")
        await asyncio.sleep(1)
        await message.edit(content="🚪           🏃")    
        await asyncio.sleep(1)
        await message.edit(content = "🚪        🏃💨")
        await asyncio.sleep(1)
        await message.edit(content = "🚪       🏃💨")
        await asyncio.sleep(1)
        await message.edit(content = "🚪     🏃💨")
        await asyncio.sleep(1)
        await message.edit(content = "🚪   🏃💨")
        await asyncio.sleep(1)
        await message.edit(content = "🚪🚶")
        await asyncio.sleep(1)
        await message.edit(content = "🚪")
        await asyncio.sleep(1)
        await message.edit(content = "🆗")
        await asyncio.sleep(1)
        await message.edit(content = "🆒")
        await asyncio.sleep(1)
        await message.edit(content = "🇧 🇾 🇪")


    @commands.command()
    async def wtc(self,ctx):
        message = await ctx.send("9/11 -  A DOCUMENTARY")
        await asyncio.sleep(1)
        await message.edit(content="🛫")    
        await asyncio.sleep(1)
        await message.edit(content = "✈️")
        await asyncio.sleep(1)
        await message.edit(content = "✈️                🏢")
        await asyncio.sleep(1)
        await message.edit(content = "✈️            🏢")
        await asyncio.sleep(1)
        await message.edit(content = "✈️         🏢")
        await asyncio.sleep(1)
        await message.edit(content = "✈️      🏢")
        await asyncio.sleep(1)
        await message.edit(content = "✈️    🏢")
        await asyncio.sleep(1)
        await message.edit(content = "✈️🧨🏢")
        await asyncio.sleep(1)
        await message.edit(content = "🎆🎆🎆")
        await asyncio.sleep(1)
        await message.edit(content = "💥💥💥")
        await asyncio.sleep(1)
        await message.edit(content = "🔥🔥🔥")
        await asyncio.sleep(1)
        await message.edit(content = "9/11 WAS AN INSIDE JOB")


    @commands.command()
    async def nyan(self, ctx):
        await ctx.send("https://cdn.discordapp.com/attachments/545239605012725779/761792892741484564/NyanNiggachan.gif")
      

    @commands.command()
    async def ok(self, ctx):
            await ctx.send("https://cdn.discordapp.com/attachments/633399054864351252/761951477060599808/images_-_2020-10-03T193206.811.jpeg")        

    @commands.command()
    async def cry(self, ctx):
            await ctx.send("https://cdn.discordapp.com/attachments/732466229574369291/763096104660107280/image0.jpg")


    @commands.command()
    async def bruh(self, ctx):
        response =  ["https://tenor.com/ba7RL.gif",
                     "https://tenor.com/0xSA.gif",
                     "https://tenor.com/Hdun.gif",
                     "https://tenor.com/2mtQ.gif",
                     "https://tenor.com/beOnD.gif",
                     "https://tenor.com/bmeZq.gif",
                     "https://tenor.com/txPN.gif",
                     "https://tenor.com/wApy.gif"]
        await ctx.send(random.choice(response))

    @commands.command()
    async def enter(self, ctx):
        await ctx.send("https://tenor.com/GbZv.gif")

def setup(client):
    client.add_cog(Funstuff(client))