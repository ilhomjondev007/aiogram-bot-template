from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData

confirm_callback_data = CallbackData('confirm_register', 'type')


confirm_markup = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='✅', callback_data=confirm_callback_data.new(type='yes')),
            InlineKeyboardButton(text='🖊', callback_data=confirm_callback_data.new(type='no'))
        ],
    ],
)
