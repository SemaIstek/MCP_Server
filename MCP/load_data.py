import pandas as pd

def load_csv(path: str):
    df = pd.read_csv(path)
    print(f"📊 Loaded {len(df)} rows and {len(df.columns)} columns")
    return df
