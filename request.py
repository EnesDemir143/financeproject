import requests # type: ignore

API_KEY = "MEGBZ2KZ70KC5KZ5"

curr_url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey={API_KEY}'

last_month_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&outputsize=full&apikey={API_KEY}"

cur_response = requests.get(curr_url)
cur_json = cur_response.json()

last_month_response = requests.get(last_month_url)
last_month_json = last_month_response.json()


