from aiogram import types
from aiogram.dispatcher import FSMContext

from mukammal_bot_paid_db_postgres.loader import dp


@dp.message_handler(commands='xarid')
async def set_state(msg: types.Message, state: FSMContext):
    await state.set_state('xarid_state')
    await msg.answer("Mahsulot tanlang")


@dp.message_handler(state='xarid_state')
async def state_example(msg: types.Message, state: FSMContext):
    await state.set_state('tolov')
    await msg.answer("Mahsulot savatga qo'shildi")


@dp.message_handler(state='tolov')
async def state_pay(msg: types.Message, state: FSMContext):
    await msg.answer('Tolov qiling')
    await state.finish()
