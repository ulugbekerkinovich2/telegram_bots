from aiogram import types

from mukammal_bot_paid_db_postgres.loader import dp


@dp.message_handler(commands='change_photo', is_chat_admin=True)
async def chat_admin_example(msg: types.Message):
    await msg.answer('rasm almashitramizmi')
