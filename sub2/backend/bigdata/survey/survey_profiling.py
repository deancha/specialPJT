import pandas as pd 
import pandas_profiling


data = pd.read_csv("./usersurvey.csv", encoding = 'cp949')
pr = data.profile_report()
pr.to_file('./survey_raw.html')