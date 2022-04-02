


print("CRYPTO REPORT...")

from app.alphavantage_service import fetch_crypto_data
from app.utils import to_usd


symbol = input("Please input a crypto symbol (default: 'BTC'): ") or "BTC"
parsed_response = fetch_crypto_data(symbol)
tsd = parsed_response["Time Series (Digital Currency Daily)"]
dates = list(tsd.keys())
latest_date = dates[0]
latest = tsd[latest_date]
print(symbol)
print(latest_date)
print(latest['4a. close (USD)'])
print(to_usd(float(latest['4a. close (USD)'])))
