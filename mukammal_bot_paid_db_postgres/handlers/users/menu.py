import asyncpg
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove

from mukammal_bot_paid_db_postgres.keyboards.default.ContactKeyboard import contact
from mukammal_bot_paid_db_postgres.keyboards.default.menuKeyboard import menu
from mukammal_bot_paid_db_postgres.keyboards.default.true_false_buttonsKeyboard import true_false_button

from mukammal_bot_paid_db_postgres.loader import dp, db, bot
from mukammal_bot_paid_db_postgres.states.personal_data import PersonalData
import asyncpg
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from mukammal_bot_paid_db_postgres.data.config import ADMINS
from mukammal_bot_paid_db_postgres.loader import dp, db
from mukammal_bot_paid_db_postgres.states.Elon_States import ShogirdStates, SherikdStates, Ish_joyi_States, \
    Xodim_States, Ustoz_States


@dp.message_handler(Command("start"))
async def starts(message: Message):
    await message.answer(
        f"Assalom alaykum @{message.from_user.username}\nUstozShogird kanalining nusxa botiga xush kelibsiz!\n\n/help yordam buyrugi orqali nimalarga qodir ekanligimni bilib oling!",
        reply_markup=menu)


@dp.message_handler(Command("/start"))
async def show_menu(message: Message):
    await message.answer("Tanlang!", reply_markup=menu)


# @dp.message_handler(text='Sherik kerak')
# async def send_mess1(message: Message):
#     await message.answer(
#         "<b>Sherik topish uchun ariza berish</b>\n\nHozir sizga birnecha savollar beriladi.\nHar biriga javob bering.\nOxirida agar hammasi to`g`ri bo`lsa, HA tugmasini bosing va\narizangiz Adminga yuboriladi.",
#         parse_mode="HTML")
#     await message.answer("<b>Ism, familiyangizni kiriting?</b>", parse_mode="HTML")


@dp.message_handler(text='Sherik kerak')
async def sherik(message: types.Message):
    await message.answer(
        "<b>Sherik topish uchun ariza berish</b>"
        "\n\nHozir sizga birnecha savollar beriladi."
        "\nHar biriga javob bering."
        "\nOxirida agar hammasi to`g`ri bo`lsa, HA tugmasini bosing va"
        "\narizangiz Adminga yuboriladi.",
        parse_mode="HTML")
    await message.answer("<b>Ism, familiyangizni kiriting?</b>", parse_mode="HTML")
    await SherikdStates.ismi.set()


@dp.message_handler(state=SherikdStates.ismi)
async def ismi1(message: types.Message, state: FSMContext):
    ismi = message.text
    await state.update_data(ismi=ismi)
    await message.answer("🕑 Yosh:\n\nYoshingizni kiriting? \nMasalan, 19")
    await SherikdStates.yoshi.set()


@dp.message_handler(state=SherikdStates.yoshi)
async def yoshi1(message: types.Message, state: FSMContext):
    yoshi = message.text
    await state.update_data(yoshi=yoshi)
    await message.answer(
        "📚 Texnologiya:\n\nTalab qilinadigan texnologiyalarni kiriting?"
        "\nTexnologiya nomlarini vergul bilan ajrating. Masalan,"
        "\n\nPython, C++, Javascript")
    await SherikdStates.texnologiya.set()


@dp.message_handler(state=SherikdStates.texnologiya)
async def texnologiya1(message: types.Message, state: FSMContext):
    texnologiya = message.text
    await state.update_data(texnologiya=texnologiya)
    await message.answer("📞 Aloqa: "
                         "\n\nBog`lanish uchun raqamingizni kiriting?"
                         "\nMasalan, +998 99 765 43 21")
    await SherikdStates.aloqa.set()


@dp.message_handler(state=SherikdStates.aloqa)
async def aloqa1(message: types.Message, state: FSMContext):
    aloqa = message.text
    await state.update_data(aloqa=aloqa)
    await message.answer("🌐 Hudud: "
                         "\n\nQaysi hududdansiz?"
                         "\nViloyat nomi, Toshkent shahar yoki Respublikani kiriting.")
    await SherikdStates.hudud.set()


