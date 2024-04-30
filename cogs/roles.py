from discord.ext import commands
from MySQL.moderation import checkModeration
from discord.ext.commands import has_permissions

import discord


class Roles(commands.Cog):


    def __init__(self, bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_ready(self):
        print("Roles commands -> Ready")


    @commands.command(pass_context=True)
    @has_permissions(administrator=True)
    async def addrole(self, ctx, user: discord.Member, role: discord.Role):
        if checkModeration(int(ctx.guild.id), int(ctx.author.id)):
            await ctx.message.delete()
            await user.add_roles(role)
            await ctx.send(f'Added {user.mention} to {role} :green_circle:')
            print(f"{ctx.author}/{ctx.author.id} added role: {role}/{role.id} --> to user: {user}/{user.id}")
        else:
            await ctx.send(f"{ctx.author} missing permissions!")
        


    @commands.command(pass_context=True)
    @has_permissions(administrator=True)
    async def removerole(self, ctx, user: discord.Member, role: discord.Role):
        if checkModeration(int(ctx.guild.id), int(ctx.author.id)):
            await ctx.message.delete()
            await user.remove_roles(role)
            await ctx.send(f'Removed {user.mention} from {role} :green_circle:')
        else:
            await ctx.send(f"{ctx.author} missing permissions!")


async def setup(bot):
    await bot.add_cog(Roles(bot))
