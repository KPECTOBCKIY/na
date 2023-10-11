import aiogram
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import ParseMode
from aiogram.utils import executor

from handlers import (
    on_start,
    search_form_start,
    process_search_query,
    SearchForm,
)

API_TOKEN = '6648964856:AAEl3d48O2kL71dxEpFrK8CAgL2Oy9kLkoY'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Register handlers
dp.register_message_handler(on_start, commands=['start'])
dp.register_message_handler(
    search_form_start, commands=['search'], state='*'
)
dp.register_message_handler(
    process_search_query,
    state=SearchForm.waiting_for_query,
    content_types=types.ContentType.TEXT,
)
