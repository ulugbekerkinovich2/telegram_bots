# from aiogram import types
# from aiogram.dispatcher import FSMContext
# # from aiogram.dispatcher.filters import state
#
# from mukammal_bot_paid_db_postgres.loader import dp, bot
# from mukammal_bot_paid_db_postgres.states.Elon_States import ShogirdStates
#
#
# @dp.message_handler(text='Ish joyi kerak')
# async def ish_joyi(message: types.Message):
#     await message.answer(
#         "<b>Ish joyi topish uchun ariza berish</b>"
#         "\n\nHozir sizga birnecha savollar beriladi."
#         "\nHar biriga javob bering."
#         "\nOxirida agar hammasi to`g`ri bo`lsa, HA tugmasini bosing va"
#         "\narizangiz Adminga yuboriladi.",
#         parse_mode="HTML")
#     await message.answer("<b>Ism, familiyangizni kiriting?</b>", parse_mode="HTML")
#     await ShogirdStates.ismi.set()
#
#
# @dp.message_handler(state=ShogirdStates.ismi)
# async def ismi2(message: types.Message, state: FSMContext):
#     ismi = message.text
#     await state.update_data(ismi=ismi)
#     await message.answer("ðYosh:\n\nYoshingizni kiriting? \nMasalan, 19")
#     await ShogirdStates.yoshi.set()
#
#
# @dp.message_handler(state=ShogirdStates.yoshi)
# async def yoshi2(message: types.Message, state: FSMContext):
#     yoshi = message.text
#     await state.update_data(yoshi=yoshi)
#     await message.answer(
#         "ð Texnologiya:\n\nTalab qilinadigan texnologiyalarni kiriting?"
#         "\nTexnologiya nomlarini vergul bilan ajrating. Masalan,"
#         "\n\nPython, C++, Javascript")
#     await ShogirdStates.texnologiya.set()
#
#
# @dp.message_handler(state=ShogirdStates.texnologiya)
# async def texnologiya2(message: types.Message, state: FSMContext):
#     texnologiya = message.text
#     await state.update_data(texnologiya=texnologiya)
#     await message.answer("ð Aloqa: "
#                          "\n\nBog`lanish uchun raqamingizni kiriting?"
#                          "\nMasalan, +998 99 765 43 21")
#     await ShogirdStates.aloqa.set()
#
#
# @dp.message_handler(state=ShogirdStates.aloqa)
# async def aloqa2(message: types.Message, state: FSMContext):
#     aloqa = message.text
#     await state.update_data(aloqa=aloqa)
#     await message.answer("ð Hudud: "
#                          "\n\nQaysi hududdansiz?"
#                          "\nViloyat nomi, Toshkent shahar yoki Respublikani kiriting.")
#     await ShogirdStates.hudud.set()
#
#
# @dp.message_handler(state=ShogirdStates.hudud)
# async def hudud2(message: types.Message, state: FSMContext):
#     hudud = message.text
#     await state.update_data(hudud=hudud)
#     await message.answer("ð° Narxi:"
#                          "\n\nTolov qilasizmi yoki Tekinmi?"
#                          "\nKerak bo`lsa, Summani kiriting?")
#     await ShogirdStates.narxi.set()
#
#
# @dp.message_handler(state=ShogirdStates.narxi)
# async def narxi2(message: types.Message, state: FSMContext):
#     narxi = message.text
#     await state.update_data(narxi=narxi)
#     await message.answer("ð¨ð»âð» Kasbi:"
#                          "\n\nIshlaysizmi yoki o`qiysizmi?"
#                          "\nMasalan, Talaba")
#     await ShogirdStates.kasbi.set()
#
#
# #
# #
# @dp.message_handler(state=ShogirdStates.kasbi)
# async def kasbi2(message: types.Message, state: FSMContext):
#     kasbi = message.text
#     await state.update_data(kasbi=kasbi)
#     await message.answer("ð° Murojaat qilish vaqti: "
#                          "\n\nQaysi vaqtda murojaat qilish mumkin?"
#                          "\nMasalan, 10:00 - 20:00")
#     await ShogirdStates.murojaat_vaqti.set()
#
#
# @dp.message_handler(state=ShogirdStates.murojaat_vaqti)
# async def murojat2(message: types.Message, state: FSMContext):
#     murojaat_vaqti = message.text
#     await state.update_data(murojaat_vaqti=murojaat_vaqti)
#     await message.answer("ð Maqsad:"
#                          "\n\nMaqsadingizni qisqacha yozib bering.")
#
#     await ShogirdStates.maqsad.set()
#
#
# @dp.message_handler(state=ShogirdStates.maqsad)
# async def maqsad2(message: types.Message, state: FSMContext):
#         maqsad = message.text
#         await state.update_data(maqsad=maqsad)
#         await message.answer('Qabul qilindi')
#
#         data = await state.get_data()
#         ismi = data.get('ismi')
#         yoshi = data.get('yoshi')
#         texnologiya = data.get('texnologiya')
#         aloqa = data.get('aloqa')
#         hudud = data.get('hudud')
#         narxi = data.get('narxi')
#         kasbi = data.get('kasbi')
#         murojaat_vaqti = data.get('murojaat_vaqti')
#         maqsad = data.get('maqsad')
#
#         msg = "<b>Ish joyi kerak:</b>\n\n"
#         msg += f"ð¨âð¼ Ustoz: <b>{ismi}</b>\n"
#         msg += f"ð Yosh: {yoshi}\n"
#         msg += f"ð Texnologiya: <b>{texnologiya}</b>\n"
#         msg += f"ðºð¿ Telegram: @{message.from_user.username}\n"
#         msg += f"ð Aloqa: {aloqa}\n"
#         msg += f"ð Hudud: <b>{hudud}</b>\n"
#         msg += f"ð° Narxi: {narxi}\n"
#         msg += f"ð¨ð»âð» Kasbi: {kasbi}\n"
#         msg += f"ð° Murojaat qilish vaqti: {murojaat_vaqti}\n"
#         msg += f"ð Maqsad: {maqsad}\n\n"
#         msg += f"xodim #{(texnologiya.split(' ')[0])} #{hudud}  \n@UstozShogird boti nusxasi"
#         await message.answer(msg)
#         await bot.send_message(-871587737, msg)
#
#         await state.finish()
