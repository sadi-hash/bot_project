
from aiogram import types
from .keybords import get_cities_keyboards
from service.utlis import get_weather

async def welcome_message(message: types.Message):
    await message.answer("Hello World",reply_markup=get_cities_keyboards())


async def get_city_weather(call: types.CallbackQuery):
   message = call.message
   city = str(call.data).split("_")[1]
   response = await get_weather(city)
   text = f"""
        Название города:{city.title()}
        Температура: {response["temp"]} C
        Чувстуеться как:{response["feels_like"]} C
        Давление:{response["pressure"]} hP
        Скорость ветра:{response["wind_speed"]}m/c
        Влажность:{response["humidity"]}%
        Время:{response["city_time"]}
        Время восхода:{response["sunrise"]}
        Время заката:{response["sunset"]}

     """  
















    
   await message.answer(text)

