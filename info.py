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

# compute item-total correlation and item reliability
df_out.loc['item_total_corr'] = df_in.corrwith(df_in['Total']) 
df_out.loc['item_reliability'] = df_in.corrwith(df_in['Total']) * df_in.std()
for i in df_in.columns[3:-1]:
    df_out.loc['item_total-i_corr', i] = np.corrcoef(df_in[i], df_in['Total']-df_in[i])[0, 1]

# save to file
df_out.transpose().to_csv("description.csv")


# compute cronbach's alpha
items = df_in.iloc[:, 3:-1]
item_var = items.var()
K = len(items.columns)

alpha = (K/(K-1)) * (1 - (item_var.sum() / df_in['Total'].var()))
print(f"Cronbach's alpha = {alpha}")