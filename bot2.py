from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
import datetime
from config import TOKEN

bot = Bot(token=TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

class Form(StatesGroup):
    name = State()
    phone = State()
    rating = State()
    review = State()


@dp.message_handler(commands=['start'])
async def start_proc(message: types.Message):
    text = '''Привет! Здесь можете 
    написать отзыв на пробный урок)
    '''
    text2 = 'Напишите свое имя'
    markup = types.ReplyKeyboardRemove()
    await bot.send_message(message.from_user.id, text)
    await Form.name.set()
    await message.reply(text2, reply_markup=markup)

@dp.message_handler(lambda message: message.text[0] == '/', state=Form.name)
async def invalid_name_proc(message: types.Message, state: FSMContext):
    await message.reply("Имя не может начинатся с символа '/', так как с этого символа начинаются команды телеграм бота")

@dp.message_handler(state=Form.name)
async def name_proc(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
        
    await Form.next()
    await message.reply('Напишите свой номер телефона')

@dp.message_handler(lambda message: not message.text.isdigit(), state=Form.phone)
async def invalid_phone_proc(message: types.Message, state: FSMContext):
    await message.reply('Пожалуйста, напишите вверный формат вашего номера')


@dp.message_handler(lambda message: message.text.isdigit(),state=Form.phone)
async def phone_proc(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['phone'] = message.text
    await Form.next()
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('1', '2', '3','4','5')
    await message.reply('Какую оценку вы поставите?', reply_markup=markup)


@dp.message_handler(lambda message: message.text not in ['1', '2', '3','4','5'], state=Form.rating)
async def invalid_rating(message: types.Message):
    await message.reply('Выберете оценку на кнопках')


@dp.message_handler(lambda message: message.text in ['1', '2', '3','4','5'],state=Form.rating)
async def rating_proc(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['rating'] = message.text
        markup = types.ReplyKeyboardRemove()
    await Form.next()
    await message.reply('Напишите отзыв)', reply_markup=markup)

@dp.message_handler(state=Form.review)
async def review_proc(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['review'] = message.text
    await state.finish()
    text = f"""
    
    Имя: {data['name']}
    Номер: {data['phone']}
    Оценка: {data['rating']}
    Отзыв: {data['review']}
    Спасибо за отзыв!
    """
    current_date_time = datetime.datetime.now()
    current_time = current_date_time.date()
    with open('review.txt', 'a+') as file:
        file.write(f"{current_time}    Имя: {data['name']} Номер: {data['phone']} Оценка: {data['rating']} Отзыв: {data['review']} \n")
    await message.reply(text)




executor.start_polling(dp)
