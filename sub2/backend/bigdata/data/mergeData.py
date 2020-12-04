import pandas as pd

df1 = pd.read_csv("./data20s.csv")
df2 = pd.read_csv("./data30s.csv")

result = pd.concat([df1,df2], ignore_index=True)
result.drop("Unnamed: 0", axis=1, inplace=True)
# result = df1.append(df2)
print(result)

result.to_csv("./userdata.csv")