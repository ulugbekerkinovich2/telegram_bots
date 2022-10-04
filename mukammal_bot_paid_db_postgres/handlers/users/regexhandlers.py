from aiogram import types
from aiogram.dispatcher import filters
from aiogram.dispatcher.filters import Regexp
from mukammal_bot_paid_db_postgres.loader import dp

EMAIL_REGEX = r'[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+'
PHONE_NUM = '^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$'
COMMAND_EMAIL_REGEX = r"/email:" + EMAIL_REGEX


@dp.message_handler(Regexp(EMAIL_REGEX))
async def regexp_email(msg: types.Message):
    await msg.answer('Email qabul qilindi')


@dp.message_handler(Regexp(PHONE_NUM))
async def regexp_phone(msg: types.Message):
    await msg.answer('Telefon qabul qilindi')


@dp.message_handler(regexp_commands=[COMMAND_EMAIL_REGEX])
async def command_regexp_commands(msg: types.Message):
    await msg.answer('Email qabul qilindi')