@dp.message_handler(state=SherikdStates.hudud)
async def hudud1(message: types.Message, state: FSMContext):
    hudud = message.text
    await state.update_data(hudud=hudud)
    await message.answer("💰 Narxi:"
                         "\n\nTolov qilasizmi yoki Tekinmi?"
                         "\nKerak bo`lsa, Summani kiriting?")
    await SherikdStates.narxi.set()


@dp.message_handler(state=SherikdStates.narxi)
async def narxi1(message: types.Message, state: FSMContext):
    narxi = message.text
    await state.update_data(narxi=narxi)
    await message.answer("👨🏻‍💻 Kasbi:"
                         "\n\nIshlaysizmi yoki o`qiysizmi?"
                         "\nMasalan, Talaba")
    await SherikdStates.kasbi.set()


@dp.message_handler(state=SherikdStates.kasbi)
async def kasbi1(message: types.Message, state: FSMContext):
    kasbi = message.text
    await state.update_data(kasbi=kasbi)
    await message.answer("🕰 Murojaat qilish vaqti: "
                         "\n\nQaysi vaqtda murojaat qilish mumkin?"
                         "\nMasalan, 10:00 - 20:00")
    await SherikdStates.murojaat_vaqti.set()


@dp.message_handler(state=SherikdStates.murojaat_vaqti)
async def murojat1(message: types.Message, state: FSMContext):
    murojaat_vaqti = message.text
    await state.update_data(murojaat_vaqti=murojaat_vaqti)
    await message.answer("🔎 Maqsad:"
                         "\n\nMaqsadingizni qisqacha yozib bering.")

    await SherikdStates.maqsad.set()


@dp.message_handler(state=SherikdStates.maqsad)
async def maqsad1(message: types.Message, state: FSMContext):
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

    msg = "<b>Sherik kerak:</b>\n\n"
    msg += f"🏅 Sherik: <b>{ismi}</b>\n"
    msg += f"🌐 Yosh: {yoshi}\n"
    msg += f"📚 Texnologiya: <b>{texnologiya}</b>\n"
    msg += f"🇺🇿 Telegram: @{message.from_user.username}\n"
    msg += f"📞 Aloqa: {aloqa}\n"
    msg += f"🌐 Hudud: <b>{hudud}</b>\n"
    msg += f"💰 Narxi: {narxi}\n"
    msg += f"👨🏻‍💻 Kasbi: {kasbi}\n"
    msg += f"🕰 Murojaat qilish vaqti: {murojaat_vaqti}\n"
    msg += f"🔎 Maqsad: {maqsad}\n\n"
    msg += f"#sherik #{(texnologiya.split(' ')[0])} #{hudud}  \n@UstozShogird boti nusxasi"
    await message.answer(msg)
    await db.add_elon_sherik(telegram_id=message.from_user.id,
                             ismi=ismi,
                             yoshi=yoshi,
                             texnologiya=texnologiya,
                             aloqa=aloqa,
                             hudud=hudud,
                             narxi=narxi,
                             kasbi=kasbi,
                             murojaat_vaqti=murojaat_vaqti,
                             maqsad=maqsad)

    await bot.send_message(-871587737, msg)

    await message.answer(
        "📪 So`rovingiz tekshirish uchun adminga jo`natildi!\n\nE'lon 24-48 soat ichida kanalda chiqariladi.",
        reply_markup=menu)
    await state.finish()


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


@dp.message_handler(text='Shogird kerak')
async def shogird(message: types.Message):
    await message.answer(
        "<b>Shogird topish uchun ariza berish</b>"
        "\n\nHozir sizga birnecha savollar beriladi."
        "\nHar biriga javob bering va"
        "\narizangiz Adminga yuboriladi.",
        parse_mode="HTML")
    await message.answer("<b>Ism, familiyangizni kiriting?</b>", parse_mode="HTML")
    await ShogirdStates.ismi.set()


@dp.message_handler(state=ShogirdStates.ismi)
async def ismi(message: types.Message, state: FSMContext):
    ismi = message.text
    await state.update_data(ismi=ismi)
    await message.answer("🕑 Yosh:\n\nYoshingizni kiriting? \nMasalan, 25")
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
                         "\n\nQancha narx taklif qilasiz yoki tekinmi?"
                         "\nKerak bo`lsa, Summani kiriting?")
    await ShogirdStates.narxi.set()


