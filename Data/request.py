import requests # type: ignore
import os
from datatosql import db
from dotenv import load_dotenv  # python-dotenv kütüphanesini import edin

load_dotenv("/Users/enesdemir/Desktop/financeProject/.venv")

API_KEY = os.getenv("alphavantageapi")

last_month_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&outputsize=full&apikey={API_KEY}"


last_month_response = requests.get(last_month_url)
last_month_json = last_month_response.json()


db.add_values_db(last_month_json)

