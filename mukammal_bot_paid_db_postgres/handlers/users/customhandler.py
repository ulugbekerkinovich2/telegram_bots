from aiogram import types

from mukammal_bot_paid_db_postgres.data.config import ADMINS
from mukammal_bot_paid_db_postgres.loader import dp

SUPERUSERS = [935920479]


@dp.message_handler(chat_id=ADMINS, commands='/start')
async def id_filter_example(msg: types.Message):
    await msg.answer('Xush kelibsiz ADMIN')
