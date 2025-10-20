import pytest
from unittest.mock import AsyncMock, MagicMock, patch
from market_data.provider.stock_provider import StockProvider, cache

@pytest.mark.asyncio
async def test_fetch_data_success():
    provider = StockProvider()
    cache.clear()

    mock_response = {
        "c": 247.01,
        "d": -2.33,
        "dp": -0.9345,
        "h": 250.18,
        "l": 245.13,
        "o": 250.18,
        "pc": 249.34,
    }

    mock_response_cm = AsyncMock()
    mock_response_cm.__aenter__.return_value.status = 200
    mock_response_cm.__aenter__.return_value.json = AsyncMock(return_value=mock_response)

    mock_session_cm = MagicMock()
    mock_session_cm.__aenter__.return_value = mock_session_cm
    mock_session_cm.get.return_value = mock_response_cm

    with patch("market_data.provider.stock_provider.aiohttp.ClientSession", return_value=mock_session_cm):
        result = await provider.fetch_data("AAPL")

    assert "Current: 247.01" in result
    assert "Change: -2.33 (-0.9345%)" in result


@pytest.mark.asyncio
async def test_fetch_data_invalid_json():
    cache.clear()
    provider = StockProvider()
    symbol = "AAPL"

    mock_response_cm = AsyncMock()
    mock_response_cm.__aenter__.return_value.status = 200
    mock_response_cm.__aenter__.return_value.json = AsyncMock(return_value={"unexpected": "data"})

    mock_session_cm = MagicMock()
    mock_session_cm.__aenter__.return_value = mock_session_cm
    mock_session_cm.get.return_value = mock_response_cm

    with patch("market_data.provider.stock_provider.aiohttp.ClientSession", return_value=mock_session_cm):
        result = await provider.fetch_data(symbol)

    assert "Unexpected error" in result