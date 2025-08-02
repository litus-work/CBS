import asyncio
from aiogram.client.default import DefaultBotProperties
from aiogram.filters import CommandStart
from aiogram.types import Message
import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from config import TELEGRAM_TOKEN
from utils.messages import MessageService
from utils.logger import logger
from services.openweather import OpenWeatherClient
from utils.exceptions import CityNotFoundError, WeatherBotError
from states.weather import WeatherStates
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from aiogram import Router
from keyboards.main import main_menu_keyboard
from states.menu import MenuStates
from aiogram import F
from aiogram.fsm.storage.memory import MemoryStorage
from datetime import datetime
from aiogram.utils.markdown import hbold



load_dotenv()

storage = MemoryStorage()

dp = Dispatcher(storage=storage)
router = Router()
dp.include_router(router)


@router.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext) -> None:
    await message.answer(
        MessageService.hello(),
        reply_markup=main_menu_keyboard()
    )
    await state.clear()

@router.callback_query(F.data == "select_city")
async def on_select_city(callback: CallbackQuery, state: FSMContext):
    await state.set_state(MenuStates.choosing_city)
    await callback.message.answer("📝 Введіть назву міста або надішліть геолокацію 📍")
    await callback.answer()

@router.callback_query(F.data == "weather_now")
async def on_weather_now(callback: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    logger.info(f"[FSM] Состояние: {data}")
    city = data.get("city")
    location = data.get("location")

    if not city and not location:
        await callback.message.answer("❗ Спочатку оберіть місто або надішліть геолокацію 📍")
        await callback.answer()
        return

    try:
        async with OpenWeatherClient() as weather:
            if location:
                lat, lon = location
                data = await weather.get_current_by_coords(lat, lon)
            else:
                data = await weather.get_current(city)
    except WeatherBotError as e:
        await callback.message.answer(f"⚠️ Помилка: {e}")
        await callback.answer()
        return

    temp_day = data["current"]["temp"]
    temp_night = data["daily"][0]["temp"]["night"]
    clouds = data["current"]["clouds"]
    pop = round(data["daily"][0]["pop"] * 100)
    desc = data["current"]["weather"][0]["description"].capitalize()

    message = (
        f"🌤 <b>Погода зараз у {data['name']}:</b>\n"
        f"🌡 Температура: {temp_day}°C вдень, {temp_night}°C вночі\n"
        f"☁️ Хмарність: {clouds}%\n"
        f"🌧 Ймовірність опадів: {pop}%\n"
        f"📌 {desc}"
    )

    await callback.message.answer(message)
    await callback.answer()

@router.message(MenuStates.choosing_city)
async def on_city_text(message: Message, state: FSMContext):
    city = message.text.strip()
    await state.update_data(city=city)
    logger.info(f"[FSM] Сохраняем город: {city}")
    await message.answer(f"✅ Місто встановлено: {city}", reply_markup=main_menu_keyboard())
    await state.set_state(None)

@router.message(F.location)
async def on_location(message: Message, state: FSMContext):
    loc = message.location
    await state.update_data(location=(loc.latitude, loc.longitude))
    await message.answer("✅ Геолокація отримана!", reply_markup=main_menu_keyboard())
    await state.set_state(None)

@router.callback_query(F.data == "weather_hourly")
async def on_weather_hourly(callback: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    city = data.get("city")
    location = data.get("location")

    if not city and not location:
        await callback.message.answer("❗ Спочатку оберіть місто або надішліть геолокацію 📍")
        await callback.answer()
        return

    try:
        async with OpenWeatherClient() as weather:
            if location:
                lat, lon = location
                data = await weather.get_current_by_coords(lat, lon)
            else:
                data = await weather.get_current(city)
    except WeatherBotError as e:
        await callback.message.answer(f"⚠️ Помилка: {e}")
        await callback.answer()
        return

    hourly = data.get("hourly", [])[:6]
    name = data["name"]
    lines = [f"⏰ <b>Щогодинний прогноз у {name}:</b>\n"]

    for hour in hourly:
        ts = datetime.fromtimestamp(hour["dt"])
        time_str = ts.strftime("%H:%M")
        temp = hour["temp"]
        desc = hour["weather"][0]["description"].capitalize()
        clouds = hour["clouds"]
        pop = round(hour.get("pop", 0) * 100)

        lines.append(
            f"{time_str} — {temp}°C, {desc}, ☁️ {clouds}% хмар, 🌧 {pop}% опадів"
        )

    await callback.message.answer("\n".join(lines))
    await callback.answer()



async def main() -> None:
    bot = Bot(TELEGRAM_TOKEN, default=DefaultBotProperties(parse_mode="HTML"))
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(main())