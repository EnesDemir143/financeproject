import mysql.connector
import os
from request import cur_json,last_month_json

password = os.getenv("MYSQL_PASSWORD")

db = mysql.connector.connect(
    host="localhost",
    user="root",  
    password=f"{password}",
    database="finance"  
)

cursor = db.cursor()

meta_data = last_month_json["Meta Data"]

insert_company_query = """
INSERT INTO company (symbol, last_refreshed, intervaltime, output_size, time_zone)
VALUES (%s, %s, %s, %s, %s)
"""

company_values = (
    meta_data["2. Symbol"],
    meta_data["3. Last Refreshed"],
    meta_data["4. Interval"],
    meta_data["5. Output Size"],
    meta_data["6. Time Zone"]
)

cursor.execute(insert_company_query,company_values)
company_id = cursor.lastrowid

insert_stock_data_query = """
INSERT INTO stock_data (timestampp, open_price, high_price, low_price, close_price, volume, company_id)
VALUES (%s, %s, %s, %s, %s, %s, %s)
"""

stock_data = last_month_json["Time Series (5min)"]

for time,data in stock_data.items():
    stock_data_cursor=(
        time,
        float(data["1. open"]),
        float(data["2. high"]),
        float(data["3. low"]),
        float(data["4. close"]),
        int(data["5. volume"]),
        company_id
    )
    cursor.execute(insert_stock_data_query,stock_data_cursor)

db.commit()
cursor.close()
db.close()

print("Veriler başarıyla eklendi!")