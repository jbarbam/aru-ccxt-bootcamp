from pathlib import Path
import pandas as pd

DATA_DIR = Path("data")
DATA_DIR.mkdir(exist_ok=True)

def save_csv(df: pd.DataFrame, name: str) -> str:
path = DATA_DIR / name
df.to_csv(path, index=False)
return str(path)