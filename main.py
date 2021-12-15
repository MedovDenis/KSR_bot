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
    1. Пройти опрос /vote
    2. Узнать результаты опроса /resvote
    2. Возможные неблагоприятные условия на улицах города /causes
    3. Результаты исследований Советсткого района /research
    4. Решение проблем Советского района /solution 
    5. Умный город /smartcity''')

@dp.message_handler(commands=['smartcity'])
async def process_start_command(msg: types.Message):
    photo = [InputMediaPhoto(InputFile('photos/photo11.jpg'))]
    
    await bot.send_message(msg.from_user.id, '''По мнению экспертов, в ближайшем будущем упор будет сделан на экологию — набирают популярность установки, контролирующие уровень грунтовых вод, загрязнения воздуха, сейсмической активности и другие. В стандарт «Умного города» включены такие проекты, как: автоматизация системы управления обращением с твердыми коммунальными отходами, система онлайн-мониторинга воздуха, система онлайн-мониторинга воды. Инженерно-технические подсистемы города Самара и умные решения:
    - Охрана окружающей среды;
    - ГИС для мониторинга состояния окружающей среды;
    - Системы мониторинга предельных выбросов;
    - Робототехника для проведения измерений;
    - Зеленые технологии. Системы снижающие выбросы СО2 и вредных веществ.''')
    await bot.send_media_group(msg.from_user.id, photo)
   
@dp.message_handler(commands=['research'])
async def process_start_command(msg: types.Message):
    photo1 = [InputMediaPhoto(InputFile('photos/photo1.1.jpg')), InputMediaPhoto(InputFile('photos/photo1.2.jpg'))]
    photo2 = [InputMediaPhoto(InputFile('photos/photo2.1.jpg')), InputMediaPhoto(InputFile('photos/photo2.2.jpg'))]
    photo3 = [InputMediaPhoto(InputFile('photos/photo3.1.jpg')), InputMediaPhoto(InputFile('photos/photo3.2.jpg'))]
    photo4 = [InputMediaPhoto(InputFile('photos/photo4.1.jpg')), InputMediaPhoto(InputFile('photos/photo4.2.jpg'))]
    photo5 = [InputMediaPhoto(InputFile('photos/photo5.jpg'))]
    photo6 = [InputMediaPhoto(InputFile('photos/photo6.1.jpg')), InputMediaPhoto(InputFile('photos/photo6.2.jpg')), InputMediaPhoto(InputFile('photos/photo6.3.jpg'))]

    await bot.send_message(msg.from_user.id, 'Участок автодороги и трамвайных путей на ул. Антонова-Овсеенко г. Самара')
    await bot.send_media_group(msg.from_user.id, photo1)
    await bot.send_message(msg.from_user.id, 'Участок автодороги на ул. Карбышева г. Самара')
    await bot.send_media_group(msg.from_user.id, photo2)
    await bot.send_message(msg.from_user.id, 'Участок автодороги на ул. Мориса-Тореза г. Самара')
    await bot.send_media_group(msg.from_user.id, photo3)
    await bot.send_message(msg.from_user.id, 'Участок автодороги на ул. Свободы г. Самара')
    await bot.send_media_group(msg.from_user.id, photo4)
    await bot.send_message(msg.from_user.id, 'Уровни шума на улицах Советского района')
    await bot.send_media_group(msg.from_user.id, photo5)
    await bot.send_message(msg.from_user.id, 'Данные с измерениями уровня шума и расстояний от трамвайных линий до линии жилых домов на улице Ивана Булкина')
    await bot.send_media_group(msg.from_user.id, photo6)

@dp.message_handler(commands=['solution'])
async def process_start_command(msg: types.Message):
    photo1 = [InputMediaPhoto(InputFile('photos/photo7.jpg'))]
    photo2 = [InputMediaPhoto(InputFile('photos/photo8.1.jpg')), InputMediaPhoto(InputFile('photos/photo8.2.jpg'))]
    photo3 = [InputMediaPhoto(InputFile('photos/photo9.1.jpg')), InputMediaPhoto(InputFile('photos/photo9.2.jpg'))]

    await bot.send_message(msg.from_user.id, 
    '''1. Посадка деревьев, в частности. 
Плюсы данного вариант:
    a. Снижение шума от близлежащей дороги;
    b. Озеленение города;
    c. Обогащение города кислородом;
Минусы данного варианта:
    a. Чтобы деревья выросли необходимо достаточно много времени;
    b. На деревья будет оставаться пыль, которая может способствовать развитию болезней и/или аллергии;''')
    await bot.send_media_group(msg.from_user.id, photo1)
    await bot.send_message(msg.from_user.id, 
    '''2. Строительство защитных конструкций (тоннелей), полностью ограждающих проезжую часть. 
