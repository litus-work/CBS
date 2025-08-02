from __future__ import annotations
import httpx
from typing import Any, TypedDict
from utils.exceptions import CityNotFoundError, WeatherBotError
from config import OPENWEATHER_TOKEN

__all__ = [
    "OpenWeatherClient",
]


class _GeoResponse(TypedDict):
    lat: float
    lon: float
    name: str


class OpenWeatherClient:


    GEO_URL = "https://api.openweathermap.org/geo/1.0/direct"
    ONECALL_URL = "https://api.openweathermap.org/data/3.0/onecall"

    def __init__(self, token: str | None = None) -> None:
        self._token = token or OPENWEATHER_TOKEN
        if self._token is None:
            raise RuntimeError("OPENWEATHER_TOKEN не заданий або порожній")
        self._client: httpx.AsyncClient | None = None



    async def get_current(self, city: str, lang: str = "ua", units: str = "metric") -> dict[str, Any]:
        """Повернути блок *current* із One Call API.

        :param city: назва населеного пункту (Kyiv, Київ …)
        :param lang: мова опису погоди
        :param units: одиниці (metric, imperial, standard)
        :raises CityNotFoundError: якщо геокодування не знаходить місто
        :raises WeatherBotError: інші помилки API / мережі
        """
        client = await self._client_or_create()
        geo_params = {
            "q": city,
            "limit": 1,
            "appid": self._token,
        }
        try:
            geo_resp = await client.get(self.GEO_URL, params=geo_params)
        except httpx.HTTPError as exc:
            raise WeatherBotError("Помилка мережі під час геокодування") from exc

        if geo_resp.status_code == 404 or not geo_resp.json():
            raise CityNotFoundError(city)
        if geo_resp.status_code >= 400:
            raise WeatherBotError(f"Помилка геокодування: {geo_resp.text}")

        geo_data: list[_GeoResponse] = geo_resp.json()
        coords = geo_data[0]
        lat, lon = coords["lat"], coords["lon"]
        weather_params = {
            "lat": lat,
            "lon": lon,
            "exclude": "minutely,alerts",
            "appid": self._token,
            "lang": lang,
            "units": units,
        }
        try:
            weather_resp = await client.get(self.ONECALL_URL, params=weather_params)
        except httpx.HTTPError as exc:
            raise WeatherBotError("Помилка мережі під час запиту погоди") from exc

        if weather_resp.status_code >= 400:
            raise WeatherBotError(f"Помилка API погоди: {weather_resp.text}")

        weather_json: dict[str, Any] = weather_resp.json()
        weather_json["name"] = coords["name"]
        return weather_json

    # ------------------------------------------------------------------
    # async context manager support
    # ------------------------------------------------------------------

    async def __aenter__(self) -> "OpenWeatherClient":
        await self._client_or_create()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):  # noqa: D401 – context exit
        if self._client and not self._client.is_closed:
            await self._client.aclose()

    # ------------------------------------------------------------------
    # internal
    # ------------------------------------------------------------------

    async def _client_or_create(self) -> httpx.AsyncClient:
        if self._client is None or self._client.is_closed:
            self._client = httpx.AsyncClient(timeout=10)
        return self._client