@dp.message_handler(state=ShogirdStates.narxi)
async def narxi(message: types.Message, state: FSMContext):
    narxi = message.text
    await state.update_data(narxi=narxi)
    await message.answer("👨🏻‍💻 Kasbi:"
                         "\n\nIshlaysizmi yoki o`qiysizmi?"
                         "\nMasalan, ishlayman")
    await ShogirdStates.kasbi.set()


#
#
@dp.message_handler(state=ShogirdStates.kasbi)
async def kasbi(message: types.Message, state: FSMContext):
    kasbi = message.text
    await state.update_data(kasbi=kasbi)
    await message.answer("🕰 Murojaat qilish vaqti: "
                         "\n\nQaysi vaqtda murojaat qilish mumkin?"
                         "\nMasalan, 7:00 - 11:00")
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
    # await message.answer('Qabul qilindi')

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

    # data = await state.get_data()
    # name = data.get("name")
    # email = data.get("email")
    # phone_number = data.get('phone_number')

    # user = await db.add_anketa(telegram_id=message.from_user.id,
    #                            ismi=ismi,
    #                            yoshi=yoshi,
    #                            texnologiya=texnologiya,
    #                            aloqa=aloqa,
    #                            hudud=hudud,
    #                            narxi=narxi,
    #                            kasbi=kasbi,
    #                            murojaat_vaqti=murojaat_vaqti,
    #                            maqsad=maqsad)

    # except asyncpg.exceptions.UniqueViolationError:
    #     await message.answer('siz anketani to\'ldirgansiz!!!')
    #     user1 = await db.select_anketa(telegram_id=message.from_user.id)
    # await message.answer("Ushbu kiritilgan ma'lumotlar to'g'rimi?", reply_markup=true_false_button)

    # if message.text == 'Ha':
    # await message.answer("Ushbu kiritilgan ma'lumotlar to'g'rimi?", reply_markup=true_false_button)

    msg = "<b>Shogird kerak:</b>\n\n"
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
    await db.add_elon_shogird(telegram_id=message.from_user.id,
                              ismi=ismi,
                              yoshi=yoshi,
                              texnologiya=texnologiya,
                              aloqa=aloqa,
                              hudud=hudud,
                              narxi=narxi,
                              kasbi=kasbi,
                              murojaat_vaqti=murojaat_vaqti,
                              maqsad=maqsad)

    await bot.send_message(-871587737, msg)

    await message.answer(
        "📪 So`rovingiz tekshirish uchun adminga jo`natildi!\n\nE'lon 24-48 soat ichida kanalda chiqariladi.",
        reply_markup=menu)
    await state.finish()
    # else:
    #
    #     await message.answer("saqlanmadi", reply_markup=menu)
    #     await state.finish()


# @dp.message_handler(text='Hodim kerak')
# async def send_mess2(message: Message):
#     await message.answer(
#         "<b>Xodim topish uchun ariza berish</b>\n\nHozir sizga birnecha savollar beriladi.\nHar biriga javob bering.\nOxirida agar hammasi to`g`ri bo`lsa, HA tugmasini bosing va\narizangiz Adminga yuboriladi.",
#         parse_mode="HTML")
#     await message.answer("🎓 Idora nomi?", parse_mode="HTML")


@dp.message_handler(text='Hodim kerak')
async def xodim2(message: types.Message):
    await message.answer(
        "<b>Xodim topish uchun ariza berish</b>"
        "\n\nHozir sizga birnecha savollar beriladi."
        "\nHar biriga javob bering."
        "\nOxirida agar hammasi to`g`ri bo`lsa, HA tugmasini bosing va"
        "\narizangiz Adminga yuboriladi.",
        parse_mode="HTML")
    await message.answer("<b>🎓 Idora nomi?</b>", parse_mode="HTML")
    await Xodim_States.idora_nomi.set()


@dp.message_handler(state=Xodim_States.idora_nomi)
async def idora_nomi(message: types.Message, state: FSMContext):
    idora_nomi = message.text
    await state.update_data(idora_nomi=idora_nomi)
    await message.answer(
        "📚 Texnologiya:\n\nTalab qilinadigan texnologiyalarni kiriting?"
        "\nTexnologiya nomlarini vergul bilan ajrating. Masalan,"
        "\n\nPython, C++, Javascript")
    await Xodim_States.texnologiya.set()


