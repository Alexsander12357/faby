import asyncio
from colorama import init, Fore
from colorama import Back
from colorama import Style
from aiogram.types import InputFile

import logging
from aiogram import Bot, Dispatcher, types, executor
init(autoreset=True)
logging.basicConfig(level=logging.INFO)
bot = Bot(token="5694672158:AAFV_CTnARdISBdOi-zZuUV2x5XRlaHcAvg")
dp = Dispatcher(bot)
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
greet_markup = ReplyKeyboardMarkup()
button_hi = KeyboardButton("🎒 Расписание уроков🎒")
button_1 = KeyboardButton("🏖Когда каникулы?🏖")
button_2 = KeyboardButton("🍕Меню столовой🍕")
button_3 = KeyboardButton("🎉Школьные события🎉")

greet_markup.add(button_hi)
greet_markup.add(button_1)
greet_markup.add(button_2)
greet_markup.add(button_3)

urlkb=InlineKeyboardMarkup(row_width=1)
urlbutton1=InlineKeyboardMarkup(text='Понедельник', url='https://лицейтехнополис.рф/food/2023-02-06-sm.xlsx')
urlbutton2=InlineKeyboardMarkup(text='Вторник', url='https://лицейтехнополис.рф/food/2023-02-07-sm.xlsx')
urlbutton3=InlineKeyboardMarkup(text='Среда', url='https://лицейтехнополис.рф/food/2023-02-08-sm.xlsx')
urlbutton4=InlineKeyboardMarkup(text='Четверг', url='https://лицейтехнополис.рф/food/2023-02-09-sm.xlsx')
urlbutton5=InlineKeyboardMarkup(text='Пятница', url='https://лицейтехнополис.рф/food/2023-02-10-sm.xlsx')
urlbutton6=InlineKeyboardMarkup(text='4Е', url='https://лицейтехнополис.рф/food/2023-02-11-sm.xlsx')
urlkb.add(urlbutton1,urlbutton2,urlbutton3,urlbutton4,urlbutton5)
inkb = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton(text='1-4', callback_data='fabymi'), InlineKeyboardButton(text='5-11', callback_data='ttt'))
infaby = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton(text='2А', callback_data='ttt'), InlineKeyboardButton(text='2Б', callback_data='ttt'), InlineKeyboardButton(text='2В', callback_data='ttt'), InlineKeyboardButton(text='2Г', callback_data='bbb'), InlineKeyboardButton(text='2Д', callback_data='ttt'))
anfaby = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton(text='4А', callback_data='ttt'), InlineKeyboardButton(text='4Б', callback_data='ttt'), InlineKeyboardButton(text='4В', callback_data='ttt'), InlineKeyboardButton(text='4Г', callback_data='ttt'), InlineKeyboardButton(text='4Д', callback_data='ttt'),InlineKeyboardButton(text='4Е', callback_data='ppp'))
yfaby = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton(text='Понедельник', callback_data='qqq'), InlineKeyboardButton(text='Вторник', callback_data='mmm'), InlineKeyboardButton(text='Среда', callback_data='faby'), InlineKeyboardButton(text='Четверг', callback_data='vvv'), InlineKeyboardButton(text='Пятница', callback_data='xomka'))
faby = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton(text='Понедельник', callback_data='123'), InlineKeyboardButton(text='Вторник', callback_data='456'), InlineKeyboardButton(text='Среда', callback_data='789'), InlineKeyboardButton(text='Четверг', callback_data='000'), InlineKeyboardButton(text='Пятница', callback_data='mi'))
Sports = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton(text='💪Спортивные💪', callback_data='Sportyat'), InlineKeyboardButton(text='🧠Олимпиады🧠', callback_data='Brain'), InlineKeyboardButton(text='🎸Музыкальные🎸', callback_data='Music'), InlineKeyboardButton(text='🦉На эрудицию🦉', callback_data='what'), InlineKeyboardButton(text='🎨Конкурсы 🎨', callback_data='concyrs'), InlineKeyboardButton(text='🎉Праздники🎉', callback_data='parte'), InlineKeyboardButton(text='🎭Другие события🎭', callback_data='all'))
fabymi = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton(text='1', callback_data='ttt'), InlineKeyboardButton(text='2', callback_data='www'),InlineKeyboardButton(text='3', callback_data='ttt') , InlineKeyboardButton(text='4', callback_data='aaa'))



