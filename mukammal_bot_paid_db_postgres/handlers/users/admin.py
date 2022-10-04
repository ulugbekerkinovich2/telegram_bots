import asyncio

from aiogram import types

from mukammal_bot_paid_db_postgres.data.config import ADMINS
from mukammal_bot_paid_db_postgres.loader import dp, db, bot





@dp.message_handler(text="/rek", chat_id=ADMINS)
async def send_ad_to_all(message: types.Message):
    users = await db.select_all_users()
    for user in users:
        print(user[3])
        user_id = user[3]
        await bot.send_message(chat_id=user_id, text="Assalomu hush kelibsiz qadrli foydalanuvchi \n@status_py_developer adminga murojat qiling!")
        # await asyncio.sleep(0.05)


@dp.message_handler(text="/allusers", user_id=ADMINS)
async def get_allusers(message: types.Message):
    get_user = await db.select_all_users()
    try:
        k = len(get_user)
        for i in get_user:
            user_id = i[0]
            user_name = i[1]
            user_nick = i[2]

            # print(user_id, i)
            await bot.send_message(chat_id=ADMINS[0],
                                   text=f'<b>{user_id}</b>' '.' f"<b>  {user_name}</b>" f"  @{user_nick} ",
                                   parse_mode='HTML')
        await bot.send_message(chat_id=ADMINS[0], text=f"\n{k} ta user mavjud")
    except:
        await bot.send_message(chat_id=ADMINS[0], text="foydalanuvchilar o'chirilgan")


@dp.message_handler(text="/delete_users", user_id=ADMINS)
async def delete_users(message: types.Message):
    await db.delete_users()
    await bot.send_message(chat_id=ADMINS[0], text="foydalanuvchilar o'chirildi")


@dp.message_handler(text='/count_user', user_id=ADMINS)
async def count_user(message: types.Message):
    count = await db.count_users()
    await bot.send_message(chat_id=ADMINS, text=f"{count}")
    await bot.send_message(chat_id=ADMINS, text="shu")


@dp.message_handler(text='/count')
async def count__users(message: types.Message):
    count = await db.count_users()
    print(count)

    await bot.send_message(chat_id=ADMINS, text=count)


@dp.message_handler(text='/allanketa')
async def select_anketa(message: MemoryError):
    all_anketa = await db.select_anketa()
    print(all_anketa)
    await bot.send_message(chat_id=ADMINS[0], text=all_anketa)
