import numpy as np
import pandas as pd

rng = np.random.default_rng(42)

n = 600
products = {"Laptop": 850, "Phone": 520, "Headphones": 90, "Monitor": 260, "Keyboard": 45}
cities = ["Lahore", "Karachi", "Islamabad", "Multan", "Faisalabad"]

dates = pd.to_datetime("2025-01-01") + pd.to_timedelta(rng.integers(0, 365, n), unit="D")
prod = rng.choice(list(products), n)
df = pd.DataFrame({
    "order_id": np.arange(1001, 1001 + n),
    "order_date": dates,
    "city": rng.choice(cities, n),
    "product": prod,
    "quantity": rng.integers(1, 6, n),
    "unit_price": [products[p] * rng.uniform(0.9, 1.1) for p in prod],
    "customer_rating": rng.integers(1, 6, n).astype(float),
})
df["unit_price"] = df["unit_price"].round(2)

df["order_date"] = df["order_date"].dt.strftime("%Y-%m-%d")
mix = rng.choice(n, 60, replace=False)
df.loc[mix, "order_date"] = pd.to_datetime(df.loc[mix, "order_date"]).dt.strftime("%d/%m/%Y")

df["city"] = df["city"].astype(object)
bad = rng.choice(n, 90, replace=False)
df.loc[bad, "city"] = [c.lower() if i % 2 else f"  {c.upper()} " for i, c in enumerate(df.loc[bad, "city"])]

df.loc[rng.choice(n, 40, replace=False), "customer_rating"] = np.nan
df.loc[rng.choice(n, 25, replace=False), "unit_price"] = np.nan
df.loc[rng.choice(n, 15, replace=False), "quantity"] = np.nan

df.loc[[5, 77, 140], "unit_price"] = [99999, 88888, -50]

df = pd.concat([df, df.sample(30, random_state=1)], ignore_index=True)

df.to_csv("sales_raw_messy.csv", index=False)
print("saved", len(df), "rows")
