from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


contact_markup = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Kontaktni yuborish', request_contact=True)],
    ],
    resize_keyboard=True
)
