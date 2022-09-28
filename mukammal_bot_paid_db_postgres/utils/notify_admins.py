import logging

from aiogram import Dispatcher

from mukammal_bot_paid_db_postgres.data.config import ADMINS


async def on_startup_notify(dp: Dispatcher):
    for admin in ADMINS:
        try:
            await dp.bot.send_message(admin, "bot is started")

        except Exception as err:
            logging.exception(err)
