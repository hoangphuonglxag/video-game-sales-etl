# etl/extract.py

import pandas as pd

def extract_data(file_path):
    try:
        df = pd.read_csv(file_path)
        print("[✓] Dữ liệu đã được đọc thành công.")
        return df
    except Exception as e:
        print("[✗] Lỗi khi đọc dữ liệu:", e)
        return None

if __name__ == "__main__":
    df = extract_data("../vgsales.csv")
    print(df.head())