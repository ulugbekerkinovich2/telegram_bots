from aiogram import types
from aiogram.dispatcher.filters import Text

from mukammal_bot_paid_db_postgres.loader import dp


@dp.message_handler(Text(contains='location', ignore_case=True))
async def text_example(msg: types.Message):
    await msg.reply_location(41.25848505118257, 69.2206991550083)


@dp.message_handler(Text(contains='salom-', ignore_case=True))
async def text_example(msg: types.Message):
    await msg.reply_photo(
        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT52viIJLNCM7XNd6asRrhDlLjjPhLW4Z_jgQ&usqp=CAU",
        disable_notification=True,
        caption='<b>hello galaxy</b>', parse_mode='HTML')


@dp.message_handler(Text(contains='video', ignore_case=True))
async def text(msg: types.Message):
    await msg.reply_video(
        "https://assets.mixkit.co/videos/preview/mixkit-forest-stream-in-the-sunlight-529-large.mp4", 35,
        caption='nature',
    )