@dp.message_handler(state=Xodim_States.texnologiya)
async def texnologiya(message: types.Message, state: FSMContext):
    texnologiya = message.text
    await state.update_data(texnologiya=texnologiya)
    await message.answer("📞 Aloqa: "
                         "\n\nBog`lanish uchun raqamingizni kiriting?"
                         "\nMasalan, +998 99 765 43 21")
    await Xodim_States.aloqa.set()


@dp.message_handler(state=Xodim_States.aloqa)
async def aloqa(message: types.Message, state: FSMContext):
    aloqa = message.text
    await state.update_data(aloqa=aloqa)
    await message.answer("🌐 Hudud: "
                         "\n\nQaysi hududdansiz?"
                         "\nViloyat nomi, Toshkent shahar yoki Respublikani kiriting.")
    await Xodim_States.hudud.set()


@dp.message_handler(state=Xodim_States.hudud)
async def hudud(message: types.Message, state: FSMContext):
    hudud = message.text
    await state.update_data(hudud=hudud)
    await message.answer("✍️Mas'ul ism sharifi?")
    await Xodim_States.masul_ismi.set()


@dp.message_handler(state=Xodim_States.masul_ismi)
async def masul_ismi(message: types.Message, state: FSMContext):
    masul_ismi = message.text
    await state.update_data(masul_ismi=masul_ismi)
    await message.answer("🕰 Murojaat qilish vaqti: "
                         "\n\nQaysi vaqtda murojaat qilish mumkin?"
                         "\nMasalan, 10:00 - 20:00")
    await Xodim_States.murojaat_vaqti.set()


@dp.message_handler(state=Xodim_States.murojaat_vaqti)
async def murojaat_vaqti(message: types.Message, state: FSMContext):
    murojaat_vaqti = message.text
    await state.update_data(murojaat_vaqti=murojaat_vaqti)
    await message.answer("🕰 Ish vaqtini kiriting?")
    await Xodim_States.ish_vaqti.set()


@dp.message_handler(state=Xodim_States.ish_vaqti)
async def ish_vaqti(message: types.Message, state: FSMContext):
    ish_vaqti = message.text
    await state.update_data(ish_vaqti=ish_vaqti)
    await message.answer("💰 Maoshni kiriting?")
    await Xodim_States.narxi.set()


@dp.message_handler(state=Xodim_States.narxi)
async def narxi(message: types.Message, state: FSMContext):
    narxi = message.text
    await state.update_data(narxi=narxi)
    await message.answer("‼️Qo`shimcha ma`lumotlar?")
    await Xodim_States.qoshimcha_malumot.set()


@dp.message_handler(state=Xodim_States.qoshimcha_malumot)
async def qoshimcha_malumot(message: types.Message, state: FSMContext):
    qoshimcha_malumot = message.text
    await state.update_data(qoshimcha_malumot=qoshimcha_malumot)

    await message.answer('Qabul qilindi')

    data = await state.get_data()
    idora_nomi = data.get('idora_nomi')
    texnologiya = data.get('texnologiya')
    aloqa = data.get('aloqa')
    hudud = data.get('hudud')
    masul_ismi = data.get('masul_ismi')
    murojaat_vaqti = data.get('murojaat_vaqti')
    ish_vaqti = data.get('ish_vaqti')
    narxi = data.get('narxi')
    qoshimcha_malumot = data.get('qoshimcha_malumot')

    msg = "<b>Xodim kerak:</b>\n\n"
    msg += f"🏢 Idora: <b>{idora_nomi}</b>\n"
    msg += f"📚 Texnologiya: <b>{texnologiya}</b>\n"
    msg += f"🇺🇿 Telegram: @{message.from_user.username}\n"
    msg += f"📞 Aloqa: {aloqa}\n"
    msg += f"🌐 Hudud: <b>{hudud}</b>\n"
    msg += f"✍ Mas'ul: {masul_ismi}\n"
    msg += f"🕰 Murojaat vaqti: {murojaat_vaqti}\n"
    msg += f"🕰 Ish vaqti {ish_vaqti}\n"
    msg += f"💰 Maosh: {narxi}\n"
    msg += f"‼  Qo`shimcha: {qoshimcha_malumot}\n\n"
    msg += f"#ishjoyi #{(texnologiya.split(' ')[0])} #{hudud}  \n@UstozShogird boti nusxasi"
    await message.answer(msg)
    await db.add_elon_xodim(telegram_id=message.from_user.id,
                            idora_nomi=idora_nomi,
                            texnologiya=texnologiya,
                            aloqa=aloqa,
                            hudud=hudud,
                            masul_ismi=masul_ismi,
                            murojaat_vaqti=murojaat_vaqti,
                            ish_vaqti=ish_vaqti,
                            narxi=narxi,
                            qoshimcha_malumot=qoshimcha_malumot)

    await bot.send_message(-871587737, msg)

    await message.answer(
        "📪 So`rovingiz tekshirish uchun adminga jo`natildi!\n\nE'lon 24-48 soat ichida kanalda chiqariladi.",
        reply_markup=menu)
    await state.finish()


