import pandas as pd
import logging

def load_csv(path: str):
    df = pd.read_csv(path)
    logging.info("📊 Loaded %d rows and %d columns", len(df), len(df.columns))
    return df
