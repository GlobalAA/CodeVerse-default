from aiogram import types

from dispatcher import dp

from .main_events import on_main_events
from .main_handler import moderate

dp.register_channel_post_handler(
	on_main_events, 
	content_types=[
		types.ContentType.NEW_CHAT_PHOTO, 
		types.ContentType.NEW_CHAT_MEMBERS,
		types.ContentType.LEFT_CHAT_MEMBER,
		types.ContentType.NEW_CHAT_TITLE,
		types.ContentType.DELETE_CHAT_PHOTO,
		types.ContentType.PINNED_MESSAGE,
		types.ContentType.NEW_CHAT_TITLE,
	]
)

dp.register_channel_post_handler(
	moderate, 
	content_types=[
		types.ContentType.TEXT, 
		types.ContentType.VIDEO, 
		types.ContentType.PHOTO
	]
)
