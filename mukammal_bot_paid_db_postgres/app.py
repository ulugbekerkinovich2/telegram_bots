from aiogram import executor

from mukammal_bot_paid_db_postgres.loader import dp, db
import middlewares, filters, handlers
from mukammal_bot_paid_db_postgres.utils.notify_admins import on_startup_notify
from mukammal_bot_paid_db_postgres.utils.set_bot_commands import set_default_commands


async def on_startup(dispatcher):
    await db.create()
    # await db.drop_users()
    await db.create_table_users()

    await db.create_table_anketa()

    await db.create_table_elon_shogird()

    await db.create_table_elon_sherik()

    await db.create_table_elon_xodim()

    await db.create_table_elon_Ish_joyi_kerak()

    await db.create_table_elon_ustoz_kerak()

    # Birlamchi komandalar (/star va /help)
    await set_default_commands(dispatcher)

    # Bot ishga tushgani haqida adminga xabar berish
    await on_startup_notify(dispatcher)


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)
