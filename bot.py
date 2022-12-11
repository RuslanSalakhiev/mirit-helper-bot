from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import logging
import asyncio
import datetime
import requests
import json

import config
from converter import get_converted
from handlers import handlers as hd

storage = MemoryStorage()
bot = Bot(token=config.TG_TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot, storage=storage)

dp.register_message_handler(hd.main_menu_initial, commands=['Start'])
dp.register_callback_query_handler(hd.converter,
                                   lambda call: call.data in ('converter'))
dp.register_callback_query_handler(hd.main_menu,
                                   lambda call: call.data in ('navi_main_menu'))


# отправка сообщений в технический канал
def send_to_channel(chat_id: int, text: str = None, keyboard: bool = False):
    executor.start(dp, send_message(chat_id, text))
    return


async def send_message(channel_id: int, text: str):
    await bot.send_message(channel_id, text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