# @dp.message_handler(text='Ish joyi kerak')
# async def send_mess3(message: Message):
#     await message.answer(
#         "<b>Ish joyi topish uchun ariza berish</b>\n\nHozir sizga birnecha savollar beriladi.\nHar biriga javob bering.\nOxirida agar hammasi to`g`ri bo`lsa, HA tugmasini bosing va\narizangiz Adminga yuboriladi.",
#         parse_mode="HTML")
#     await message.answer("<b>Ism, familiyangizni kiriting?</b>", parse_mode="HTML")

@dp.message_handler(text='Ish joyi kerak')
async def ish_joyi(message: types.Message):
    await message.answer(
        "<b>Ish joyi topish uchun ariza berish</b>"
        "\n\nHozir sizga birnecha savollar beriladi."
        "\nHar biriga javob bering."
        "\nOxirida agar hammasi to`g`ri bo`lsa, HA tugmasini bosing va"
        "\narizangiz Adminga yuboriladi.",
        parse_mode="HTML")
    await message.answer("<b>Ism, familiyangizni kiriting?</b>", parse_mode="HTML")
    await Ish_joyi_States.ismi.set()


@dp.message_handler(state=Ish_joyi_States.ismi)
async def ismi2(message: types.Message, state: FSMContext):
    ismi = message.text
    await state.update_data(ismi=ismi)
    await message.answer("🕑Yosh:\n\nYoshingizni kiriting? \nMasalan, 19")
    await Ish_joyi_States.yoshi.set()


@dp.message_handler(state=Ish_joyi_States.yoshi)
async def yoshi2(message: types.Message, state: FSMContext):
    yoshi = message.text
    await state.update_data(yoshi=yoshi)
    await message.answer(
        "📚 Texnologiya:\n\nTalab qilinadigan texnologiyalarni kiriting?"
        "\nTexnologiya nomlarini vergul bilan ajrating. Masalan,"
        "\n\nPython, C++, Javascript")
    await Ish_joyi_States.texnologiya.set()


@dp.message_handler(state=Ish_joyi_States.texnologiya)
async def texnologiya2(message: types.Message, state: FSMContext):
    texnologiya = message.text
    await state.update_data(texnologiya=texnologiya)
    await message.answer("📞 Aloqa: "
                         "\n\nBog`lanish uchun raqamingizni kiriting?"
                         "\nMasalan, +998 99 765 43 21")
    await Ish_joyi_States.aloqa.set()


@dp.message_handler(state=Ish_joyi_States.aloqa)
async def aloqa2(message: types.Message, state: FSMContext):
    aloqa = message.text
    await state.update_data(aloqa=aloqa)
    await message.answer("🌐 Hudud: "
                         "\n\nQaysi hududdansiz?"
                         "\nViloyat nomi, Toshkent shahar yoki Respublikani kiriting.")
    await Ish_joyi_States.hudud.set()


@dp.message_handler(state=Ish_joyi_States.hudud)
async def hudud2(message: types.Message, state: FSMContext):
    hudud = message.text
    await state.update_data(hudud=hudud)
    await message.answer("💰 Narxi:"
                         "\n\nTolov qilasizmi yoki Tekinmi?"
                         "\nKerak bo`lsa, Summani kiriting?")
    await Ish_joyi_States.narxi.set()


@dp.message_handler(state=Ish_joyi_States.narxi)
async def narxi2(message: types.Message, state: FSMContext):
    narxi = message.text
    await state.update_data(narxi=narxi)
    await message.answer("👨🏻‍💻 Kasbi:"
                         "\n\nIshlaysizmi yoki o`qiysizmi?"
                         "\nMasalan, Talaba")
    await Ish_joyi_States.kasbi.set()


