from aiogram import types

from mukammal_bot_paid_db_postgres.loader import dp


@dp.message_handler(hashtags=['salom', 'qalesan'])
async def tags(msg: types.Message):
    await msg.answer('how are you?')

