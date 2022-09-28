from aiogram import types

from mukammal_bot_paid_db_postgres.loader import dp


# Echo bot
@dp.message_handler(state=None)
async def bot_echo(message: types.Message):
    await message.answer(message.text)