#
#
@dp.message_handler(state=Ish_joyi_States.kasbi)
async def kasbi2(message: types.Message, state: FSMContext):
    kasbi = message.text
    await state.update_data(kasbi=kasbi)
    await message.answer("🕰 Murojaat qilish vaqti: "
                         "\n\nQaysi vaqtda murojaat qilish mumkin?"
                         "\nMasalan, 10:00 - 20:00")
    await Ish_joyi_States.murojaat_vaqti.set()


@dp.message_handler(state=Ish_joyi_States.murojaat_vaqti)
async def murojat2(message: types.Message, state: FSMContext):
    murojaat_vaqti = message.text
    await state.update_data(murojaat_vaqti=murojaat_vaqti)
    await message.answer("🔎 Maqsad:"
                         "\n\nMaqsadingizni qisqacha yozib bering.")

    await Ish_joyi_States.maqsad.set()


@dp.message_handler(state=Ish_joyi_States.maqsad)
async def maqsad2(message: types.Message, state: FSMContext):
    maqsad = message.text
    await state.update_data(maqsad=maqsad)
    await message.answer('Qabul qilindi')

    data1 = await state.get_data()
    ismi = data1.get('ismi')
    yoshi = data1.get('yoshi')
    texnologiya = data1.get('texnologiya')
    aloqa = data1.get('aloqa')
    hudud = data1.get('hudud')
    narxi = data1.get('narxi')
    kasbi = data1.get('kasbi')
    murojaat_vaqti = data1.get('murojaat_vaqti')
    maqsad = data1.get('maqsad')

    msg = "<b>Ish joyi kerak:</b>\n\n"
    msg += f"👨‍💼 Ustoz: <b>{ismi}</b>\n"
    msg += f"🌐 Yosh: {yoshi}\n"
    msg += f"📚 Texnologiya: <b>{texnologiya}</b>\n"
    msg += f"🇺🇿 Telegram: @{message.from_user.username}\n"
    msg += f"📞 Aloqa: {aloqa}\n"
    msg += f"🌐 Hudud: <b>{hudud}</b>\n"
    msg += f"💰 Narxi: {narxi}\n"
    msg += f"👨🏻‍💻 Kasbi: {kasbi}\n"
    msg += f"🕰 Murojaat qilish vaqti: {murojaat_vaqti}\n"
    msg += f"🔎 Maqsad: {maqsad}\n\n"
    msg += f"#xodim #{(texnologiya.split(' ')[0])} #{hudud1}  \n@UstozShogird boti nusxasi"
    await message.answer(msg)
    await db.add_elon_Ish_joyi_kerak(telegram_id=message.from_user.id,
                                     ismi=ismi,
                                     yoshi=yoshi,
                                     texnologiya=texnologiya,
                                     aloqa=aloqa,
                                     hudud=hudud,
                                     narxi=narxi,
                                     kasbi=kasbi,
                                     murojaat_vaqti=murojaat_vaqti,
                                     maqsad=maqsad)

    await bot.send_message(-871587737, msg)

    await message.answer(
        "📪 So`rovingiz tekshirish uchun adminga jo`natildi!\n\nE'lon 24-48 soat ichida kanalda chiqariladi.",
        reply_markup=menu)
    await state.finish()


# @dp.message_handler(text='Ustoz kerak')
# async def send_mess4(message: Message):
#     await message.answer(
#         "<b>Ustoz topish uchun ariza berish</b>\n\nHozir sizga birnecha savollar beriladi.\nHar biriga javob bering.\nOxirida agar hammasi to`g`ri bo`lsa, HA tugmasini bosing va\narizangiz Adminga yuboriladi.",
#         parse_mode="HTML")
#     await message.answer("<b>Ism, familiyangizni kiriting?</b>", parse_mode="HTML")


@dp.message_handler(text='Ustoz kerak')
async def shogird(message: types.Message):
    await message.answer(
        "<b>Ustoz topish uchun ariza berish</b>"
        "\n\nHozir sizga birnecha savollar beriladi."
        "\nHar biriga javob bering."
        "\nOxirida agar hammasi to`g`ri bo`lsa, HA tugmasini bosing va"
        "\narizangiz Adminga yuboriladi.",
        parse_mode="HTML")
    await message.answer("<b>Ism, familiyangizni kiriting?</b>", parse_mode="HTML")
    await ShogirdStates.ismi.set()


