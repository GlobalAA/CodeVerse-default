import os
from uuid import uuid4

from aiogram import types
from better_profanity import profanity

from dispatcher import bot


async def on_message(message: types.Message):
	allowed_chat_type = "private"
	if message.chat.type == allowed_chat_type:
		if not (message.from_user.id == int(os.getenv("OWNER_ID"))) and message.content_type == types.ContentType.PHOTO:
			caption = message.caption if message.caption != None else None

			if not caption:
				return await message.reply("У вашего изображения должно быть описание!")

			photo = message.photo[-1]
			file_name = f'photos/{uuid4()}.jpg'
			await photo.download(destination_file=file_name)

			photo = open(file_name, "rb")

			send_button = types.InlineKeyboardButton("📨", callback_data=f"send photo {file_name} {caption}")
			keyboard = types.InlineKeyboardMarkup().add(send_button)
			await bot.send_photo(int(os.getenv("OWNER_ID")), photo, caption=caption, reply_markup=keyboard)

			os.remove(file_name)

		elif not (message.from_user.id == int(os.getenv("OWNER_ID"))) and message.content_type == types.ContentType.TEXT:
			profanity.load_censor_words_from_file("wordlist.txt")
			if profanity.contains_profanity(message.text):
				return await message.answer("Ваше сообщение содержит ненормативную лексику!")
			else:
				await bot.send_message(int(os.getenv("OWNER_ID")), message.text)

async def send_to_channel(callback_query: types.CallbackQuery):
	photo_path = callback_query.data.split()[-2]
	caption = callback_query.data.split()[-1]
	chat_id = os.getenv("CHAT_ID")
	await callback_query.message.photo[-1].download(destination_file=photo_path)

	try:
		photo = open(photo_path, "rb")
		await bot.send_photo(chat_id, photo, caption=caption)
		os.remove(photo_path)
	except FileNotFoundError as e:
		print(e)
