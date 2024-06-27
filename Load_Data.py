import csv
import mysql.connector
from mysql.connector import Error
import os

def load_data_from_csv_to_mysql(csv_file, table_name, mysql_config):
    try:
        conn = mysql.connector.connect(**mysql_config)
        cursor = conn.cursor()

        print("Current working directory:", os.getcwd())

        csv_path = os.path.join('DATA', csv_file)
        
        with open(csv_path, 'r', newline='', encoding='utf-8') as file:
            csv_reader = csv.reader(file)
            next(csv_reader)  
            for row in csv_reader:
                sql = f"INSERT INTO {table_name} (Product, category, prix, commission) VALUES (%s, %s, %s, %s)"
                cursor.execute(sql, row)

        conn.commit()  

        print("Successfully loaded data from CSV file to MySQL.")

    except Error as e:
        print(f"Error loading data from CSV file to MySQL: {e}")

    finally:
        if conn and conn.is_connected():
            cursor.close()
            conn.close()