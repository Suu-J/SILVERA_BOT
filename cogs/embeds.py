import discord
from discord.ext import commands
import asyncio
from asyncio import sleep

class Embeds(commands.Cog):


    def __init__(self, client):
        self.client = client

    @commands.command()
    async def id(self, ctx, member : discord.Member):
        embed = discord.Embed(title = member.name, description = member.mention, color = discord.Color.green())
        embed.add_field(name = 'ID', value = member.id, inline = True)
        embed.set_thumbnail(url = member.avatar_url)
        embed.set_footer(icon_url = ctx.author.avatar_url,text=f"Requested by {ctx.author.name}")
        await ctx.send(embed = embed)

    @commands.command()
    async def info(self, ctx, member : discord.Member = None):

        member = ctx.author if not member else member
        roles = [role for role in member.roles]

        embed = discord.Embed(colour=member.color, timestamp=ctx.message.created_at)
       
        embed.set_author(name = f'User Info - {member}')
        embed.set_thumbnail(url=member.avatar_url)
        embed.set_footer(text=f'Requested by {ctx.author}', icon_url=ctx.author.avatar_url)

        embed.add_field(name='ID', value=member.id)
        embed.add_field(name="Nickname:", value=member.display_name)

        embed.add_field(name='Creation Date:', value=member.created_at.strftime("%a, %#d %B %Y, %I : %M %p UTC"))
        embed.add_field(name='Joined server:', value=member.joined_at.strftime("%a, %#d %B %Y, %I : %M %p UTC"))

        embed.add_field(name=f"Roles ({len(roles)})", value=" ".join([role.mention for role in roles]))
        embed.add_field(name="Top role:", value = member.top_role.mention)

        embed.add_field(name='Bot?', value = member.bot)

        await ctx.send(embed=embed)



    '''@commands.command()
    async def testing(self, ctx):
        message1 = discord.Embed(title='OOGA')
        message2 = discord.Embed(title='BOOGA')
        message3 = discord.Embed(title='NIGGA')
        message4 = discord.Embed(title='NIGGAx69')
        msg = await ctx.send(embed=message1)
        await msg.add_reaction("❌")
        await msg.add_reaction("➡️")
        await asyncio.sleep(4)
        await msg.edit(embed=message2)
        await msg.add_reaction("❌")
        await msg.add_reaction("⬅️")
        await msg.add_reaction("➡️")     
        await asyncio.sleep(4)
        await msg.edit(embed=message3)
        await msg.add_reaction("❌")
        await msg.add_reaction("⬅️")
        await msg.add_reaction("➡️")
        await asyncio.sleep(4)
        await msg.edit(embed=message3)
        await msg.add_reaction("❌")
        await msg.add_reaction("⬅️")
        await asyncio.sleep(4)
        await msg.edit(embed=message4)'''
    
    
    @commands.command()
    async def test(self,ctx):
        message1 = discord.Embed(title='OOGA')
        msg = await ctx.send(embed=message1)
        message2 = discord.Embed(title='BOOGA')
        await msg.add_reaction("❌")

        def check(reaction, user):
            return user == ctx.author and str(reaction.emoji) == '❌'

        try:
            reaction, user = await self.client.wait_for('reaction_add', timeout=60.0, check=check)
        except asyncio.TimeoutError:
            await ctx.send("Fail")
        else:
            await msg.edit(embed=message2)


def setup(client):
    client.add_cog(Embeds(client))