import asyncio

from aiogram import types

from mukammal_bot_paid_db_postgres.data.config import ADMINS
from mukammal_bot_paid_db_postgres.loader import dp, db, bot


@dp.message_handler(text="/rek", user_id=ADMINS)
async def send_ad_to_all(message: types.Message):
    users = await db.select_all_users()
    for user in users:
        print(user[3])
        user_id = user[3]
        await bot.send_message(chat_id=user_id, text="@status_py_developer adminga murojat qiling!")
        # await asyncio.sleep(0.05)
