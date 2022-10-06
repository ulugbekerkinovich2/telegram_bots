from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from mukammal_bot_paid_db_postgres.loader import dp

a = '@status_developer'


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = (
        f"{a} tomonidan yaratilgan Ustoz-Shogird kanali nusxasi.\n\nBu yerda Programmalash bo`yicha\n#Ustoz,\n#Shogird,\n#oquvKursi,\n#Sherik,\n#Xodim va\n#IshJoyi\ntopishingiz mumkin.\nE'lon berish: @chints_checkBot\n\nAdmin @status_developer")

    await message.answer(text)
