import os

from aiogram import types

from dispatcher import bot
from utils.moderator import isLink


async def moderate(message: types.Message):
	text = message.text or message.caption
	if isLink(message):
		await message.delete()
		await bot.send_message(os.getenv("OWNER_ID"), f'В канал была отправлена неверная ссылка! {text}')