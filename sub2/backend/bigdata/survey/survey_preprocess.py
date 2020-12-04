import pandas as pd
import math
'''
로직
1. csv 불러와서 pandas 형식으로 저장하기
2. 전처리한 결과를 담을 데이터프레임 만들기
3. 저장한 pandas 한줄씩 돌면서 전처리하기
4. 한줄식 전처리된 결과 새로운 데이터프레임에 처리해서 넣기
5. 다 완성되면 csv파일로 다시 저장
'''
def isNaN(string):
    return string != string

# 1. csv 불러와서 pandas 형식으로 저장
survey = pd.read_csv("./usersurvey.csv",encoding = 'cp949')
# print(survey.head())

#---------------------------------------------------------------------
# 2. 전처리한 결과를 담을 데이터프레임 만들기
# column 목록
# gender, age, friend, couple, family, alone, alcohol,sweet,bitter, sour, body, salty, fancy, spicy, represhing, Carbonated, cloudy, flavor

size_survey = len(survey)

survey_preprocessing_columns = (
    # 칼럼          실제 입력값
    "gender",         # 성별
    "age",            # 나이
    "friend",         # 친구
    "couple",         # 연인
    "family",         # 가족
    "alone",          # 혼자
    "alcohol",        # 도수
    "sweet",          # 단맛
    "bitter",         # 쌉쌀함
    "sour",           # 산미
    "body",           # 바디감
    "salty",          # 고소함
    "fancy",          # 화려함
    "spicy",          # 스파이시
    "represhing",     # 깔끔함
    "carbonated",     # 탄산감
    "cloudy",         # 탁도
    "flavor"          # 향
)
# 전처리담을 데이터 프레임 생성
survey_preprocessing = pd.DataFrame(columns = survey_preprocessing_columns)

#---------------------------------------------------------------------
# 3. 저장한 pandas 한줄씩 돌면서 처리시작

for idx in survey.index:
    # 변수 초기화
    gender_value = 0         # 성별
    age_value = 0            # 나이
    friend_value = 0         # 친구
    couple_value = 0         # 연인
    family_value = 0         # 가족
    alone_value = 0          # 혼자
    alcohol_value = 0        # 무관
    sweet_value = 0          # 단맛
    bitter_value = 0         # 쌉쌀함
    sour_value = 0           # 산미
    body_value = 0           # 바디감
    salty_value = 0          # 고소함
    fancy_value = 0          # 화려함
    spicy_value = 0          # 스파이시
    represhing_value = 0     # 깔끔함
    carbonated_value = 0     # 탄산감
    cloudy_value = 0         # 탁도
    flavor_value = 0         # 향

    # print(survey.loc[idx]) 한줄씩 받아와서 저장
    row = survey.loc[idx]
    # print(row)


    # 성별 처리 (column="gender"남자 : 0, 여자 : 1)
    gender_row = row["gender"]
    if(gender_row == "남"):
        gender_value = 0
    else:
        gender_value = 1 
    # print(gender_value)


    # 나이 처리(column="age")
    age_value = row["age"]
    # print(age_value)


    # 누구랑 먹는지 처리(column="who", 해당 항목있으면 1, 없으면 0)
    who_row = row["who"]
    who_list = []
    # print(who_row)
    
    try :
        who_list = who_row.split(",")
        for i in range(len(who_list)) : 
            # print(who_list[i].strip())
            if(who_list[i].strip()== "친구"):
                friend_value = 1
            elif(who_list[i].strip()=="연인"):
                couple_value = 1
            elif(who_list[i].strip() =="가족"):
                family_value = 1
            else:
                alone_value = 1
    except:
        pass

    



    # 알콜도수 처리(column="alcohol", 무관:0, 10도이하: 1, 10도 이상 20도 이하: 2, 20도 이상:3)
    alcohol_row = row["alcohol"]
    try : 
        # print(alcohol_row)
        if(alcohol_row.strip() == "무관"):
            alcohol_value = 1
        elif(alcohol_row.strip() == "10도이하"):
            alcohol_value = 2
        elif(alcohol_row.strip() == "10도 이상 20도 이하"):
            alcohol_value = 3
        else:
            alcohol_value = 4 
    except:
        pass


    # 좋아하는 맛 처리(column="taste")
    taste_row = row["taste"]
    # print(taste_row)
    taste_list = taste_row.split(",")
    for i in range(len(taste_list)) : 
        if(taste_list[i].strip() =="단맛"):
            sweet_value = 1
        elif(taste_list[i].strip() == "쌉쌀함"):
            bitter_value = 1
        elif(taste_list[i].strip() == "산미"):
            sour_value = 1
        elif(taste_list[i].strip() == "바디감"):
            body_value = 1
        elif(taste_list[i].strip() == "고소함"):
            salty_value = 1
        elif(taste_list[i].strip() == "화려함"):
            fancy_value = 1
        elif(taste_list[i].strip() == "스파이시"):
            spicy_value = 1
        elif(taste_list[i].strip() == "깔끔함"):
            represhing_value = 1
        elif(taste_list[i].strip() == "탄산감"):
            carbonated_value = 1
        elif(taste_list[i].strip() == "탁도"):
            cloudy_value = 1
        elif(taste_list[i].strip() == "향"):
            flavor_value = 1
   

    #---------------------------------------------------------------------
    # 4. 한줄식 전처리된 결과 새로운 데이터프레임에 처리해서 넣기

    survey_preprocessing.loc[idx] = {
        "gender" : gender_value,         # 성별
        "age" : age_value,            # 나이
        "friend" : friend_value,         # 친구
        "couple" : couple_value,         # 연인
        "family" : family_value,         # 가족
        "alone" : alone_value,          # 혼자
        "alcohol" : alcohol_value,        # 도수
        "sweet" : sweet_value,          # 단맛
        "bitter" : bitter_value,         # 쌉쌀함
        "sour" : sour_value,           # 산미
        "body" : body_value,           # 바디감
        "salty" : salty_value,          # 고소함
        "fancy" : fancy_value,          # 화려함
        "spicy" : spicy_value,          # 스파이시
        "represhing" :represhing_value,   # 깔끔함
        "carbonated" : carbonated_value,     # 탄산감
        "cloudy" : cloudy_value,         # 탁도
        "flavor" : flavor_value         # 향
    }

survey_preprocessing.to_csv("./survey_preprocessing.csv")

# if __name__ == "__main__":
#     main()
