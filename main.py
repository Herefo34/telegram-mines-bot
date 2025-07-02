from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

API_TOKEN = 'YOUR_BOT_TOKEN_HERE'  # Այստեղ դիր քո բոտի token-ը

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start_game(message: types.Message):
    await message.answer("Բարև, բարի գալուստ քո Մայնզ խաղը 💣։ Սեղմիր մի բջիջ սկսելու համար։")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
