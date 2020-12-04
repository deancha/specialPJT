import pandas as pd

df = pd.read_csv("./userNewData.csv", encoding = 'utf-8')
df['email'] = [ i for i in range(100000)]
# print(df['email'])
pd.concat([df['email'],df],axis=1)

df.to_csv("./userNewData2.csv")