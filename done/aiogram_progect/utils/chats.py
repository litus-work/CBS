from aiogram.types import Message
from utils.exceptions import UserQueueException
from utils.messages import MessageService
from aiogram.fsm.context import FSMContext
from states import ChatState
import random


class ChatService:
    _queue_users: list[dict[str, int | FSMContext]] = []

    @classmethod
    async def _select_companion(cls, user_id: int, user_state: FSMContext) -> bool | int:
        """Find companion for user and set data/states for communication

        Args:
            user_id (int): Telegram id of user  
            user_state (FSMContext): FSM state of user

        Returns:
            bool | int: _description_
        """
        if len(cls._queue_users) > 0:
            companion = random.choice(cls._queue_users)
            await companion["state"].set_state(ChatState.in_chat)
            await companion["state"].set_data(
                {"companion": user_id, "companion_state": user_state}
            )
            await user_state.set_state(ChatState.in_chat)
            await user_state.set_data(
                {"companion": companion["id"], "companion_state": companion["state"]}
            )
            cls._remove_from_queue(companion["id"])
            return companion["id"]
        return False

    @classmethod
    def _remove_from_queue(cls, user_id: int) -> None:
        """Remove user from queuq by user_id

        Args:
            user_id (int): telegram id of user account
        """
        for idx, user in enumerate(cls._queue_users):
            if user["id"] == user_id:
                idx_for_remove = idx
                break
        del cls._queue_users[idx_for_remove]

    @classmethod
    async def add_user(cls, message: Message, state: FSMContext):
        """Add user to search queue and find companion

        Args:
            message (Message): Message which bot recive from user
            state (FSMContext): State of user

        Raises:
            UserQueueException: Raised when user alredy in queue
        """
        user_id = message.from_user.id

        if user_id in cls._queue_users:
            raise UserQueueException
        await message.answer(MessageService.success_add_to_queue(message))
        companion = await cls._select_companion(user_id, state)
        if companion:
            await message.answer(MessageService.success_search(message))
            await message.bot.send_message(
                companion, MessageService.success_search(message)
            )
        else:
            cls._queue_users.append({"id": user_id, "state": state})
            await state.set_state(ChatState.search)

    @classmethod
    async def stop_chat(cls, message: Message, state: FSMContext):
        """Remove user from queue or stop chat session

        Args:
            message (Message): Message which bot recive from user
            state (FSMContext): State of user

        Raises:
            UserQueueException: Raised when user not in queue and not in chat
        """
        user_id = message.from_user.id
        is_not_in_chat = await state.get_state() != ChatState.in_chat
        if user_id not in cls._queue_users and is_not_in_chat:
            raise UserQueueException
        if is_not_in_chat:
            cls._remove_from_queue(user_id)
            await message.answer(MessageService.stop_search(message))
            await state.set_state(ChatState.default)
        else:
            data = await state.get_data()
            await state.clear()
            await data["companion_state"].clear()
            await message.answer(MessageService.stop_chat(message))
