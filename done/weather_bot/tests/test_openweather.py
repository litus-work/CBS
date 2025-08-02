import asyncio
import pytest
from services.openweather import OpenWeatherClient, CityNotFoundError


@pytest.mark.asyncio
async def test_city_not_found():
    client = OpenWeatherClient(token="invalid")
    with pytest.raises(CityNotFoundError):
        await client.get_current("Atlantis")