import ccxt
import pandas as pd
from src.core.io import save_csv


print("Exchanges soportados:", ccxt.exchanges[:10], "...")


rows = []
for ex_name in ccxt.exchanges:
ex = getattr(ccxt, ex_name)()
has = ex.has
rows.append({
"exchange": ex_name,
"has_spot": has.get("spot", False),
"has_margin": has.get("margin", False),
"has_future": has.get("future", False),
})


df = pd.DataFrame(rows)
path = save_csv(df, "exchanges.csv")
print(f"Guardado en {path}")