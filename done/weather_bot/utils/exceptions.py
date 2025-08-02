class WeatherBotError(Exception):
    """Базовий клас винятків бота."""


class CityNotFoundError(WeatherBotError):
    """Місто не знайдено в OpenWeatherMap."""