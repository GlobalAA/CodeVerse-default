from aiogram import types


async def on_main_events(message: types.Message):
	await message.delete()