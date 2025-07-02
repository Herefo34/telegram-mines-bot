import random
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

API_TOKEN = '7386380333:AAE0giVzCDeH6Hcouf5AIPY9wrhw0stOzWA'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'game'])
async def start_game(message: types.Message):
    keyboard = types.InlineKeyboardMarkup(row_width=5)
    buttons = []

    for i in range(1, 61):  # 5x12 = 60 բջիջ
        buttons.append(types.InlineKeyboardButton(text=str(i), callback_data=f'cell_{i}'))

    keyboard.add(*buttons)
    await message.answer("Բարև, ընտրիր բջիջ 🎯", reply_markup=keyboard)

@dp.callback_query_handler(lambda c: c.data and c.data.startswith('cell_'))
async def handle_cell_click(callback_query: types.CallbackQuery):
    user_choice = int(callback_query.data.split('_')[1])

    # 💣 Պայթյունի հավանականություն (փոխիր ըստ ցանկության)
    bomb_probability = 0.3
    is_bomb = random.random() < bomb_probability

    if is_bomb:
        await callback_query.message.edit_text(f"💥 Բջիջ {user_choice} — Պայթեցիր 😢")
    else:
        await callback_query.message.edit_text(f"✅ Բջիջ {user_choice} — Ամեն ինչ OK է, կարող ես շարունակել!")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
