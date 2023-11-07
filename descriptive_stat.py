import pandas as pd
import numpy as np

file = "cleaned_data.csv"
df_in = pd.read_csv(file)

df_low = df_in[df_in['Total'].between(*df_in['Total'].quantile([0, 0.333]))]
df_high = df_in[df_in['Total'].between(*df_in['Total'].quantile([0.666, 1]))]

# descriptive statistics
df_out = df_in.describe()
# add skew and kurtosis
df_out.loc["skew"] = df_in.skew()
df_out.loc["kurtosis"] = df_in.kurtosis()
df_out.loc["mean diff"] = df_high.mean() - df_low.mean()
df_out.to_csv("descriptive_stat.csv")