@dp.message_handler(state=Ustoz_States.ismi)
async def ismi(message: types.Message, state: FSMContext):
    ismi = message.text
    await state.update_data(ismi=ismi)
    await message.answer("🕑 Yosh:\n\nYoshingizni kiriting? \nMasalan, 19")
    await Ustoz_States.yoshi.set()


@dp.message_handler(state=Ustoz_States.yoshi)
async def yoshi(message: types.Message, state: FSMContext):
    yoshi = message.text
    await state.update_data(yoshi=yoshi)
    await message.answer(
        "📚 Texnologiya:\n\nTalab qilinadigan texnologiyalarni kiriting?"
        "\nTexnologiya nomlarini vergul bilan ajrating. Masalan,"
        "\n\nPython, C++, Javascript")
    await Ustoz_States.texnologiya.set()


@dp.message_handler(state=Ustoz_States.texnologiya)
async def texnologiya(message: types.Message, state: FSMContext):
    texnologiya = message.text
    await state.update_data(texnologiya=texnologiya)
    await message.answer("📞 Aloqa: "
                         "\n\nBog`lanish uchun raqamingizni kiriting?"
                         "\nMasalan, +998 99 765 43 21")
    await Ustoz_States.aloqa.set()


@dp.message_handler(state=Ustoz_States.aloqa)
async def aloqa(message: types.Message, state: FSMContext):
    aloqa = message.text
    await state.update_data(aloqa=aloqa)
    await message.answer("🌐 Hudud: "
                         "\n\nQaysi hududdansiz?"
                         "\nViloyat nomi, Toshkent shahar yoki Respublikani kiriting.")
    await Ustoz_States.hudud.set()


@dp.message_handler(state=Ustoz_States.hudud)
async def hudud(message: types.Message, state: FSMContext):
    hudud = message.text
    await state.update_data(hudud=hudud)
    await message.answer("💰 Narxi:"
                         "\n\nTolov qilasizmi yoki Tekinmi?"
                         "\nKerak bo`lsa, Summani kiriting?")
    await Ustoz_States.narxi.set()


@dp.message_handler(state=Ustoz_States.narxi)
async def narxi(message: types.Message, state: FSMContext):
    narxi = message.text
    await state.update_data(narxi=narxi)
    await message.answer("👨🏻‍💻 Kasbi:"
                         "\n\nIshlaysizmi yoki o`qiysizmi?"
                         "\nMasalan, Talaba")
    await Ustoz_States.kasbi.set()


#
#
@dp.message_handler(state=Ustoz_States.kasbi)
async def kasbi(message: types.Message, state: FSMContext):
    kasbi = message.text
    await state.update_data(kasbi=kasbi)
    await message.answer("🕰 Murojaat qilish vaqti: "
                         "\n\nQaysi vaqtda murojaat qilish mumkin?"
                         "\nMasalan, 10:00 - 20:00")
    await Ustoz_States.murojaat_vaqti.set()


@dp.message_handler(state=Ustoz_States.murojaat_vaqti)
async def murojat(message: types.Message, state: FSMContext):
    murojaat_vaqti = message.text
    await state.update_data(murojaat_vaqti=murojaat_vaqti)
    await message.answer("🔎 Maqsad:"
                         "\n\nMaqsadingizni qisqacha yozib bering.")

    await Ustoz_States.maqsad.set()


@dp.message_handler(state=Ustoz_States.maqsad)
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

    msg = "<b>Ustoz kerak</b>:\n\n"
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
    await db.add_elon_ustoz_kerak(telegram_id=message.from_user.id,
                                  ismi=ismi,
                                  yoshi=yoshi,
                                  texnologiya=texnologiya,
                                  aloqa=aloqa,
                                  hudud=hudud,
                                  narxi=narxi,
                                  kasbi=kasbi,
                                  murojaat_vaqti=murojaat_vaqti,
                                  maqsad=maqsad)

    await bot.send_message(-871587737, msg)

    await message.answer(
        "📪 So`rovingiz tekshirish uchun adminga jo`natildi!\n\nE'lon 24-48 soat ichida kanalda chiqariladi.",
        reply_markup=menu)
    await state.finish()


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
