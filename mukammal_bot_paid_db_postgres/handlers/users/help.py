from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from mukammal_bot_paid_db_postgres.loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = ("Buyruqlar: ",
            "/start - Botni ishga tushirish",
            "/help - Yordam")
    
    await message.answer("\n".join(text))