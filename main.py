from os import replace
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
    await bot.send_message(msg.from_user.id, 
    '''Меню бота:
    1. Пройти опрос /opros
    2. Узнать результаты опроса /resopros
    2. Неблагоприятные условия Советского района /causes
    3. Результаты исследований Советсткого района /research
    4. Решение проблем Советского района /solution ''')

@dp.message_handler(commands=['opros'])
async def process_start_command(msg: types.Message):
    await bot.send_message(msg.from_user.id, 
    '''Выберите какое именно решение вы считаете лучшим:
    1. Переезд /moving
    2. Построка тунеля /tunnel
    3. Озеленение /trees''')

@dp.message_handler(commands=['resopros'])
async def process_start_command(msg: types.Message):
    res = get_users()
    count_res = len(res)

    count_moving = 0
    count_tunnel = 0
    count_trees = 0

    for item in res:
        count_moving += 1 if 'Переезд' in item else 0
        count_tunnel += 1 if 'Тунель' in item else 0
        count_trees += 1 if 'Озеленение' in item else 0

    await bot.send_message(msg.from_user.id, 
    '''Результаты голосования:
    За Переезд проголосовало: {} - {}%
    За Строительство тунеля проголосовало: {} - {}%
    За Озеленение проголосовало: {} - {}%
    Всего приняло участие в голосовании - {} человек
    '''.format(
        count_moving, round(count_moving / count_res * 100, 2),
        count_tunnel, round(count_tunnel / count_res * 100, 2),
        count_trees, round(count_trees / count_res * 100, 2),
        count_res))


@dp.message_handler(commands=['moving', 'tunnel', 'trees'])
async def process_start_command(msg: types.Message):
    if msg.text == '/moving':
        set_user({'id': msg.from_user.id, 'choise':'Переезд'})
    elif msg.text == '/tunnel':
        set_user({'id': msg.from_user.id, 'choise':'Тунель'})
    elif msg.text == '/trees':
        set_user({'id': msg.from_user.id, 'choise':'Озеленение'})
    await bot.send_message(msg.from_user.id, '''Спасибо за принятие участие в опросе!''')

@dp.message_handler(commands=['causes'])
async def process_start_command(msg: types.Message):
    await bot.send_message(msg.from_user.id, 
    '''Причины:
    1. Нахождение несоответствия уровня шума и расстояния между жилыми домами и проезжей частью
    2. Большое число экологических проблем Самары и области связаны с повышенной загрязненностью воздуха
                ''')


@dp.message_handler()
async def echo_message(msg: types.Message):
    pass


if __name__ == '__main__':
    executor.start_polling(dp)

