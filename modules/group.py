import discord
from discord.ext import commands
from discord.commands import SlashCommandGroup

class group(commands.Cog):

  def __init__(self, bot):
    self.bot = bot

  group_cmds = SlashCommandGroup("group", "The group!") # Создаём категорию (группу) команд с названием "group"

  @group_cmds.command() # Объявляем подкоманду для группы "group"
  async def testcmd( # Функция, которая вызывается при запуске подкомманды и которая имеет название этой функции (то есть в итоге у нас получится команда group testcmd)
    self,
    ctx: discord.ApplicationContext
  ):
    await ctx.respond(
        "Тест!"
    )

  test = group_cmds.create_subgroup( # Создаём подкатегорию (подгруппу) для категории "group"
      "test", "The test cmd!" #название подкатегории и её описание
  )

  @test.command(name="doubletest") # Объявляем новую команду для подкатегории "test" с названием "doubletest"
  async def test2(
    self,
    ctx: discord.ApplicationContext
  ):
    await ctx.respond(
        "Двойной тест!"
    )

def setup(bot):
  bot.add_cog(group(bot))
