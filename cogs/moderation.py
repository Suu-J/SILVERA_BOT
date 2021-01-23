import discord
from discord.ext import commands

class Mod(commands.Cog):


    def __init__(self, client):
        self.client = client
    
    #@commands.Cog.listener()#decorator to create event within a cog
    #async def on_ready(self):#self must be passed, for every function inside a class
    #    print('All systems operational!')
    #    await client.change_presence()

    

    @commands.command(aliases = ['purge','cl','clean','c'])
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount : int):
        await ctx.channel.purge(limit = amount +1)

   
    #Errors
    @clear.error
    async def clear_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Please specify an amount of messages to delete.')

    
    @commands.command(aliases = ['m'])
    @commands.has_permissions(kick_members=True)
    async def mute(self,ctx, member : discord.Member):
        muted_role = ctx.guild.get_role(545262967655235595)
        await member.add_roles(muted_role)
        await ctx.send(member.mention+" has been muted")
    
    @commands.command(aliases = ['um'])
    @commands.has_permissions(kick_members=True)
    async def unmute(self,ctx, member : discord.Member):
        muted_role = ctx.guild.get_role(545262967655235595)
        await member.remove_roles(muted_role)
        await ctx.send(member.mention+" has been unmuted")

    
    @commands.command(aliases = ['yeet'])
    @commands.has_permissions(kick_members=True)
    async def kick(self,ctx, member : discord.Member,*,reason = "No reason provided"):
        await member.send("You have been kicked from the server\nReason = "+reason)
        await ctx.send(f'{member} has been kicked from the server\nReason = '+reason)
        await member.kick(reason=reason)


    @commands.command(aliases = ['dump'])
    @commands.has_permissions(ban_members=True)
    async def ban(self,ctx, member : discord.Member,*,reason = "No reason provided"):
        await member.send("You have been banned from the server\nReason = "+reason)
        await ctx.send(f'{member} has been banned from the server\nReason = '+reason)
        await member.ban(reason=reason)

    
    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def unban(self,ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name,member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user

            if(user.name, user.discriminator) == (member_name,member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f'Unbanned {user.name}#{user.discriminator}')
                return 
        
        await ctx.send(member+' was not found')




def setup(client):
    client.add_cog(Mod(client))