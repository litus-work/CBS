from aiogram.fsm.state import State, StatesGroup

class MenuStates(StatesGroup):
    choosing_city = State()
    waiting_for_location = State()
    showing_now = State()
    showing_hourly = State()
    showing_daily = State()