import asyncpg
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove

from mukammal_bot_paid_db_postgres.keyboards.default.ContactKeyboard import contact
from mukammal_bot_paid_db_postgres.keyboards.default.menuKeyboard import menu

from mukammal_bot_paid_db_postgres.loader import dp, db
from mukammal_bot_paid_db_postgres.states.personal_data import PersonalData
import asyncpg
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from mukammal_bot_paid_db_postgres.data.config import ADMINS
from mukammal_bot_paid_db_postgres.loader import dp, db
from mukammal_bot_paid_db_postgres.states.Elon_States import ShogirdStates


@dp.message_handler(Command("/start"))
async def starts(message: Message):
    await message.answer('Tanglang', reply_markup=menu)


@dp.message_handler(Command("menu"))
async def show_menu(message: Message):
    await message.answer("Tanlang!", reply_markup=menu)


# @dp.message_handler(text='Shogird kerak')
# async def send_mess(message: Message):
#     await message.answer(
#         "<b>Shogird topish uchun ariza berish</b>"
#         "\n\nHozir sizga birnecha savollar beriladi."
#         "\nHar biriga javob bering."
#         "\nOxirida agar hammasi to`g`ri bo`lsa, HA tugmasini bosing va"
#         "\narizangiz Adminga yuboriladi.",
#         parse_mode="HTML")
#     await message.answer("<b>Ism, familiyangizni kiriting?</b>", parse_mode="HTML")


# @dp.message_handler(text='Sherik kerak')
# async def send_mess1(message: Message):
#     await message.answer(
#         "<b>Sherik topish uchun ariza berish</b>\n\nHozir sizga birnecha savollar beriladi.\nHar biriga javob bering.\nOxirida agar hammasi to`g`ri bo`lsa, HA tugmasini bosing va\narizangiz Adminga yuboriladi.",
#         parse_mode="HTML")
#     await message.answer("<b>Ism, familiyangizni kiriting?</b>", parse_mode="HTML")


@dp.message_handler(text='Hodim kerak')
async def send_mess2(message: Message):
    await message.answer(
        "<b>Xodim topish uchun ariza berish</b>\n\nHozir sizga birnecha savollar beriladi.\nHar biriga javob bering.\nOxirida agar hammasi to`g`ri bo`lsa, HA tugmasini bosing va\narizangiz Adminga yuboriladi.",
        parse_mode="HTML")
    await message.answer("🎓 Idora nomi?", parse_mode="HTML")


# @dp.message_handler(text='Ish joyi kerak')
# async def send_mess3(message: Message):
#     await message.answer(
#         "<b>Ish joyi topish uchun ariza berish</b>\n\nHozir sizga birnecha savollar beriladi.\nHar biriga javob bering.\nOxirida agar hammasi to`g`ri bo`lsa, HA tugmasini bosing va\narizangiz Adminga yuboriladi.",
#         parse_mode="HTML")
#     await message.answer("<b>Ism, familiyangizni kiriting?</b>", parse_mode="HTML")


@dp.message_handler(text='Ustoz kerak')
async def send_mess4(message: Message):
    await message.answer(
        "<b>Ustoz topish uchun ariza berish</b>\n\nHozir sizga birnecha savollar beriladi.\nHar biriga javob bering.\nOxirida agar hammasi to`g`ri bo`lsa, HA tugmasini bosing va\narizangiz Adminga yuboriladi.",
        parse_mode="HTML")
    await message.answer("<b>Ism, familiyangizni kiriting?</b>", parse_mode="HTML")


@dp.message_handler(text="Bog'lanish")
async def support(message: Message):
    await message.answer(text="<b>Bog'lanish uchun @status_developer ga murojat qiling</b>", parse_mode='HTML')
    await message.answer("Bog'lanish uchun birini tangalng", reply_markup=contact)


@dp.message_handler(text="Admin bilan bog'lanish")
async def contact_vs_admin(message: Message):
    await message.answer(text="<b>Telegram</b>: @status_developer\n<b>Contact</b>: +998 99 835 90 15")


@dp.message_handler(text="Bot yaratuvchisi bilan bog'lanish")
async def contact_vs_dev(message: Message):
    await message.answer(text="<b>Telegram</b>: @status_py_developer")


@dp.message_handler(text="<<Ortga")
async def back(message: Message):
    await message.answer(text="Tanlang", reply_markup=menu)


# ########
# @dp.message_handler(text='anketa')
# async def enter_test(message: types.Message):
#     await message.answer("to'liq ismingizni kiriting: ")
#     await PersonalData.fullname.set()
#
#
# @dp.message_handler(state=PersonalData.fullname)
# async def answer_fullname(message: types.Message, state: FSMContext):
#     fullname = message.text
#     await state.update_data(name=fullname)
#     await message.answer('Email manzil kiriting')
#     await PersonalData.email.set()
#
#
# @dp.message_handler(state=PersonalData.email)
# async def answer_email(message: types.Message, state: FSMContext):
#     email = message.text
#     await state.update_data(email=email)
#     await message.answer('Telefon raqam kiriting')
#     await PersonalData.phone_number.set()
#
#
# @dp.message_handler(state=PersonalData.phone_number)
# async def answer_phonnum(message: types.Message, state: FSMContext):
#     phone_number = message.text
#     await state.update_data(phone_number=phone_number)
#
#     data = await state.get_data()
#     name = data.get("name")
#     email = data.get("email")
#     phone_number = data.get('phone_number')
#
#     try:
#         user = await db.add_anketa(telegram_id=message.from_user.id,
#                                    fullname=name,
#                                    email=email,
#                                    phone_number=phone_number)
#
#     except asyncpg.exceptions.UniqueViolationError:
#         user1 = await db.select_anketa(telegram_id=message.from_user.id)
#         await message.answer("Ushbu foydalanuvchi ma'lumotlari mazada mavjud")
#
#     await message.answer("Ma'lumotlar saqlandi!")
#
#     msg = "Quyidagi ma'lumotlar qabul qilindi:\n"
#     msg += f"Ismingiz - {name}\n"
#     msg += f"Email - {email}\n"
#     msg += f"Telefon raqam - {phone_number}"
#     await message.answer(msg)
#
#     await state.finish()
