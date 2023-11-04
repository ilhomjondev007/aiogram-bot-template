import json

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ContentType, ReplyKeyboardRemove

from keyboards.default import contact_markup
from keyboards.inline import confirm_markup, confirm_callback_data
from loader import dp
from states import RegisterState


@dp.message_handler(commands=['register'])
async def register(msg: types.Message, state: FSMContext):
    await msg.answer("Ismingizni yuboring: ")
    await RegisterState.fullname.set()
    # await state.set_state(RegisterState.fullname)


@dp.message_handler(state=RegisterState.fullname)
async def send_fullname(msg: types.Message, state: FSMContext):
    fullname = msg.text
    await state.update_data({'fullname': fullname})
    await msg.reply("Telefon raqamingizni yuboring:", reply_markup=contact_markup)
    await RegisterState.next()


@dp.message_handler(state=RegisterState.phone, content_types=ContentType.CONTACT)
async def send_contact(msg: types.Message, state: FSMContext):
    phone = msg.contact.phone_number
    await state.update_data({'phone': phone})
    await msg.reply("Emailni yuboring: ", reply_markup=ReplyKeyboardRemove())
    await RegisterState.next()


@dp.message_handler(state=RegisterState.email)
async def send_email(msg: types.Message, state: FSMContext):
    email = msg.text
    await state.update_data({'email': email})
    await msg.answer("Yoshingizni kiriting: ")
    await RegisterState.next()


@dp.message_handler(state=RegisterState.age)
async def send_age(msg: types.Message, state: FSMContext):
    age = msg.text
    await state.update_data({'age': age})
    async with state.proxy() as data:
        fullname = data.get('fullname')
        phone = data['phone']
        email = data['email']
    info = f"Sizni ma'lumotlaringiz:\n" \
           f"Ismingiz: {fullname}\n" \
           f"Tel: {phone}\n" \
           f"email: {email}\n" \
           f"Yoshingiz: {age}"

    await msg.answer(info, reply_markup=confirm_markup)
    await RegisterState.next()


@dp.callback_query_handler(confirm_callback_data.filter(), state=RegisterState.confirm)
async def confirm_register(call: types.CallbackQuery, callback_data: dict, state: FSMContext):
    if callback_data.get('type') == 'yes':
        async with state.proxy() as data:
            data_user = {
                'fullname': data.get('fullname'),
                'phone': data['phone'],
                'email': data['email'],
                'age': data['age']
            }
        try:
            with open('data/users.json', 'r') as file:
                data_all = json.load(file)
                data_all.append(data_user)
            with open('data/users.json', 'w') as file:
                json.dump(data_all, file)
        except:
            with open('data/users.json', 'w') as file:
                data_all = list()
                data_all.append(data_user)
                json.dump(data_all, file)
        await call.answer("Saqlandi!", show_alert=True)
        await call.message.delete()
    elif callback_data.get('type') == 'no':
        await call.message.answer('Ma\'lumotlarni qaytadan kiriting,\n'
                                  'Ismini kiriting: ')
        await call.message.delete()
        await RegisterState.first()
        return
    await state.finish()
