from discord.ext import commands
from MySQL.superuser import checkSuperuser
from MySQL.gold import addGoldToUser, deductGoldFromUser, addUserToGoldDB

import discord


class Superuser(commands.Cog):


    def __init__(self, bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_ready(self):
        print("Superuser commands -> Ready")


    @commands.command(pass_context=True)
    async def deductgold(self, ctx, user: discord.User, ammount):
        if checkSuperuser(ctx.author.id):
            await ctx.message.delete()
            if deductGoldFromUser(int(user.id), int(ammount)) == 0:
                await ctx.send(f"Deducted *{ammount}* from {user.mention} :green_circle:")
                print(f">> {ctx.author.name}/{ctx.author.id} deducted {ammount} from {user.id}")
            else:
                ctx.send(f"ERROR! Users balance below zero OR not in database! Type __{self.bot.command_prefix}enter__ :red_circle:")


    @commands.command(hidden=True)
    async def addgold(self, ctx, user: discord.User, ammount):
        if checkSuperuser(int(ctx.author.id)):
            await ctx.message.delete()
            if addGoldToUser(user.id, int(ammount)) == 0:
                await ctx.send(f"Added *{ammount}* to {user.mention} :green_circle:")
                print(f">> {ctx.author.name}/{ctx.author.id} added {ammount} to {user.id}")
            else:
                await ctx.send(f"ERROR! Users balance exceeded maximum OR not in database! Type __{self.bot.command_prefix}enter__ :red_circle:")


    @commands.command(pass_context=True)
    async def force(self, ctx, user: discord.User, goldAmmount=200):
        if checkSuperuser(ctx.author.id):
            if addUserToGoldDB(user.id, goldAmmount) == 0:
                await ctx.send(f"{user.id}/{user.mention} was added to the __Gold database__ :green_circle:")
            else:
                await ctx.send(f"{user.id}/{user.mention} is already in the gold database :red_circle:")



async def setup(bot):
    await bot.add_cog(Superuser(bot))
