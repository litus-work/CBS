from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def main_menu_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="📍 Обрати місто", callback_data="select_city")],
        [InlineKeyboardButton(text="🌤 Погода зараз", callback_data="weather_now")],
        [InlineKeyboardButton(text="⏰ Щогодинний прогноз", callback_data="weather_hourly")],
        [InlineKeyboardButton(text="📅 Прогноз на 10 днів", callback_data="weather_daily")]
    ])