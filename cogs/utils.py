import discord
from discord.ext import commands


class Util(commands.Cog):
 

    def __init__(self, client):
        self.client = client
    
    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'📶  {round(self.client.latency*1000)}ms')

    @commands.command()
    async def help(self, ctx):
         embed = discord.Embed(title = "Commands List", colour = discord.Color.lighter_gray(), timestamp=ctx.message.created_at)
         embed.set_footer(text=f'Requested by {ctx.author}', icon_url=ctx.author.avatar_url)
         embed.add_field(name="Moderation 🔒", value=".clear [amount]\tor .c\n.mute @mention\n.unmute @mention\n.kick @mention\n.ban @mention\n.unban [name#tag]\n - ")
         #embed.add_field(name="_", value="_", inline=False)
         embed.add_field(name="Utility ⚙️", value='.ping\n.poll [text]\n.info @mention\n.id @mention\n.membercount\n - ')
         embed.add_field(name="Fun 🎉",value='.bong\tpurge bongs\n.say [text]\n.quote [text]\n.ask [text]\n.who\n.coin\n.enter\n.exit (to exit the chats in style)\n.wtc (watch the 9/11 incident)\n.hoe\n.nyan\n.ok\n.cry\n.pankaj\n.bruh\n',inline=False)
         embed.set_footer(text="This bot is still under development 😤")
         await ctx.send(embed=embed)

    #@commands.command()
    #async def usercount(self, ctx):
    #    await ctx.send(len(ctx.guild.members))

    @commands.command()
    async def membercount(self,ctx):
        await ctx.send(ctx.guild.member_count)


def setup(client):
    client.add_cog(Util(client))