import aiohttp
from diskcache import Cache
from market_data.model import Stock
from market_data.provider.provider import Provider

cache = Cache("stock_cache")

class StockProvider(Provider):
    url = "https://finnhub.io/api/v1/quote"
    access_key = "d3ok9gpr01quo6o4nu2gd3ok9gpr01quo6o4nu30"
    
    async def fetch_data(self, symbol: str) -> str:
        """
        Fetch market data.
        """
        params = {
            "token": self.access_key,
            "symbol": symbol,
        }
        if symbol in cache:
            return str(Stock(**cache[symbol]))

        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(self.url, params=params) as response:
                    data = await response.json()
                    cache[symbol] = data
                    return str(Stock(**data))        
        except aiohttp.ClientError as e:
            return f"Network error for {symbol}: {str(e)}"
        except Exception as e:
            return f"Unexpected error for {symbol}: {str(e)}"