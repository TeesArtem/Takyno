# !!! После main.py смотрите modules/hello.py в качестве примера обычной команды !!!
# !!! modules/ping.py - это практически то же самое, что и modules/hello.py !!!
# !!! Затем можете посмотреть modules/group.py в качестве примера группы команд !!!


#import os #--для реплита
import discord
from discord.ext import commands
import os

bot = discord.Bot() # Создаём нашего бота


# Подключаем все команды
for filename in os.listdir("modules/"): #проходимся по всем файлам в папке modules/
  if filename.endswith(".py"): #проверяем, что это файл python
    bot.load_extension(f"modules.{filename[:-3]}") #загружаем его в бота
    print(f"Загружен модуль {filename[:-3]}") #выводим в консоль, что модуль загружен


@bot.event
async def on_ready(): # Функция вызывается после запуска бота
  print(f"{bot.user} запущен")

#bot.run(os.environ['BOT_TOKEN']) #--для реплита
bot.run(os.environ['BOT_TOKEN']) # Запускаем бота (тут нужно указать токен)