@dp.callback_query_handler(text='fabymi')
async def www_call(callback : types.CallbackQuery):
    await callback.message.answer('"Выберите параллель. Пока доступно расписание только 2 "Г" и 4 "Е" классов".', reply_markup=fabymi)



@dp.message_handler(commands='test')
async def test_commands(message: types.Message):
    await message.answer('Инлайн кнопка', reply_markup=inkb)
@dp.callback_query_handler(text='www')
async def www_call(callback : types.CallbackQuery):
    await callback.message.answer('Выберите класс:', reply_markup=infaby)
@dp.callback_query_handler(text='aaa')
async def www_call(callback : types.CallbackQuery):
    await callback.message.answer('Выберите класс:', reply_markup=anfaby)
@dp.callback_query_handler(text='ttt')
async def www_call(callback : types.CallbackQuery):
    await callback.message.answer('Извините, раздел в разработке')
@dp.callback_query_handler(text='ppp')
async def www_call(callback : types.CallbackQuery):
    await callback.message.answer('Выберите день:', reply_markup=yfaby) #4Е
@dp.callback_query_handler(text='bbb')
async def www_call(callback : types.CallbackQuery):
    await callback.message.answer('Выберите день:', reply_markup=faby) #2Г
@dp.callback_query_handler(text='123')
async def www_call(callback : types.CallbackQuery):
    await callback.message.answer('Понедельник:\n0 урок: 12:50 - 13:30 Классный час \n 1 урок: 13:40 - 14:20 Англ.яз. \n 2 урок: 14:30 - 15:10 Математика \n 3 урок: 15:30 - 16:10 Русский язык \n 4 урок: 16:30 - 17:10 Лит-ра\n 5 урок: 17:30 - 18:10 ИЗО')
@dp.callback_query_handler(text='456')
async def www_call(callback : types.CallbackQuery):
    await callback.message.answer('Вторник:\n 1 урок: 13:40 - 14:20 Математика \n 2 урок: 14:30 - 15:10 Русский язык \n 3 урок: 15:30 - 16:10 Литература \n 4 урок: 16:30 - 17:10 Окр.мир')
@dp.callback_query_handler(text='789')
async def www_call(callback : types.CallbackQuery):
    await callback.message.answer('Среда:\n 1 урок: 13:40 - 14:20 Математика \n 2 урок: 14:30 - 15:10 Физ-ра \n 3 урок: 15:30 - 16:10 Русский язык \n 4 урок: 16:30 - 17:10 Англ.яз \n 5 урок: 17:30 - 18:00 Лит-ра')
@dp.callback_query_handler(text='000')
async def www_call(callback : types.CallbackQuery):
    await callback.message.answer('Четверг:\n1 урок: 13:40 - 14:20 Ритмика \n 2 урок: 14:30 - 15:10 Математика \n 3 урок: 15:30 - 16:10 Русский язык \n 4 урок: 16:30 - 17:10 Информатика')

@dp.callback_query_handler(text='mi')
async def www_call(callback : types.CallbackQuery):
    await callback.message.answer('Пятница:\n 1 урок: 13:40 - 14:20 Окр.мир \n 2 урок: 14:30 - 15:10 Лит-ра \n 3 урок: 15:30 - 16:10 Музыка \n 4 урок: 16:30 - 17:10 Геометрия/Основы смыслового чтения \n 5 урок: 17:30 - 18:10 Технология')
@dp.callback_query_handler(text='qqq')
async def www_call(callback : types.CallbackQuery):
    await callback.message.answer('Понедельник:\n 1 урок: 08:00 - 08:40 Математика \n 2 урок: 08:50 - 09:30 Информатика \n 3 урок: 09:50 - 10:30 Лит-ра \n 4 урок: 10:50 - 11:30 Физ-ра \n5 урок: 10:50 - 11:30 Окружающий мир \n6 урок: 11:50 - 12:30 Классный час')
