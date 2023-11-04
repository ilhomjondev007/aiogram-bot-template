from aiogram import types
from aiogram.types import ContentType, ReplyKeyboardRemove

from loader import dp
from keyboards.default import contact_markup


# @dp.message_handler(content_types='contact')
@dp.message_handler(content_types=ContentType.CONTACT)
async def send_contact(msg: types.Message):
    phone = msg.contact.phone_number
    await msg.answer(f"Sizning telingiz: {phone}", reply_markup=ReplyKeyboardRemove())


# @dp.message_handler(content_types='photo')
@dp.message_handler(content_types=[ContentType.PHOTO])
async def send_photo(msg: types.Message):
    await msg.answer('Bu rasm')
    await msg.answer(f"{msg.photo[-1].file_id}")


# @dp.message_handler(content_types='video')
@dp.message_handler(content_types=ContentType.VIDEO)
async def send_photo(msg: types.Message):
    await msg.answer("Bu video")
    await msg.answer(f"{msg.video.file_id}")


# @dp.message_handler(content_types='audio')
@dp.message_handler(content_types=ContentType.AUDIO)
async def send_audio(msg: types.Message):
    await msg.answer("Bu audio")


# @dp.message_handler(content_types='voice')
@dp.message_handler(content_types=ContentType.VOICE)
async def send_audio(msg: types.Message):
    await msg.answer("Bu voice")


# @dp.message_handler(content_types='document')
@dp.message_handler(content_types=ContentType.DOCUMENT)
async def send_audio(msg: types.Message):
    await msg.answer("Bu Document")


