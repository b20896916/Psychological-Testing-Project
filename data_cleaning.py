import pandas as pd

K = 0
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
   global K
   K += 1
   return f"{tmp[0]}."
df.rename(columns=function_1, inplace=True)

# convert Likert scale to numerical values
mapping = {"非常同意": 5, "同意": 4, "普通": 3, "不同意": 2, "非常不同意": 1}
df.replace(mapping, inplace=True)
reverse_scale = {"17.", "34.", "42."}
n = len(reverse_scale)
for i in reverse_scale:
   df[i] = 6 - df[i]
df["Total"] = df.iloc[:, 3:].sum(axis=1)

# drop the rows acquiescently answered
df["diff"] = (df["Total"] - (df["17."] + df["34."] + df["42."]))/(K-n) - (df["17."] + df["34."] + df["42."])/n
df.drop(df[abs(df["diff"]) >= 2].index, inplace=True)
df.drop(["diff"], axis=1, inplace=True)

# drop the rows with constant values
df.drop(df[df.iloc[:, 3:-1].std(axis=1) == 0].index, inplace=True)

# convert sex and relationship status to numerical values
sex_mapping = {"生理男性": 1, "生理女性": 0}
relation_mapping = {"單身": 0, "有伴侶": 1}
df.replace(sex_mapping, inplace=True)
df.replace(relation_mapping, inplace=True)

# keep the columns we decided to use, comment the lines below if you want to use the original data
if input("Do you want to use the selected questions only? (y/n) ") == 'y':
   kept = ["1.", "4.", "11.", "12.", "13.", "15.", "19.", "21.", "24.", "25.", "26.", "27.", "28.", "29.", "30.", "36.", "39.", "40.", "41.", "43.", "44.", "46."]
   df = pd.concat([df.iloc[:, 0:3], df[kept]], axis=1)
   df["Total"] = df.iloc[:, 3:].sum(axis=1)

# filter out those have relationship partner, comment the line below if you want to keep them
if input("Do you want to filter responses according to whether they have relationship partner? (y/n) ") == 'y':
   if input("Do you want to **keep** those have relationship partner (y) or those single (n)? ") == 'y':
       df.drop(df[df["Relationship_Status"] == 0].index, inplace=True)
   else:
      df.drop(df[df["Relationship_Status"] == 1].index, inplace=True)


df.to_csv("cleaned_data.csv", index=False)