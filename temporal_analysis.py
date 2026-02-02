import pandas as pd
import matplotlib.pyplot
import numpy as np
data = 'BTC-market-analysis_2021-25.csv'
df = pd.read_csv(data)
df = df[["date", "btc_return", "sp500_return", "gold_return"]]

df = df.replace(0.000000, pd.NA)
df = df.dropna(subset=["sp500_return"])        
df = df.dropna(subset=["gold_return"])  



print(df.to_string())
