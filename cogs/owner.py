from discord.ext import commands
from MySQL.connection import commiting
from MySQL.superuser import addSuperuser, delSuperuser

import time
import asyncio
import discord
import datetime


class Owner(commands.Cog):


    def __init__(self, bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_ready(self):
        global startTime
        startTime = time.time()
        print("Owner commands -> Ready")


    @commands.command(hidden=True)
    @commands.is_owner()
    async def shutdown(self, ctx):
        for cmds in self.bot.all_commands:
            cmd = self.bot.get_command(cmds)
            print(cmd)
            self.bot.remove_command(cmd)
        await ctx.send("The Bot is shutting down! :green_circle:")
        await asyncio.sleep(2)
        commiting()
        exit()


    @commands.command(hidden=True)
    @commands.is_owner()
    async def block(self, ctx):
        for cmds in self.bot.all_commands:
            print(cmds)
            cmd = self.bot.get_command(cmds)
            if str(cmd) == "unblock" or str(cmd) == "shutdown":
                pass
            else:
                cmd.update(enabled=False)
        await asyncio.sleep(2)
        commiting()
        await ctx.send("Disabled all commands :green_circle:")


    @commands.command(hidden=True)
    @commands.is_owner()
    async def unblock(self, ctx):
        for cmds in self.bot.all_commands:
            cmd = self.bot.get_command(cmds)
            cmd.update(enabled=True)
        await asyncio.sleep(2)
        commiting()
        await ctx.send("Enabled all commands :green_circle:")
    

    @commands.command(hidden=True)
    @commands.is_owner()
    async def uptime(self, ctx):
        uptime = str(datetime.timedelta(seconds=int(round(time.time()-startTime))))
        await ctx.send(f"Uptime: {uptime}")
        print("Uptime")
    
    
    @commands.command(hidden=True)
    @commands.is_owner()
    async def addsu(self, ctx, user: discord.User):
        addSuperuser(user.id)
        await ctx.send(f"Added Superuser {user.id}")
        print(f"Added Superuser {user.id}")


    @commands.command(hidden=True)
    @commands.is_owner()
    async def delsu(self, ctx, user: discord.User):
        delSuperuser(user)
        await ctx.send(f"Removed Superuser {user.id}")
        print(f"Removed Superuser {user}")


async def setup(bot):
    await bot.add_cog(Owner(bot))
