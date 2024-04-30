from discord.ext import commands
from discord.ext.commands import has_permissions
from MySQL.moderation import addModeration, removeModeration, checkModeration

import discord

class Admin(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Admin commands -> Ready")

    @commands.command(pass_context=True)
    @commands.cooldown(12, 60, commands.BucketType.guild)
    @has_permissions(administrator=True)
    async def addmod(self, ctx, user: discord.Member):
        if checkModeration(int(ctx.guild.id), int(user.id)):
            await ctx.send(f"{user}/{user.id} is already a server mod")
        else:
            addModeration(int(ctx.guild.id), int(user.id))
            await ctx.send(f"Added {user} to active server moderators :green_circle:")
    
    @commands.command(pass_context=True)
    @commands.cooldown(12, 60, commands.BucketType.guild)
    @has_permissions(administrator=True)
    async def delmod(self, ctx, user: discord.Member):
        if not checkModeration(int(ctx.guild.id), int(user.id)):
            await ctx.send(f"{user}/{user.id} is not a server mod")
        else:
            removeModeration(int(ctx.guild.id), int(user.id))
            await ctx.send(f"Removed {user} from active server moderators :green_circle:")


async def setup(bot):
    await bot.add_cog(Admin(bot))