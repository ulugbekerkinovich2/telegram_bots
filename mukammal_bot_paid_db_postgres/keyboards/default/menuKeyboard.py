from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

#
menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Sherik kerak'),
            KeyboardButton(text='Ish joyi kerak'),

        ],
        [
            KeyboardButton(text="Hodim kerak"),
            KeyboardButton(text='Ustoz kerak'),

        ],
        [
            KeyboardButton(text='Shogird kerak'),

        ],
        [
            KeyboardButton(text="Bog'lanish"),
            KeyboardButton(text="anketa")

        ],

    ], resize_keyboard=True  # button hajmii tog'irlaydi
    , one_time_keyboard=True

)
