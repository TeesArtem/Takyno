import discord
from discord.ext import commands
from discord.ui import Button, View

class button(commands.Cog):

  def __init__(self, bot):
    self.bot = bot

  @commands.slash_command(
    name="butt_on",
    description="Тест кнопки"
  )
  async def test(self, ctx):

      async def button_callback(interaction):
        await interaction.channel.send(content='🎂 <--- ТОРТИК!!!', view=None)

      button = Button(custom_id='butt_on', label='я кнопка, нажми на меня ^^', style=discord.ButtonStyle.green)
      button.callback = button_callback

      await ctx.respond('Тут такая прикольная кнопочка соблазняющая внизу, нажми ка на неё', view=View(button))

def setup(bot):
  bot.add_cog(button(bot))
