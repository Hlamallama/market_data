import asyncio
import argparse
import logging
from market_data.provider.stock_provider import StockProvider

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s')

async def main():
    parser = argparse.ArgumentParser(description="Stock CLI")
    parser.add_argument("--symbols", "-s", nargs="+", required=True, help="Stock symbols")
    args = parser.parse_args()

    provider = StockProvider()
    tasks = [provider.fetch_data(symbol.upper()) for symbol in args.symbols]
    results = await asyncio.gather(*tasks)

    output = "\n".join(results)
    logging.info("Stocks\n%s", output)

if __name__ == "__main__":
    asyncio.run(main())
