import discord
from discord.ext import commands

class ping(commands.Cog):

  def __init__(self, bot):
      self.bot = bot

  @commands.slash_command(name="ping")
  async def ping_command(
    self,
    ctx: discord.ApplicationContext
  ):
    await ctx.respond(
        f"Pong! {round(self.bot.latency * 1000)}ms"
    )

def setup(bot):
  bot.add_cog(ping(bot))
