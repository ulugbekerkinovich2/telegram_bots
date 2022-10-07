import asyncpg
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from mukammal_bot_paid_db_postgres.data.config import ADMINS
from mukammal_bot_paid_db_postgres.loader import dp, db, bot
from mukammal_bot_paid_db_postgres.states.personal_data import PersonalData


@dp.message_handler(text='anketa')
async def enter_test(message: types.Message):
    await message.answer("to'liq ismingizni kiriting: ")
    await PersonalData.fullname.set()


@dp.message_handler(state=PersonalData.fullname)
async def answer_fullname(message: types.Message, state: FSMContext):
    fullname = message.text
    await state.update_data(name=fullname)
    await message.answer('Email manzil kiriting')
    await PersonalData.email.set()


@dp.message_handler(state=PersonalData.email)
async def answer_email(message: types.Message, state: FSMContext):
    email = message.text
    await state.update_data(email=email)
    await message.answer('Telefon raqam kiriting')
    await PersonalData.phone_number.set()


@dp.message_handler(state=PersonalData.phone_number)
async def answer_phonnum(message: types.Message, state: FSMContext):
    phone_number = message.text
    await state.update_data(phone_number=phone_number)

    data = await state.get_data()
    name = data.get("name")
    email = data.get("email")
    phone_number = data.get('phone_number')

    try:
        user = await db.add_anketa(telegram_id=message.from_user.id,
                                   fullname=name,
                                   email=email,
                                   phone_number=phone_number)

    except asyncpg.exceptions.UniqueViolationError:
        await message.answer('siz anketani to\'ldirgansiz!!!')
        await state.finish()
        user1 = await db.select_anketa(telegram_id=message.from_user.id)


    await message.answer("Ma'lumotlar saqlandi!")

    msg = "Quyidagi ma'lumotlar qabul qilindi:\n"
    msg += f"Ismingiz - {name}\n"
    msg += f"Email - {email}\n"
    msg += f"Telefon raqam - {phone_number}"
    await message.answer(msg)

    await state.finish()
