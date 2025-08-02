from aiogram.fsm.state import State, StatesGroup


class ChatState(StatesGroup):
    default = State()
    search = State()
    in_chat = State()
