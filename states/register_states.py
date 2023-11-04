from aiogram.dispatcher.filters.state import State, StatesGroup


class RegisterState(StatesGroup):
    fullname = State()
    phone = State()
    email = State()
    age = State()
    confirm = State()
