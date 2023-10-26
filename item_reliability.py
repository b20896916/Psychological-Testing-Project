import pandas as pd

data = "cleaned_data.csv"
df_in = pd.read_csv(data)

# compute item-total correlation and item reliability
df_out = pd.DataFrame(columns=df_in.columns)
df_out.loc['item_total_corr'] = df_in.corrwith(df_in['Total']) 
df_out.loc['item_reliability'] = df_in.corrwith(df_in['Total']) * df_in.std()

df_out.to_csv("item_reli.csv")

# compute cronbach's alpha
items = df_in.iloc[:, 3:-1]
item_var = items.var()
K = len(items.columns)

alpha = (K/(K-1)) * (1 - (item_var.sum() / df_in['Total'].var()))
print(f"Cronbach's alpha = {alpha}")