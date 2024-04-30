from discord.ext import commands
from MySQL.gold import *
from easy_pil import Editor, Font, load_image_async
from MySQL.moderation import checkModeration
from discord import Color

import discord

class Economics(commands.Cog):


    def __init__(self, bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_ready(self):
        print("Economics commands -> Ready")
    

    @commands.Cog.listener()
    async def on_message(self, message):
        addGoldToUser(int(message.author.id), 3)


    @commands.command(pass_context=True)
    @commands.cooldown(2, 5, commands.BucketType.user)
    async def bal(self, ctx, user: discord.User=None):
        if user is None:
            user = ctx.author
        gold = checkGoldForUser(user.id)
        if gold != "ERROR":
            await ctx.send(f"{user.mention} current balance is *{gold}*")
        else:
            await ctx.send(f"{user.mention} ERROR: User not in database. Type __{self.bot.command_prefix}enter__ :red_circle:")


    @commands.command(pass_context=True)
    @commands.cooldown(2, 7, commands.BucketType.user)
    async def profile(self, ctx, user: discord.User=None):
        if user is None:
            user = ctx.author
        PROFILE_BACKGROUND = Editor("profile_background.jpg")#.resize((900, 300))
        avatar = await load_image_async(ctx.author.display_avatar.url)
        circle_avatar = Editor(avatar).resize((150, 150)).circle_image()
        PROFILE_BACKGROUND.paste(circle_avatar, (75, 75))
        big_text = Font.poppins(size=40, variant="bold")
        PROFILE_BACKGROUND.text((550, 134), f"{user.name} | Gold: {checkGoldForUser(int(user.id))}", color="black", font=big_text, align="center")
        PROFILE_BACKGROUND.text((710, 50), f"Moderator: {checkModeration(int(ctx.guild.id), int(user.id))}", color="blue", font=big_text, align="center")
        file = discord.File(fp=PROFILE_BACKGROUND.image_bytes, filename=f"{user.id}.png")
        PROFILE_BACKGROUND.rounded_corners
        await ctx.send(file=file)
        file.reset()
        file.close()


    @commands.command(pass_context=True)
    @commands.cooldown(2, 5, commands.BucketType.user)
    async def share(self, ctx, user: discord.User, ammount):
        if deductGoldFromUser(int(ctx.author.id), int(ammount)) == 0:
            if addGoldToUser(int(user.id), int(ammount)) == 0:
                await ctx.send(f"{ctx.author.mention} you shared {ammount} with {user.name}/{user.id} :green_circle:")
            else:
                addGoldToUser(int(ctx.author.id), int(ammount))
                await ctx.send(f"{ctx.author.mention} looks like the other users balance exceeded the maximum :red_circle:")
        else:
            await ctx.send(f"{ctx.author.mention} you dont have enough gold to tranfer :red_circle:")


    @commands.command(pass_context=True)
    async def enter(self, ctx):
        if addUserToGoldDB(int(ctx.author.id), 200) == 0:
            await ctx.send(f"{ctx.author.mention} you entered the __Gold database__ :green_circle:")
        else:
            await ctx.send(f"{ctx.author.mention} you are already in the gold database :red_circle:")



    @commands.command(name="leaderboard", pass_context=True)
    @commands.cooldown(2, 6, commands.BucketType.user)
    async def getLeaderboard(self, ctx, limit = None):
        if limit is None:
            limit = 20
        if int(limit) > 20:
            await ctx.send("Setting limit to 20")
            limit = 20
        leaderboard_embed = discord.Embed(title=f"GLOBAL LEADERBOARD - Top {limit}", color=Color.dark_gold())
        counter = 1
        for i in getGlobalLeaderboard(int(limit)):
            for j in i:
                u = f"<@{str(i[0])}>"
            special = ":moneybag:"
            if counter == 1:
                special = ":first_place:"
            if counter == 2:
                special = ":second_place:"
            if counter == 3:
                special = ":third_place:"
            leaderboard_embed.add_field(name=f"{counter} {special}", value=f"{u} -- {str(i[1])} Gold", inline=False)
            counter += 1
        await ctx.send(embed=leaderboard_embed)


async def setup(bot):
    await bot.add_cog(Economics(bot))
