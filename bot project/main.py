
from aiogram import executor
from bot_router import bot_dispatcher


if __name__ == "__main__":
    executor.start_polling(bot_dispatcher,skip_updates=True)
