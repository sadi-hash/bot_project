from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import datetime
from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def proc_start_command(message: types.Message):
    await bot.send_photo(message.from_user.id, types.InputFile('img/1.jpg'))
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('инфо', 'время')
    await message.reply('Привет! Отправь любой текст', reply_markup=markup)

@dp.message_handler(lambda message: message.text not in ['инфо', 'время'])
async def proc_info_invalid(message: types.Message):
    await message.reply('Выберете одну из кнопок')

@dp.message_handler()
async def proc_info(message: types.Message):
    info = '''
        Этот бот показывает время
    '''
    current_date_time = datetime.datetime.now()
    current_time = current_date_time.time()
    if message.text == 'инфо':
        await message.reply(info)
    elif message.text == 'время':
        await message.reply(str(current_time)[:8])
# @dp.message_handler(commands=['help'])
# async def help_command(message: types.Message):
#     await message.reply('Привет! Отправь любой текст и я это повторю')

# @dp.message_handler()
# async def echo_message(message: types.Message):
#     await bot.send_message(message.from_user.id, message.text)

executor.start_polling(dp)