from aiogram import types
from aiogram.dispatcher import FSMContext
# from aiogram.dispatcher.filters import state

from mukammal_bot_paid_db_postgres.loader import dp, bot
from mukammal_bot_paid_db_postgres.states.Elon_States import ShogirdStates


@dp.message_handler(text='Shogird kerak')
async def shogird(message: types.Message):
    await message.answer(
        "<b>Shogird topish uchun ariza berish</b>"
        "\n\nHozir sizga birnecha savollar beriladi."
        "\nHar biriga javob bering."
        "\nOxirida agar hammasi to`g`ri bo`lsa, HA tugmasini bosing va"
        "\narizangiz Adminga yuboriladi.",
        parse_mode="HTML")
    await message.answer("<b>Ism, familiyangizni kiriting?</b>", parse_mode="HTML")
    await ShogirdStates.ismi.set()


@dp.message_handler(state=ShogirdStates.ismi)
async def ismi(message: types.Message, state: FSMContext):
    ismi = message.text
    await state.update_data(ismi=ismi)
    await message.answer("🕑 Yosh:\n\nYoshingizni kiriting? \nMasalan, 19")
    await ShogirdStates.yoshi.set()


@dp.message_handler(state=ShogirdStates.yoshi)
async def yoshi(message: types.Message, state: FSMContext):
    yoshi = message.text
    await state.update_data(yoshi=yoshi)
    await message.answer(
        "📚 Texnologiya:\n\nTalab qilinadigan texnologiyalarni kiriting?"
        "\nTexnologiya nomlarini vergul bilan ajrating. Masalan,"
        "\n\nPython, C++, Javascript")
    await ShogirdStates.texnologiya.set()


@dp.message_handler(state=ShogirdStates.texnologiya)
async def texnologiya(message: types.Message, state: FSMContext):
    texnologiya = message.text
    await state.update_data(texnologiya=texnologiya)
    await message.answer("📞 Aloqa: "
                         "\n\nBog`lanish uchun raqamingizni kiriting?"
                         "\nMasalan, +998 99 765 43 21")
    await ShogirdStates.aloqa.set()


@dp.message_handler(state=ShogirdStates.aloqa)
async def aloqa(message: types.Message, state: FSMContext):
    aloqa = message.text
    await state.update_data(aloqa=aloqa)
    await message.answer("🌐 Hudud: "
                         "\n\nQaysi hududdansiz?"
                         "\nViloyat nomi, Toshkent shahar yoki Respublikani kiriting.")
    await ShogirdStates.hudud.set()


@dp.message_handler(state=ShogirdStates.hudud)
async def hudud(message: types.Message, state: FSMContext):
    hudud = message.text
    await state.update_data(hudud=hudud)
    await message.answer("💰 Narxi:"
                         "\n\nTolov qilasizmi yoki Tekinmi?"
                         "\nKerak bo`lsa, Summani kiriting?")
    await ShogirdStates.narxi.set()


@dp.message_handler(state=ShogirdStates.narxi)
async def narxi(message: types.Message, state: FSMContext):
    narxi = message.text
    await state.update_data(narxi=narxi)
    await message.answer("👨🏻‍💻 Kasbi:"
                         "\n\nIshlaysizmi yoki o`qiysizmi?"
                         "\nMasalan, Talaba")
    await ShogirdStates.kasbi.set()


#
#
@dp.message_handler(state=ShogirdStates.kasbi)
async def kasbi(message: types.Message, state: FSMContext):
    kasbi = message.text
    await state.update_data(kasbi=kasbi)
    await message.answer("🕰 Murojaat qilish vaqti: "
                         "\n\nQaysi vaqtda murojaat qilish mumkin?"
                         "\nMasalan, 10:00 - 20:00")
    await ShogirdStates.murojaat_vaqti.set()


@dp.message_handler(state=ShogirdStates.murojaat_vaqti)
async def murojat(message: types.Message, state: FSMContext):
    murojaat_vaqti = message.text
    await state.update_data(murojaat_vaqti=murojaat_vaqti)
    await message.answer("🔎 Maqsad:"
                         "\n\nMaqsadingizni qisqacha yozib bering.")

    await ShogirdStates.maqsad.set()


@dp.message_handler(state=ShogirdStates.maqsad)
async def maqsad(message: types.Message, state: FSMContext):
    maqsad = message.text
    await state.update_data(maqsad=maqsad)
    await message.answer('Qabul qilindi')

    data = await state.get_data()
    ismi = data.get('ismi')
    yoshi = data.get('yoshi')
    texnologiya = data.get('texnologiya')
    aloqa = data.get('aloqa')
    hudud = data.get('hudud')
    narxi = data.get('narxi')
    kasbi = data.get('kasbi')
    murojaat_vaqti = data.get('murojaat_vaqti')
    maqsad = data.get('maqsad')

    msg = "<b>Shogird kerak</b>:\n\n"
    msg += f"🎓 Ustoz: <b>{ismi}</b>\n"
    msg += f"🌐 Yosh: {yoshi}\n"
    msg += f"📚 Texnologiya: <b>{texnologiya}</b>\n"
    msg += f"🇺🇿 Telegram: @{message.from_user.username}\n"
    msg += f"📞 Aloqa: {aloqa}\n"
    msg += f"🌐 Hudud: <b>{hudud}</b>\n"
    msg += f"💰 Narxi: {narxi}\n"
    msg += f"👨🏻‍💻 Kasbi: {kasbi}\n"
    msg += f"🕰 Murojaat qilish vaqti: {murojaat_vaqti}\n"
    msg += f"🔎 Maqsad: {maqsad}\n\n"
    msg += f"#shogird #{(texnologiya.split(' ')[0])} #{hudud}  \n@UstozShogird boti nusxasi"
    await message.answer(msg)
    await bot.send_message(-871587737, msg)

    await state.finish()
