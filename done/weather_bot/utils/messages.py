class MessageService:

    @classmethod
    def hello(cls) -> str:
        return (
            "👋 Вітаю! Я можу показати прогноз погоди.\nОбери опцію нижче 👇"

        )

    @classmethod
    def help(cls) -> str:
        return (
            "Щоб отримати поточну погоду, введіть назву міста латиницею або кирилицею.\n"
            "Приклад: `Kyiv` або `Київ`."
        )

    @classmethod
    def city_not_found(cls, city: str) -> str:
        return f"🔍 На жаль, не знайшов погоду для \"{city}\". Спробуйте іншу назву."