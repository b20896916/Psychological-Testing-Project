import pandas as pd

file = "responses.csv"
df = pd.read_csv(file)
# drop the first two columns
df.drop(df.columns[0:2], axis=1, inplace=True)
df.drop(df.columns[-1], axis=1, inplace=True)


# drop the rows with missing values
df.dropna(inplace=True)

# rename the columns
column_name_mapping = {"您的年齡(足歲)": "Age", "您的性別": "Sex", "感情狀況": "Relationship_Status"}
df.rename(columns=column_name_mapping, inplace=True)
df["Age"] = df["Age"].str.replace("歲", "")
def function_1(x):
   tmp = x.split('.')
   if len(tmp) == 1:
       return f"{tmp[0]}"
   return f"{tmp[0]}."
df.rename(columns=function_1, inplace=True)

# convert Likert scale to numerical values
mapping = {"非常同意": 5, "同意": 4, "普通": 3, "不同意": 2, "非常不同意": 1}
df.replace(mapping, inplace=True)
reverse_scale = {"17.", "34.", "42."}
for i in reverse_scale:
   df[i] = 6 - df[i]
df["Total"] = df.iloc[:, 3:].sum(axis=1)

# convert sex and relationship status to numerical values
sex_mapping = {"生理男性": 1, "生理女性": 0}
relation_mapping = {"單身": 0, "有伴侶": 1}
df.replace(sex_mapping, inplace=True)
df.replace(relation_mapping, inplace=True)

df.to_csv("cleaned_data.csv", index=False)