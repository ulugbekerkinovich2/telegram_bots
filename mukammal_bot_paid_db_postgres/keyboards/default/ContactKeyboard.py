from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

#
contact = ReplyKeyboardMarkup(
    keyboard=[

        [
            KeyboardButton(text="Admin bilan bog'lanish"),
            # KeyboardButton(text="Bot yaratuvchisi bilan bog'lanish"),

        ],
        # [
        #     KeyboardButton(text="contact", request_contact=True),
        #     KeyboardButton(text="location", request_location=True)
        # ],
        [
            KeyboardButton(text="<<Ortga")
        ]

    ], resize_keyboard=True  # button hajmii tog'irlaydi
    , one_time_keyboard=False

)
