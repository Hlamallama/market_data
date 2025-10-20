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
            return self._format_data(cache[symbol])

        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(self.url, params=params) as response:
                    data = await response.json()
                    cache[symbol] = data
                    return self._format_data(data)            
        except aiohttp.ClientError as e:
            return f"Network error for {symbol}: {str(e)}"
        except Exception as e:
            return f"Unexpected error for {symbol}: {str(e)}"

    def _format_data(self, stock_data: dict) -> str:
        """
        Convert stock data dict into a formatted string.
        """
        stock = Stock(**stock_data)
        return (
            f"Current: {stock.c}\n"
            f"Change: {stock.d} ({stock.dp}%)\n"
            f"High: {stock.h}\n"
            f"Low: {stock.l}\n"
            f"Open: {stock.o}\n"
            f"Previous Close: {stock.pc}\n"
            + "-"*30
        )