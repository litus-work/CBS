import asyncio
import logging
import sys
import os
from dotenv import load_dotenv

from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from utils import MessageService, ChatService, UserQueueException
from aiogram.fsm.context import FSMContext
from states import ChatState

load_dotenv()

TOKEN = os.environ.get("BOT_TOKEN")

dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message, state: FSMContext) -> None:
    """Handler of /start  command

    Args:
        message (Message): Message which bot recive from user
        state (FSMContext): State of user
    """
    await message.answer(MessageService.hello(message))


@dp.message(Command("start_chat"))
async def start_chat(message: Message, state: FSMContext) -> None:
    try:
        await ChatService.add_user(message, state)
    except UserQueueException:
        await message.answer(MessageService.alredy_in_queue(message))


@dp.message(Command("stop_chat"))
async def stop_chat(message: Message, state: FSMContext) -> None:
    try:
        await ChatService.stop_chat(message, state)
    except UserQueueException:
        await message.answer(MessageService.user_not_in_queue(message))


@dp.message(ChatState.search)
async def in_search_message(message: Message, state: FSMContext) -> None:
    await message.answer(MessageService.in_search(message))


@dp.message(ChatState.in_chat)
async def send_to_companion(message: Message, state: FSMContext) -> None:
    data = await state.get_data()
    companion_id = data["companion"]
    await message.copy_to(companion_id)


async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
