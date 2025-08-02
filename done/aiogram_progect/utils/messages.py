from aiogram.types import Message
from aiogram import html


class MessageService:
    """Service wich save all messages texts

    """


    @classmethod
    def hello(cls, message: Message):
        return f"Привіт, {message.from_user.full_name}. Напиши {html.bold('/start_chat')} щоб знайти співрозмовника"

    @classmethod
    def alredy_in_queue(cls, message: Message):
        return f"Ви вже знаходитесь в чержі очікуйте на підключення другого користувач"
    
    @classmethod
    def success_add_to_queue(cls, message: Message):
        return f"Вас додано в чергу очікуйте на другого користувача для того щоб припинити пошук введіть /stop_chat"
    
    @classmethod
    def user_not_in_queue(cls, message: Message):
        return f"Ви не можете зупитини чат так як не починали його напишіть /start_chat"
    
    @classmethod
    def stop_search(cls, message: Message):
        return f"Ви зупинили пошук"
    
    @classmethod
    def in_search(cls, message: Message):
        return f'Очікуйте ми шукаємо вам співрозмовника'
    
    @classmethod
    def success_search(cls, message: Message):
        return f'Вашого співрозмовника знайдено'
    
    @classmethod
    def stop_chat(cls, message: Message):
        return f'Розмову завершено'