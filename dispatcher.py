import logging
import os

import dotenv
from aiogram import Bot, Dispatcher

from filters.is_admin import IsAdminFilter

dotenv.load_dotenv()

logging.basicConfig(level=logging.INFO)

bot = Bot(token=os.getenv("BOT_TOKEN"), parse_mode="HTML")
dp = Dispatcher(bot)

dp.filters_factory.bind(IsAdminFilter)