@dp.callback_query_handler(text='mmm')
async def www_call(callback : types.CallbackQuery):
    await callback.message.answer('Вторник:\n 1 урок: 08:00 - 08:40 Математика \n 2 урок: 08:50 - 09:30 Русский \n 3 урок: 09:50 - 10:30 Англиский \n 4 урок: 10:50 - 11:30 Основы смыслового чтения \n 5 урок: 11:50 - 12:30 ОРКиСЭ/Технология \n 6 урок: 12:50 - 13:30 Доп. Русский')
@dp.callback_query_handler(text='faby')
async def www_call(callback : types.CallbackQuery):
    await callback.message.answer('Среда:\n 1 урок: 08:00 - 08:40 Ритмика \n 2 урок: 08:50 - 09:30 Математика \n 3 урок: 09:50 - 10:30 Русский \n 4 урок: 10:50 - 11:30 Окр. мир')
@dp.callback_query_handler(text='vvv')
async def www_call(callback : types.CallbackQuery):
    await callback.message.answer('Четверг:\n 1 урок: 08:00 - 08:40 Математика \n 2 урок: 08:50 - 09:30 Англиский \n 3 урок: 09:50 - 10:30 Русский \n 4 урок: 10:50 - 11:30 Лит-ра \n 5 урок: 11:50 - 12:30 ИЗО/Музыка/Доп.Математика\n 6 урок: 12:50 - 13:30 Доп. Русский')
@dp.callback_query_handler(text='xomka')
async def www_call(callback : types.CallbackQuery):
    await callback.message.answer('Пятница:\n 1 урок: 08:00 - 08:40 Математика \n 2 урок: 08:50 - 09:30 Англиский \n 3 урок: 09:50 - 10:30 Русский \n 4 урок: 10:50 - 11:30 Лит-ра \n 5 урок: 11:50 - 12:30 Бассейн(по желанию)')
@dp.callback_query_handler(text='Sportyat')
async def www_call(callback : types.CallbackQuery):
    await callback.message.answer('1 февраля: Муниципальный этап областного зимнего фестиваля ВФСК ГТО среди обучающихся IV-V ступеней (в нашем лицее).\n<b>2 февраля</b>: Муниципальный этап областного зимнего фестиваля ВФСК ГТО среди обучающихся IV-V ступеней (в 21 лицее).\n<b>11 февраля</b>: Зональный этап областных соревнований по баскетболу среди обучающихся 6-7 классов ОО НСО - участников проекта Школа- центр ФК и ЗОЖ (в 21 лицее).\n<b>14 февраля</b>:  Соревнования для мальчиков 5-10 классов, посвященные Дню Защитника Отечества (в нашем лицее).\n<b>15 февраля</b>: Веселые старты для учащихся начальных классов, посвященные Дню Защитника Отечества (в нашем лицее).', parse_mode=types.ParseMode.HTML)
@dp.callback_query_handler(text='Brain')
async def www_call(callback : types.CallbackQuery):
    await callback.message.answer('<b>4 февраля</b>: Региональный этап ВСОШ по обществознанию (в НГПУ).\n<b>6 февраля</b>: Региональный этап ВСОШ по английскому языку (в НГПУ).\n<b>7 февраля</b>: Региональный этап ВСОШ по английскому языку, устный (в НГПУ).\n<b>13 февраля</b>: Региональный этап ВСОШ по математике (в НГУ) и Муниципальная олимпиада младших школьников по математике для 3-6 классов  (в 21 лицее).\n<b>14 февраля</b>: Региональный этап ВСОШ по математике (в НГУ)и  Муниципальная олимпиада младших школьников по истории для 5-6 классов  (в нашем лицее).\n<b>15 февраля</b>:  Муниципальная олимпиада младших школьников по русскому языку для 3-6 классов  (в школе №5).\n<b>16 февраля</b>: Муниципальная олимпиада младших школьников по географии для 5-6 классов  (в 21 лицее).\n<b>17 февраля</b>: Муниципальная олимпиада младших школьников по литературе и лит.чтению для 3-6 классов  (в нашем лицее).\n<b>20 февраля</b>: Муниципальная олимпиада младших школьников по биологии и окр.миру для 3-6 классов  (в 21 лицее).\n<b>21 февраля</b>: Муниципальная олимпиада младших школьников по английскому языку для 3-6 классов  (в школе №5).\n<b>22 февраля</b>: Муниципальная олимпиада младших школьников по информатике для 5-6 классов  (в нашем лицее).', parse_mode=types.ParseMode.HTML)
