import numpy as np
import pandas as pd

np.random.seed(42)

emails = pd.DataFrame({
    "email_id": range(6),
    "customer_id": [101, 102, 103, 101, 104, 105],
    "send_time": pd.to_datetime("2023-01-01") 
    + pd.to_timedelta(np.random.randint(0, 240, size=6), unit="h"),
})

sales = pd.DataFrame({
    "sale_id": range(6),
    "customer_id": [101, 102, 101, 104, 106, 105],
    "sale_time": pd.to_datetime("2023-01-01") + pd.to_timedelta(np.random.randint(0, 240, size=6), unit="h"),
    "amount": np.round(np.random.normal(100, 20, size=6), 2),
})

print("Emails:") 
print(emails) 
print("Sales:") 
print(sales) 

merged = pd.merge(sales, emails, on="customer_id", how="left")

merged["time_diff"] = merged["sale_time"] - merged["send_time"]

merged["influenced"] = (merged["time_diff"] >= pd.Timedelta(0)) & (merged["time_diff"] <= pd.Timedelta(hours=72))

result = merged[["sale_id", "customer_id", "sale_time", "send_time", "influenced"]]

print("Resultado:")
print(result)
