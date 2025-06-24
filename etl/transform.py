# etl/transform.py

import pandas as pd

def clean_data(df):
    df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]

    df['year'] = pd.to_numeric(df['year'], errors='coerce')
    df['na_sales'] = pd.to_numeric(df['na_sales'], errors='coerce')
    df['eu_sales'] = pd.to_numeric(df['eu_sales'], errors='coerce')
    df['jp_sales'] = pd.to_numeric(df['jp_sales'], errors='coerce')
    df['other_sales'] = pd.to_numeric(df['other_sales'], errors='coerce')
    df['global_sales'] = pd.to_numeric(df['global_sales'], errors='coerce')

    df.dropna(inplace=True)

    df.reset_index(drop=True, inplace=True)

    print("Dữ liệu đã được làm sạch.")
    return df

if __name__ == "__main__":
    from extract import extract_data
    df = extract_data("data/vgsales.csv")
    clean_df = clean_data(df)
    print(clean_df.head())
