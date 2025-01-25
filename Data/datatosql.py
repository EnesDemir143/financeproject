import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv("/Users/enesdemir/Desktop/financeProject/.venv/.env")

class db:

    @staticmethod
    def add_values_db(last_month_json):
        password = os.getenv("MYSQL_PASSWORD")

        db = mysql.connector.connect(
            host="localhost",
            user="root",  
            password=f"{password}",
            database="finance"  
        )

        cursor = db.cursor()

        # meta_data = last_month_json["Meta Data"]

        # check_company_query = """
        # SELECT id FROM company 
        # WHERE symbol = %s 
        #   AND last_refreshed = %s 
        #   AND intervaltime = %s 
        #   AND output_size = %s 
        #   AND time_zone = %s
        # """
        # check_company_values = (
        #     meta_data["2. Symbol"],
        #     meta_data["3. Last Refreshed"],
        #     meta_data["4. Interval"],
        #     meta_data["5. Output Size"],
        #     meta_data["6. Time Zone"]
        # )

        # cursor.execute(check_company_query, check_company_values)
        # existing_company = cursor.fetchone()

        # if existing_company:
        #     print("Şirket zaten var, eklenmedi.")
        #     company_id = existing_company[0]
        # else:
        #     insert_company_query = """
        #     INSERT INTO company (symbol, last_refreshed, intervaltime, output_size, time_zone)
        #     VALUES (%s, %s, %s, %s, %s)
        #     """
        #     cursor.execute(insert_company_query, check_company_values)
        #     company_id = cursor.lastrowid
        #     print("Şirket başarıyla eklendi.")

        insert_stock_data_query = """
         INSERT INTO stock_data (timestampp, open_price, high_price, low_price, close_price, volume, company_id)
         VALUES (%s, %s, %s, %s, %s, %s, %s)
         """

        stock_data = last_month_json["Time Series (5min)"]

        for time, data in stock_data.items():
            check_stock_data_query = """
            SELECT id FROM stock_data 
            WHERE timestampp = %s 
              AND company_id = %s
            """
            check_stock_data_values = (time, 3)

            cursor.execute(check_stock_data_query, check_stock_data_values)
            existing_stock_data = cursor.fetchone()

            if existing_stock_data:
                pass
            else:
                stock_data_cursor = (
                    time,
                    float(data["1. open"]),
                    float(data["2. high"]),
                    float(data["3. low"]),
                    float(data["4. close"]),
                    int(data["5. volume"]),
                    3
                )
                cursor.execute(insert_stock_data_query, stock_data_cursor)
                print(f"Hisse senedi verisi eklendi: {time}")

        db.commit()
        cursor.close()
        db.close()

        print("Veriler başarıyla işlendi!")