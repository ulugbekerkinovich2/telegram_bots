from aiogram.types import message, update
from aiogram import types

from mukammal_bot_paid_db_postgres.loader import dp, bot


@dp.message_handler(content_types=types.ContentTypes.PHOTO)
async def photo_handler(msg: types.Message):
    await msg.answer('rasm qabul qilindi')


@dp.message_handler(content_types=types.ContentTypes.VOICE)
async def voice_handler(msg: types.Message):
    await msg.answer('voice qabul qilindi')


@dp.message_handler(content_types=types.ContentTypes.AUDIO)
async def audio_handler(msg: types.Message):
    await msg.answer('audio qabul qilindi')


@dp.message_handler(content_types=types.ContentTypes.LOCATION)
async def location_handler(msg: types.Message):
    await msg.answer('location qabul qilindi')


@dp.message_handler(content_types=types.ContentTypes.CONTACT)
async def video_handler(msg: types.Message):
    await msg.answer('contact qabul qilindi')


@dp.message_handler(content_types=types.ContentTypes.DOCUMENT)
async def document_handler(msg: types.Message):
    await msg.answer('document qabul qilindi')


#
