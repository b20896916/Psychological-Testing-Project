import pandas as pd
import numpy as np

file = "cleaned_data.csv"
df_in = pd.read_csv(file)

items = df_in.iloc[:, 3:-1]
df_out = items.corr()
df_out.to_csv("interitem_corr.csv")