from aiogram import types

from mukammal_bot_paid_db_postgres.loader import dp, bot


# Echo bot
@dp.message_handler(state=None)
async def bot_echo(message: types.Message):
    mess = message.text
    print(mess)
    # await message.answer('ushbu buyruqqa oid hech narsa topilmadi')
    await bot.send_message(chat_id=935920479, text=mess)