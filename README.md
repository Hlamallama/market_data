# Async Stock CLI

A Python CLI tool to fetch real-time stock prices asynchronously using Finnhub. Supports multiple tickers and prints nicely formatted output.  

## Features

- Fetch multiple stock symbols asynchronously.  
- Display current price, change, percent change, high, low, open, and previous close.  
- Supports Finnhub **secret key** authentication.  
- Optional caching to reduce API calls.  

## Requirements

- Python 3.10+  

## Install requirements:

```bash
pip install -r requirements.txt
```

## Run CLI
```bash
python -m market_data.cli.client --symbols AAPL
```

## Example output
```bash
Current: 247.01
Change: -2.33 (-0.9345%)
High: 250.18
Low: 245.13
Open: 250.18
Previous Close: 249.34
------------------------------
```
