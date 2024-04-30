from discord.ext import commands
from discord import Color

import discord


class HelpCommands(commands.Cog):


    def __init__(self, bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_ready(self):
        print("Help commands -> Ready")


    @commands.command(pass_context=True)
    async def help(self, ctx):
        help_embed = discord.Embed(title=f"**HELP COMMAND** :small_orange_diamond: Version: {str(self.bot.ver)}", color=Color.red())
        help_embed.set_thumbnail(url=self.bot.user.avatar)
        help_embed.add_field(name=f'__{self.bot.command_prefix}profile [mention]__', value='Shows your profile', inline=False)
        help_embed.add_field(name=f'__{self.bot.command_prefix}eco__', value=':coin:', inline=False)
        help_embed.add_field(name=f'__{self.bot.command_prefix}mod__', value=':hammer_and_pick:', inline=False)
        help_embed.add_field(name=f'__{self.bot.command_prefix}roles__', value=':closed_lock_with_key:', inline=False)
        help_embed.add_field(name=f'__{self.bot.command_prefix}fun__', value=':new_moon_with_face:', inline=False)
        help_embed.add_field(name=f'__{self.bot.command_prefix}admin__', value=':gear:', inline=False)
        await ctx.send(embed=help_embed)


    @commands.command(pass_context=True)
    async def eco(self, ctx):
        help_embed = discord.Embed(title=f"**HELP COMMAND -> eco** :coin:", color=Color.gold())
        help_embed.set_thumbnail(url=self.bot.user.avatar)
        help_embed.add_field(name=f'__{self.bot.command_prefix}enter__', value='Enter the database !REQUIRED', inline=False)
        help_embed.add_field(name=f'__{self.bot.command_prefix}bal [mention]__', value='Get your current balance', inline=False)
        help_embed.add_field(name=f'__{self.bot.command_prefix}share (user) (ammount)__', value='Share your gold', inline=False)
        help_embed.add_field(name=f'__{self.bot.command_prefix}dice__', value='Roll the dice and win gold', inline=False)
        help_embed.add_field(name=f'__{self.bot.command_prefix}guess (1-100)__', value='Guess the number and win gold', inline=False)
        help_embed.add_field(name=f'__{self.bot.command_prefix}leaderboard [n]__', value='Get the global leaderboard', inline=False)
        await ctx.send(embed=help_embed)


    @commands.command(pass_context=True)
    async def mod(self, ctx):
        help_embed = discord.Embed(title=f"**HELP COMMAND -> mod** :hammer_and_pick:", color=Color.purple())
        help_embed.set_thumbnail(url=self.bot.user.avatar)
        help_embed.add_field(name=f'__{self.bot.command_prefix}ban (mention) [reason]__', value='Ban someone', inline=False)
        help_embed.add_field(name=f'__{self.bot.command_prefix}unban (userID))__', value='Unban someone', inline=False)
        help_embed.add_field(name=f'__{self.bot.command_prefix}kick (mention) [reason]__', value='Kick someone', inline=False)
        await ctx.send(embed=help_embed)


    @commands.command(pass_context=True)
    async def roles(self, ctx):
            help_embed = discord.Embed(title=f"**HELP COMMAND -> roles** :closed_lock_with_key:", color=Color.yellow())
            help_embed.set_thumbnail(url=self.bot.user.avatar)
            help_embed.add_field(name=f'__{self.bot.command_prefix}addrole (mention) (role)__', value='Add a role to someone', inline=False)
            help_embed.add_field(name=f'__{self.bot.command_prefix}removerole (mention) (role)__', value='Remove someones role', inline=False)
            await ctx.send(embed=help_embed)


    @commands.command(pass_context=True)
    async def fun(self, ctx):
        help_embed = discord.Embed(title=f"**HELP COMMAND -> fun** :new_moon_with_face:", color=Color.orange())
        help_embed.set_thumbnail(url=self.bot.user.avatar)
        help_embed.add_field(name=f'__{self.bot.command_prefix}dice__', value='Roll the dice and win some gold', inline=False)
        help_embed.add_field(name=f'__{self.bot.command_prefix}guess 1-100__', value='Guess the number and win gold', inline=False)
        await ctx.send(embed=help_embed)

    @commands.command(pass_context=True)
    async def admin(self, ctx):
        help_embed = discord.Embed(title=f"**HELP COMMAND -> admin** :gear:", color=Color.orange())
        help_embed.set_thumbnail(url=self.bot.user.avatar)
        help_embed.add_field(name=f'__{self.bot.command_prefix}addmod__', value='Add a new server moderator', inline=False)
        help_embed.add_field(name=f'__{self.bot.command_prefix}delmod__', value='Remove a server moderation', inline=False)
        await ctx.send(embed=help_embed)


async def setup(bot):
    await bot.add_cog(HelpCommands(bot))