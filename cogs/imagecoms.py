import discord
from discord.ext import commands
from PIL import Image
from io import BytesIO

class Img(commands.Cog):


    def __init__(self, client):
        self.client = client

    
    @commands.command()
    async def wanted(self, ctx, user: discord.Member = None):
        if user == None:
            user = ctx.author

        wanted = Image.open("wanted.png")
        asset = ctx.author.avatar_url_as(size = 128)
        data = BytesIO(await asset.read())
        pfp = Image.open(data)


def setup(client):
    client.add_cog(Img(client))