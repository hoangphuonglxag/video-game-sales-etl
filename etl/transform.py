# etl/transform.py

def clean_data(df):
    df = df.dropna()

    df.columns = [col.strip().replace(" ", "_") for col in df.columns]

    df["Year"] = df["Year"].astype(int)

    return df
