import pandas as pd

def extract_data(file_path):
    try:
        df = pd.read_csv(file_path)
        print("Dữ liệu đã được đọc thành công.")
        return df
    except Exception as e:
        print("Lỗi khi đọc dữ liệu:", e)
        return None

if __name__ == "__main__":
    df = extract_data("data/vgsales.csv")
    if df is not None:
        print("\n Tổng quan dữ liệu:")
        print(df.info())
        print("\n Mô tả thống kê:")
        print(df.describe())
        print("\n 5 dòng đầu:")
        print(df.head())
