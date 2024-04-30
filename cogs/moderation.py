from discord.ext import commands
from MySQL.moderation import checkModeration, getAllModerations
from discord import Color

import discord


class Moderation(commands.Cog):

    def __init__(self, bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_ready(self):
        print("Moderator commands -> Ready")


    @commands.command(pass_context=True)
    @commands.cooldown(12, 60, commands.BucketType.user)
    async def ban(self, ctx, user: discord.Member, *args):
        if ctx.author != user:
            if checkModeration(int(ctx.guild.id), int(user.id)):
                await ctx.send("You cant ban other Bot Moderators :red_circle:")
            elif checkModeration(int(ctx.guild.id), int(ctx.author.id)):
                await ctx.message.delete()
                reasonBan = ' '.join(args)
                await user.ban(reason=reasonBan)
                await ctx.send(f'{user.name}#{user.discriminator} was banned :green_circle:')
                await user.send(f'You was banned from {ctx.guild.name}. Reason: {reasonBan}.')
                print(f"{ctx.author}/{ctx.author.id} banned user: {user}/{user.id}")
            else:
                await ctx.send(f"{ctx.author} missing permissions! *Bot Moderator*")
        else:
            await ctx.send(f"{ctx.author.mention} you cant ban yourself! *Bot Moderator*")
    

    @commands.command(pass_context=True)
    @commands.cooldown(12, 60, commands.BucketType.user)
    async def unban(self, ctx, user: discord.Member):
        if checkModeration(int(ctx.guild.id), int(ctx.author.id)):
            await ctx.message.delete()
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.name}#{user.discriminator} from the guild :green_circle:')
            print(f"{ctx.author}/{ctx.author.id} unbanned user: {user}/{user.id}")
        else:
            await ctx.send(f"{ctx.author} missing permissions!")
    
    
    @commands.command(pass_context=True)
    @commands.cooldown(12, 60, commands.BucketType.user)
    async def kick(self, ctx, user: discord.Member, *args):
        if checkModeration(int(ctx.guild.id), int(user.id)):
            await ctx.send("You cant kick other Bot Moderators :red_circle;")
        elif checkModeration(int(ctx.guild.id), int(ctx.author.id)):
            await ctx.message.delete()
            reasonKick = ' '.join(args)
            await user.kick(reason=reasonKick)
            await ctx.send(f'{user.name}#{user.discriminator} was kicked :green_circle:')
            await user.send(f'You was kicked from {ctx.guild.name}. Reason: {reasonKick}.')
            print(f"{ctx.author}/{ctx.author.id} kicked user: {user}/{user.id}")
        else:
            await ctx.send(f"{ctx.author} missing permissions! *Bot Moderator*")


    @commands.command(pass_context=True)
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def listmods(self, ctx):
        if checkModeration(int(ctx.guild.id), int(ctx.author.id)):
            mods_embed = discord.Embed(title=f"ACTIVE SERVER MODERATIONS -> {ctx.guild.name}", color=Color.orange())
            mods_embed.set_thumbnail(url=ctx.guild.icon)
            all_mods = []
            for mods in getAllModerations(int(ctx.guild.id)):
                for mods1 in mods:
                    all_mods.append(f"<@{mods1}>")
            mods_embed.add_field(name=f"", value="\n".join(all_mods), inline=True)
            await ctx.send(embed=mods_embed)
        else:
            await ctx.send("Missing permissions! *Bot Moderator*")


async def setup(bot):
    await bot.add_cog(Moderation(bot))