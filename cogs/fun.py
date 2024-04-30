from discord.ext import commands
from MySQL.gold import *
from easy_pil import Editor, Font, load_image_async
from MySQL.moderation import checkModeration
from discord import Color

import discord
import random


class Fun(commands.Cog):


    def __init__(self, bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_ready(self):
        print("Fun commands -> Ready")
        

    @commands.command(pass_context=True)
    @commands.cooldown(2, 6, commands.BucketType.user)
    async def dice(self, ctx):
        r = random.randint(1, 6)
        addGoldToUser(ctx.author.id, r*5)
        await ctx.send(f"{ctx.author.mention} you rolled a {r} and won {r} x 5 = {r*5} Gold!")


    @commands.command(pass_context=True)
    @commands.cooldown(5, 20, commands.BucketType.user)
    async def guess(self, ctx, num):
        rnum = random.randint(1, 101)
        if int(num) == rnum:
            addGoldToUser(int(ctx.author.id), 2000)
            await ctx.send(f"You won 2000 Gold!")
        else:
            await ctx.send(f"No luck. Maybe next time?! Number was {rnum}. Possible win: 2000")


async def setup(bot):
    await bot.add_cog(Fun(bot))
