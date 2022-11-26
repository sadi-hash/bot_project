# bot_router это файл марщрцтизатор который перенопровляет и активирует 
# определенные команды.
from aiogram import Bot, Dispatcher
from config import TOKEN
from message_hendlers.hendlers import welcome_message, get_city_weather
from aiogram.dispatcher.filters import Text



bot = Bot(TOKEN)

bot_dispatcher = Dispatcher(bot)

# message handlers
bot_dispatcher.register_message_handler(welcome_message, commands=["start"])

# callback handlerrs
  
bot_dispatcher.register_callback_query_handler(
    get_city_weather,
    lambda call: str(call.data).startswith("city") 
    )
 



