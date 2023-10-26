import pandas as pd
import numpy as np

file = "cleaned_data.csv"
df_in = pd.read_csv(file)

# descriptive statistics
df_out = df_in.describe()
# add skew and kurtosis
df_out.loc["skew"] = df_in.skew()
df_out.loc["kurtosis"] = df_in.kurtosis()

df_out.to_csv("descriptive_stat.csv")