from aiogram import types


def get_cities_keyboards():
    markup=types.InlineKeyboardMarkup(row_width=2)
    buttons = [
        types.InlineKeyboardButton("Бишкек", callback_data="city_bishkek"),
        types.InlineKeyboardButton("Берлин", callback_data="city_berlin"),
        types.InlineKeyboardButton("Сеул", callback_data="city_seoul"),
        types.InlineKeyboardButton("Лондон", callback_data="city_london"),

    ]

    markup.add(*buttons)
    return markup