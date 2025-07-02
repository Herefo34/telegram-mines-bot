from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

API_TOKEN = 'YOUR_BOT_TOKEN_HERE'  # 🔁 Այստեղ տեղադրիր քո բոտի token-ը

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start_game(message: types.Message):
    await message.answer("Բարև, բարի գալուստ խաղ!")

    keyboard = types.InlineKeyboardMarkup(row_width=5)
    buttons = []

    for i in range(1, 61):  # 5x12 = 60 բջիջ
        buttons.append(types.InlineKeyboardButton(text=str(i), callback_data=f"cell_{i}"))

    keyboard.add(*buttons)
    await message.answer("Ընտրիր բջիջ 👇", reply_markup=keyboard)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
