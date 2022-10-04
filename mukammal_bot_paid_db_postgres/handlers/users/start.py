import asyncpg
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from mukammal_bot_paid_db_postgres.keyboards.default.menuKeyboard import menu
from mukammal_bot_paid_db_postgres.loader import dp, db, bot
from mukammal_bot_paid_db_postgres.data.config import ADMINS


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    try:
        user = await db.add_user(telegram_id=message.from_user.id,
                                 full_name=message.from_user.full_name,
                                 username=message.from_user.username)
    except asyncpg.exceptions.UniqueViolationError:
        user = await db.select_user(telegram_id=message.from_user.id)

    await message.answer(f"Xush kelibsiz! \n{message.from_user.full_name.capitalize()} ", reply_markup=menu)

    # ADMINGA xabar beramiz
    count = await db.count_users()
    msg = f"{user[1]} bazaga qo'shildi.\nBazada {count} ta foydalanuvchi bor."
    await bot.send_message(chat_id=ADMINS[0], text=msg, reply_markup=menu)
    await bot.send_message(chat_id=-871587737, text=msg)



