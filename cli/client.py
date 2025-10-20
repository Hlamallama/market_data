import asyncio
import argparse
from market_data.provider.stock_provider import StockProvider

async def main():
    parser = argparse.ArgumentParser(description="Stock CLI")
    parser.add_argument("--symbols", "-s", nargs="+", required=True, help="Stock symbols")
    args = parser.parse_args()

    provider = StockProvider()
    tasks = [provider.fetch_data(symbol.upper()) for symbol in args.symbols]
    results = await asyncio.gather(*tasks)

    output = "\n".join(results)
    print(output)

if __name__ == "__main__":
    asyncio.run(main())
