from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.types.input_media import InputMediaPhoto
from aiogram.utils import executor
from aiogram.types.input_file import InputFile

from usersdb import *

TOKEN = '659227635:AAGRnR26NQi877H2_6dVk0W9Ci6df8Lpy4E'

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def process_start_command(msg: types.Message):
    await bot.send_message(msg.from_user.id, 'Привет Машка!!!))')

@dp.message_handler(commands=['get_users'])
async def process_start_command(msg: types.Message):
    users = get_users()
    await bot.send_message(msg.from_user.id, users)


@dp.message_handler()
async def echo_message(msg: types.Message):
    pass


if __name__ == '__main__':
    executor.start_polling(dp)