Плюсы данного варианта:
    a. Проезжая часть будет полностью скрыта в местах близкого расположения к жилым домам;
    b. Шум от транспортных средств будет заглушатся специальным материалом, которым тоннель будет покрыт изнутри;
Минусы данного варианта:
    a. Долгое по времени строительство;
    b. Потребуется большое количество денежных средств;
    c. Переселение жителей и строительство нового района, находящегося далеко от проезжей части.''')
    await bot.send_media_group(msg.from_user.id, photo2)
    await bot.send_message(msg.from_user.id, 
    '''3. Сейчас за «Амбаром» растет новый жилой район на 50 тысяч человек. В «Южном Городе» появились необычные и новые дизайны многоэтажных домов, также изменится высота небоскребов, что является шагом к развитию. Благодаря прозрачным дверям повышается уровень безопасности.
В Самаре должны забыть о коммунальных авариях, об отключениях горячей воды. Данные изменения произойдут благодаря проекту проект альткотельной, который позволит поставщику энергоресурсов в кратчайшие сроки выполнить перекладку теплосетей, заменить трубы, чтобы ни осенью, ни зимой никаких прорывов в городе не было.
Так же в «Южном Городе» развивается концепция жилого района «Центральный Парк». Данная концепция направлена на выявление и развитие средового потенциала этого соседства. Основные принципы проекта:
    - приватные пространства жилых дворов замкнутые, квартального типа, без доступа автотранспорта, кроме спецтехники;
    - часть улиц, выходящих к парку – пешеходные;
    - жилые кварталы, непосредственно выходящие к парку, разомкнуты и визуально объединены с рекреационной зоной;
    - пограничная линия селитьбы и парка оборудована полосой беседок-пергол, которая обеспечивает плавность перехода пространств многолюдных общественных улиц и приватных дворов к зеленой зоне парка;
    - дополнительные пешеходные связи, проложенные через селитебную зону, позволяют связать кратчайшими путями общественные здания и рекреационные районы, предусмотренные в других очередях строительства в единую систему пешеходного каркаса.''')
    await bot.send_media_group(msg.from_user.id, photo3)

@dp.message_handler(commands=['vote'])
async def process_start_command(msg: types.Message):
    await bot.send_message(msg.from_user.id, 
    '''Выберите какое решение вы считаете лучшим:
    1. Переезд /moving
    2. Построка тунеля /tunnel
    3. Озеленение /trees''')

@dp.message_handler(commands=['resvote'])
async def process_start_command(msg: types.Message):
    res = get_users()
    count_res = len(res) - 7

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
    await bot.send_message(msg.from_user.id, '''Спасибо за принятие участия в опросе!''')

@dp.message_handler(commands=['causes'])
async def process_start_command(msg: types.Message):
    photo = [InputMediaPhoto(InputFile('photos/photo10.jpg'))]
    await bot.send_message(msg.from_user.id, 
    '''Причины:
    1. Нахождение несоответствия уровня шума и расстояния между жилыми домами и проезжей частью
    2. Большое число экологических проблем Самары и области связаны с повышенной загрязненностью воздуха
    3. Благодаря прогрессивной урбанизации уменьшается относительная доля зеленых насаждений в зоне города. При этом сокращается фильтрация воздуха и как следствие увеличивается риск для здоровья людей. В этом случае может помочь увеличение существующих зеленых зон и правильное их содержание.
Еще более эффективный метод по минимизации шумового загрязнения окружающей среды – введение серьёзных штрафов для владельцев «высокотоксичных» машин.
При повышенном загрязнении атмосферного воздуха, вызванной неблагоприятными метеорологическими условиями, с целью предупреждения ухудшения состояния здоровья населения, обострения сердечно-сосудистых, легочных и прочих хронических заболеваний, следует уделять внимание профилактическим мероприятиям, ограничивающим поступление в организм вредных веществ, жителям рекомендуется уделять особое внимание профилактическим мероприятиям, ограничивающим поступление в организм вредных химических веществ:
        - ограничить поездки на личном транспорте, который в данный период дает наибольший вклад в загрязнение воздуха;
        - сократить время пребывания на открытом воздухе, особенно вблизи автотрасс или других источников загрязнения;
        - не открывать для проветривания помещений окна, особенно ночью и ранним утром;
        - ограничить физическую нагрузку на открытом воздухе;
        - занятие физкультурой и спортом проводить в закрытых спортивных комплексах;
        - выезжать на отдых в загородную зону;
        - не допускать сжигание отходов и мусора.''')
    await bot.send_media_group(msg.from_user.id, photo)


@dp.message_handler()
async def echo_message(msg: types.Message):
    pass


if __name__ == '__main__':
    executor.start_polling(dp)

