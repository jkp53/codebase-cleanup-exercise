
# maybe something like the following rough organizational structure would be reasonable.
# then we can import these functions into other files that need them (i.e. crypto.py, stocks.py, unemployment.py).
# one benefit of doing so is we get to refactor all the request-related code out of those files.
# for example, as a result, we'll only have the api key definition in one place (which is good)!

from email.policy import default
import os
from dotenv import load_dotenv
import requests
import json
from pandas import read_csv
from app.utils import to_usd

load_dotenv()

ALPHAVANTAGE_API_KEY = os.getenv("ALPHAVANTAGE_API_KEY", default="demo")


def fetch_crypto_data(symbol):
    url = f"https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_DAILY&market=USD&symbol={symbol}&apikey={ALPHAVANTAGE_API_KEY}"
    response = requests.get(url)
    parsed_response = json.loads(response.text)
    return parsed_response


def fetch_stocks_data(symbol):
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={symbol}&apikey={ALPHAVANTAGE_API_KEY}&datatype=csv"
    df = read_csv(url)
    return df

def fetch_unemployment_data():
    # url = ...
    # make a request
    # return some data
    return "TODO"


## TESTING IN ISOLATION

if __name__ =="__main__":
    symbol = input("Please input a stock ticker ie 'TSLA'", default = "TSLA")
    print(fetch_stocks_data(symbol))


if __name__ =="__main__":
    symbol = input("Please input a crypto symbol (default: 'BTC'): ") or "BTC"
    print(fetch_crypto_data(symbol))
