from aiogram import types

from loader import dp, bot


@dp.message_handler(commands=['photo'])
async def send_photo(msg: types.Message):
    with open('data/images/men.jpg', 'rb') as photo:
        pass
        # await msg.answer_photo(photo=photo)
        # await bot.send_photo(msg.from_user.id, photo=photo)
    # await msg.answer_photo(photo='AgACAgIAAxkBAANxZUYv0cmGRMJG33sMCnWu3EAnwgIAAuXOMRsqajBK_wiM1Xlwl8QBAAMCAAN5AAMzBA')
    await msg.answer_photo(photo='https://media.istockphoto.com/id/517188688/photo/mountain-landscape.jpg?s=612x612&w=0&k=20&c=A63koPKaCyIwQWOTFBRWXj_PwCrR4cEoOw2S9Q7yVl8=')


@dp.message_handler(commands=['video'])
async def send_video(msg: types.Message):
    await msg.answer_video(video='BAACAgIAAxkBAAN8ZUYwsI7OgF0M7BURWVd63nr6MP4AAgQ9AAKhV-FJLUkRSAmkCb4zBA')