@dp.callback_query_handler(text='Music')
async def www_call(callback : types.CallbackQuery):
    await callback.message.answer('<b>13 февраля</b>: Зимний музыкальный фестиваль обучающихся начальной школы (1 смена), в нашем лицее.\n<b>14 февраля</b>: Зимний музыкальный фестиваль обучающихся начальной школы (2 смена), в нашем лицее.', parse_mode=types.ParseMode.HTML)
@dp.callback_query_handler(text='what')
async def www_call(callback : types.CallbackQuery):
    await callback.message.answer('<b>1 февраля</b>: Квиз для 7х классов, посвящённый 80-летию со дня победы Вооруженных сил СССР над армией гитлеровской Германии в 1943 году в Сталинградской битве (в нашем лицее) и онлайн-игра "Экополис".\n<b>8 и 15 февраля</b>:  онлайн-игра "Экополис".', parse_mode=types.ParseMode.HTML)
@dp.callback_query_handler(text='concyrs')
async def www_call(callback : types.CallbackQuery):
    await callback.message.answer('<b>9 февраля</b>: Школьный этап Всероссийского конкурса юных чтецов Живая классика (в нашем лицее)', parse_mode=types.ParseMode.HTML)
@dp.callback_query_handler(text='parte')
async def www_call(callback : types.CallbackQuery):
    await callback.message.answer('<b>16 и 17 февраля</b>: Масленица (в нашем лицее).\n<b>17 февраля</b>: Яркий день Ряженые (в нашем лицее) и праздник Прощание с Азбукой! для обучающихся 1 классов (в нашем лицее).', parse_mode=types.ParseMode.HTML)
@dp.callback_query_handler(text='all')
async def www_call(callback : types.CallbackQuery):
    await callback.message.answer('<b>2 февраля</b>: "День будущего студента" для 8-9х классов (в нашем лицее).\n<b>11 февраля</b>: в 18:00 спектакль "Двенадцать месяцев" (в нашем лицее)', parse_mode=types.ParseMode.HTML)




@dp.message_handler(commands=["start"])
async def cmd_start(message: types.Message):
    await message.answer("Выберите пункт меню!", reply_markup=greet_markup)
@dp.message_handler()
async def cmd_text(message: types.Message):
    if message.text == "🎒 Расписание уроков🎒":

        await bot.send_message(message.from_user.id, "Выберите параллель:", reply_markup=inkb)
    elif message.text == "🏖Когда каникулы?🏖":

        #await bot.send_message(message.from_user.id, " 1. После 1 модуля: \n🏖10.10.2022-16.10.2022 \n 2. После 2 модуля: \n🏖21.11.2022-27.11.2022 \n 3. После 3 модуля: \n🏖31.12.2022-08.01.2023 \n 4. После 4 модуля: \n🏖20.02.2023-26.02.2023 \n 5. После 5 модуля: \n🏖03.04.2023-09.04.2023 \n 6. После 6 модуля: \n🏖08.06.2023-31.08.2023 ")
        await bot.send_message(message.from_user.id, "🍁10.10.2022-16.10.2022🍁 \n☔21.11.2022-27.11.2022☔\n🎄31.12.2022-08.01.2023🎄\n☃20.02.2023-26.02.2023☃\n🌸03.04.2023-09.04.2023🌸\n🏝08.06.2023-31.08.2023🏝")

    elif message.text == "🍕Меню столовой🍕":
        await message.answer ('Меню на текущую неделю.\nВыберите день:',reply_markup=urlkb)
    elif message.text == "🎉Школьные события🎉":
        await message.reply("Здесь вы узнаете, какие события будут проходить в лицее в феврале.\nНажмите на любую категорию:", reply_markup=Sports)

    else:
        await  bot.send_message(message.from_user.id, 'Извините, данная команда не найдена.')


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
