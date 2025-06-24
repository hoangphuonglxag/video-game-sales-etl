# etl/load.py

import pandas as pd
from sqlalchemy import create_engine

def load_to_postgres(df, table_name, db_config):
    try:
        # Tạo chuỗi kết nối
        engine = create_engine(
            f"postgresql://{db_config['user']}:{db_config['password']}@{db_config['host']}:{db_config['port']}/{db_config['dbname']}"
        )
        # Ghi DataFrame vào PostgreSQL
        df.to_sql(table_name, engine, if_exists='replace', index=False)
        print(f"Đã nạp dữ liệu vào bảng '{table_name}'.")
    except Exception as e:
        print("Lỗi khi nạp dữ liệu:", e)

if __name__ == "__main__":
    from transform import clean_data
    from extract import extract_data

    # 1. Extract
    df = extract_data("data/vgsales.csv")

    # 2. Transform
    clean_df = clean_data(df)

    # 3. Config PostgreSQL
    db_config = {
        "host": "localhost",
        "port": "5432",
        "user": "postgres",
        "password": "123456",
        "dbname": "vgsalesdb"
    }

    # 4. Load
    load_to_postgres(clean_df, "video_game_sales", db_config)