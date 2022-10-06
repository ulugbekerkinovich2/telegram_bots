from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

#
true_false_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Ha'),
            KeyboardButton(text="Yo'q"),
        ],

    ], resize_keyboard=True  # button hajmii tog'irlaydi
    , one_time_keyboard=True

)
