import pandas as pd 
import pandas_profiling


data = pd.read_csv("./data20s.csv", encoding = 'cp949')
pr = data.profile_report()
pr.to_file('./profiling.html')