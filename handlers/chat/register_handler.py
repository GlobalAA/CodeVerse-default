from aiogram import types

from dispatcher import dp

from .main_handler import on_message, send_to_channel, start_command

dp.register_message_handler(start_command, commands=["start"])

dp.register_message_handler(on_message, content_types=[types.ContentType.PHOTO, types.ContentType.TEXT])

dp.register_callback_query_handler(send_to_channel, lambda c: c.data.startswith('send'), is_admin=True)