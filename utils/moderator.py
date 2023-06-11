from aiogram import types


def isLink(message: types.Message):
	entries = [entry for entry in message.entities if entry.type == "url"]
	return True if len(entries) > 0 else False