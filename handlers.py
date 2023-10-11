from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, \
    ReplyKeyboardRemove

from search import search

class SearchForm(StatesGroup):
    waiting_for_query = State()

async def on_start(message: types.Message):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = [KeyboardButton(text='/search')]
    keyboard.add(*buttons)
    await message.answer("Hello", reply_markup=keyboard)

async def search_form_start(message: types.Message, state: FSMContext):
    await message.answer("Type query searchString")
    await SearchForm.waiting_for_query.set()

async def process_search_query(message: types.Message, state: FSMContext):
    query = message.text
    results = search(query)
    result_text = '\n'.join(map(str, results))
    await message.answer(result_text)
    await state.finish()