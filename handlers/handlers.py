from aiogram import Bot, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import logging

import config
from keyboards import keyboards as kb
from converter import get_converted

logging.basicConfig(level=logging.INFO)
storage = MemoryStorage()
bot = Bot(token=config.TG_TOKEN, parse_mode=types.ParseMode.HTML)


async def main_menu_initial(message: types.Message):
    await message.answer_photo(photo='https://disk.yandex.com/i/Aun34vdAb0BNnA',
                               caption='Привет, это бот хелпер для Марьяны, Руслана и Тоши',
                               reply_markup=kb.main_menu_keyboard())


async def main_menu(call: types.CallbackQuery):
    await call.message.edit_caption(
        caption='Привет, это бот хелпер для Марьяны, Руслана и Тоши',
        reply_markup=kb.main_menu_keyboard())
    await call.answer()


async def converter(call: types.CallbackQuery):
    await call.message.edit_caption(caption='''
Выбери валюту и сумму
''',
                                    reply_markup=kb.converter_keyboard(previous_step='main_menu', selected_amount=0,
                                                                       selected_currency=0))
    await call.answer()
