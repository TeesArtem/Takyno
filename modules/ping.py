import discord
from discord.ext import commands

class ping(commands.Cog):

  def __init__(self, bot):
      self.bot = bot

  @commands.slash_command(
    name="ping",
    description="Показывает пинг бота"
  )
  async def ping_command(
    self,
    ctx: discord.ApplicationContext
  ):
    await ctx.respond(
        f"Понг! {round(self.bot.latency * 1000)}ms"
    )

def setup(bot):
  bot.add_cog(ping(bot))
