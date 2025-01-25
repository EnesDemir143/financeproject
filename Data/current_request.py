import schedule
import time
import requests
import os
from datatosql import db
import logging
from dotenv import load_dotenv  

load_dotenv("/Users/enesdemir/Desktop/financeProject/.venv/.env")

# Log ayarlarını yapılandır
logging.basicConfig(
    level=logging.INFO,  # INFO seviyesindeki logları kaydet
    format="%(asctime)s - %(levelname)s - %(message)s",  # Log formatı
    handlers=[
        logging.FileHandler("script_log.out"),  # Logları dosyaya yaz
        logging.StreamHandler()  # Logları konsola yaz
    ]
)

def url_istek_at():
    API_KEY = os.getenv("alphavantageapi")
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey={API_KEY}'

    try:
        logging.info("API'ye istek gönderiliyor...")
        response = requests.get(url)
        logging.info(f"İstek gönderildi. Durum kodu: {response.status_code}")

        cur_json = response.json()
        logging.info("API'den başarıyla veri alındı.")

        logging.info("Veritabanına veri ekleniyor...")
        db.add_values_db(cur_json)
        logging.info("Veritabanına veri başarıyla eklendi.")

    except requests.exceptions.RequestException as e:
        logging.error(f"İstek sırasında hata oluştu: {e}")
    except Exception as e:
        logging.error(f"Beklenmeyen bir hata oluştu: {e}")

schedule.every().day.at("14:54").do(url_istek_at)

logging.info("Zamanlayıcı başlatıldı. İşlemler başlıyor...")
while True:
    schedule.run_pending()
    time.sleep(1)

#ps aux | grep "Python Data/current_request.py" | grep -v grep bu komut PID bulmayı sağlar.