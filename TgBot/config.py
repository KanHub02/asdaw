from aiogram import Bot, Dispatcher
from decouple import

TOKEN = config("TOKEN")
bot = Bot(TOKEN)
dp = Dispatcher(bot=bot)