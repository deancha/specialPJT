import pandas as pd
from tqdm import tqdm
from tqdm import trange
from random import *

'''
docs / 데이터 생성 가설.md 파일 참고
'''
THRESHOLD_VALUE = 0.8

data_columns = (
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

userdata = pd.DataFrame(columns = data_columns)

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


print("20대/남 : 24만건 생성")
for i in tqdm(range(0,240000)) :
    age_value = randint(20,29)
    gender_value = 0
    
    # 친구
    rr = uniform(0.4, 1.0)
    if(rr * 1.5 >= THRESHOLD_VALUE) :
        friend_value = 1
    else :
        friend_value = 0

    # 연인
    rr = uniform(0.4, 1.0)
    if(rr * 1.5 >= THRESHOLD_VALUE) :
        couple_value = 1         
    else :
        couple_value = 0
    
    # 가족
    rr = uniform(0.4, 1.0)
    if(rr * 1.1 >= THRESHOLD_VALUE) :
        family_value = 1         
    else :
        family_value = 0
    
    # 혼자
    rr = uniform(0.4, 1.0)
    if(rr * 1.3 >= THRESHOLD_VALUE) :
        alone_value = 1         
    else :
        alone_value = 0

    # 알콜도수
    alcohol_value = randint(1,4)

    # 단맛 
    rr = uniform(0.4, 1.0)
    if(rr * 1.3 >= THRESHOLD_VALUE) :
        sweet_value = 1         
    else :
        sweet_value = 0

    # 쓴맛
    rr = uniform(0.4, 1.0)
    if(rr * 0.8 >= THRESHOLD_VALUE) :
        bitter_value = 1         
    else :
        bitter_value = 0

    # 산미
    rr = uniform(0.4, 1.0)
    if(rr * 1.1 >= THRESHOLD_VALUE) :
        sour_value = 1         
    else :
        sour_value = 0

     # 바디감
    rr = uniform(0.4, 1.0)
    if(rr * 0.9 >= THRESHOLD_VALUE) :
        body_value = 1         
    else :
        body_value = 0

    
     # 고소함
    rr = uniform(0.4, 1.0)
    if(rr * 1.0 >= THRESHOLD_VALUE) :
        salty_value = 1         
    else :
        salty_value = 0

    # 화려함
    rr = uniform(0.4, 1.0)
    if(rr * 1.0 >= THRESHOLD_VALUE) :
        fancy_value = 1         
    else :
        fancy_value = 0

    # 스파이시
    rr = uniform(0.4, 1.0)
    if(rr * 0.9 >= THRESHOLD_VALUE) :
        spicy_value = 1         
    else :
        spicy_value = 0

    # 깔끔함
    rr = uniform(0.4, 1.0)
    if(rr * 1.3 >= THRESHOLD_VALUE) :
        represhing_value = 1         
    else :
        represhing_value = 0

    # 탄산감
    rr = uniform(0.4, 1.0)
    if(rr * 1.0 >= THRESHOLD_VALUE) :
        carbonated_value = 1         
    else :
        carbonated_value = 0

    # 탁도
    rr = uniform(0.4, 1.0)
    if(rr * 1.1 >= THRESHOLD_VALUE) :
        cloudy_value = 1         
    else :
        cloudy_value = 0

    # 향
    rr = uniform(0.4, 1.0)
    if(rr * 1.1 >= THRESHOLD_VALUE) :
        flavor_value = 1         
    else :
        flavor_value = 0
   

    userdata.loc[i] = {
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



print("20대/여 : 16만건생성")
for i in tqdm(range(240000,400000)) :

    age_value = randint(20,29)
    gender_value = 1
    
    # 친구
    rr = uniform(0.4, 1.0)
    if(rr * 1.4 >= THRESHOLD_VALUE) :
        friend_value = 1         
    else :
        friend_value = 0

    # 연인
    rr = uniform(0.4, 1.0)
    if(rr * 1.6 >= THRESHOLD_VALUE) :
        couple_value = 1         
    else :
        couple_value = 0
    
    # 가족
    rr = uniform(0.4, 1.0)
    if(rr * 1.1 >= THRESHOLD_VALUE) :
        family_value = 1         
    else :
        family_value = 0
    
    # 혼자
    rr = uniform(0.4, 1.0)
    if(rr * 1.1 >= THRESHOLD_VALUE) :
        alone_value = 1         
    else :
        alone_value = 0

    # 알콜도수
    alcohol_value = randint(1,4)

    # 단맛 
    rr = uniform(0.4, 1.0)
    if(rr * 1.3 >= THRESHOLD_VALUE) :
        sweet_value = 1         
    else :
        sweet_value = 0

    # 쓴맛
    rr = uniform(0.4, 1.0)
    if(rr * 0.8 >= THRESHOLD_VALUE) :
        bitter_value = 1         
    else :
        bitter_value = 0

    # 산미
    rr = uniform(0.4, 1.0)
    if(rr * 1.2 >= THRESHOLD_VALUE) :
        sour_value = 1         
    else :
        sour_value = 0

     # 바디감
    rr = uniform(0.4, 1.0)
    if(rr * 0.9 >= THRESHOLD_VALUE) :
        body_value = 1         
    else :
        body_value = 0

    
     # 고소함
    rr = uniform(0.4, 1.0)
    if(rr * 1.0 >= THRESHOLD_VALUE) :
        salty_value = 1         
    else :
        salty_value = 0

    # 화려함
    rr = uniform(0.4, 1.0)
    if(rr * 1.1 >= THRESHOLD_VALUE) :
        fancy_value = 1         
    else :
        fancy_value = 0

    # 스파이시
    rr = uniform(0.4, 1.0)
    if(rr * 0.8 >= THRESHOLD_VALUE) :
        spicy_value = 1         
    else :
        spicy_value = 0

    # 깔끔함
    rr = uniform(0.4, 1.0)
    if(rr * 1.3 >= THRESHOLD_VALUE) :
        represhing_value = 1         
    else :
        represhing_value = 0

    # 탄산감
    rr = uniform(0.4, 1.0)
    if(rr * 1.0 >= THRESHOLD_VALUE) :
        carbonated_value = 1         
    else :
        carbonated_value = 0

    # 탁도
    rr = uniform(0.4, 1.0)
    if(rr * 1.1 >= THRESHOLD_VALUE) :
        cloudy_value = 1         
    else :
        cloudy_value = 0

    # 향
    rr = uniform(0.4, 1.0)
    if(rr * 1.2 >= THRESHOLD_VALUE) :
        flavor_value = 1
    else :
        flavor_value = 0
   

    userdata.loc[i] = {
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

print("30대/남 : 36만건 생성")
for i in tqdm(range(400000,760000)) :
    age_value = randint(30,39)
    gender_value = 0
    
    # 친구
    rr = uniform(0.4, 1.0)
    if(rr * 1.2 >= THRESHOLD_VALUE) :
        friend_value = 1         
    else :
        friend_value = 0

    # 연인
    rr = uniform(0.4, 1.0)
    if(rr * 1.2 >= THRESHOLD_VALUE) :
        couple_value = 1         
    else :
        couple_value = 0
    
    # 가족
    rr = uniform(0.4, 1.0)
    if(rr * 1.0 >= THRESHOLD_VALUE) :
        family_value = 1         
    else :
        family_value = 0
    
    # 혼자
    rr = uniform(0.4, 1.0)
    if(rr * 1.0 >= THRESHOLD_VALUE) :
        alone_value = 1         
    else :
        alone_value = 0

    # 알콜도수
    alcohol_value = randint(1,4)

    # 단맛 
    rr = uniform(0.4, 1.0)
    if(rr * 1.1 >= THRESHOLD_VALUE) :
        sweet_value = 1         
    else :
        sweet_value = 0

    # 쓴맛
    rr = uniform(0.4, 1.0)
    if(rr * 0.9 >= THRESHOLD_VALUE) :
        bitter_value = 1         
    else :
        bitter_value = 0

    # 산미
    rr = uniform(0.4, 1.0)
    if(rr * 1.2 >= THRESHOLD_VALUE) :
        sour_value = 1         
    else :
        sour_value = 0

     # 바디감
    rr = uniform(0.4, 1.0)
    if(rr * 1.0 >= THRESHOLD_VALUE) :
        body_value = 1         
    else :
        body_value = 0

    
     # 고소함
    rr = uniform(0.4, 1.0)
    if(rr * 1.1 >= THRESHOLD_VALUE) :
        salty_value = 1         
    else :
        salty_value = 0

    # 화려함
    rr = uniform(0.4, 1.0)
    if(rr * 1.2 >= THRESHOLD_VALUE) :
        fancy_value = 1         
    else :
        fancy_value = 0

    # 스파이시
    rr = uniform(0.4, 1.0)
    if(rr * 1.0 >= THRESHOLD_VALUE) :
        spicy_value = 1         
    else :
        spicy_value = 0

    # 깔끔함
    rr = uniform(0.4, 1.0)
    if(rr * 1.3 >= THRESHOLD_VALUE) :
        represhing_value = 1         
    else :
        represhing_value = 0

    # 탄산감
    rr = uniform(0.4, 1.0)
    if(rr * 1.1 >= THRESHOLD_VALUE) :
        carbonated_value = 1         
    else :
        carbonated_value = 0

    # 탁도
    rr = uniform(0.4, 1.0)
    if(rr * 1.2 >= THRESHOLD_VALUE) :
        cloudy_value = 1         
    else :
        cloudy_value = 0

    # 향
    rr = uniform(0.4, 1.0)
    if(rr * 1.3 >= THRESHOLD_VALUE) :
        flavor_value = 1         
    else :
        flavor_value = 0
   

    userdata.loc[i] = {
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

print("30대/여 : 24만건 생성")
for i in tqdm(range(760000,1000000)) :
    age_value = randint(30,39)
    gender_value = 1
    
    # 친구
    rr = uniform(0.4, 1.0)
    if(rr * 1.2 >= THRESHOLD_VALUE) :
        friend_value = 1         
    else :
        friend_value = 0

    # 연인
    rr = uniform(0.4, 1.0)
    if(rr * 1.3 >= THRESHOLD_VALUE) :
        couple_value = 1         
    else :
        couple_value = 0
    
    # 가족
    rr = uniform(0.4, 1.0)
    if(rr * 1.0 >= THRESHOLD_VALUE) :
        family_value = 1         
    else :
        family_value = 0
    
    # 혼자
    rr = uniform(0.4, 1.0)
    if(rr * 1.0 >= THRESHOLD_VALUE) :
        alone_value = 1         
    else :
        alone_value = 0

    # 알콜도수
    alcohol_value = randint(1,4)

    # 단맛 
    rr = uniform(0.4, 1.0)
    if(rr * 1.2 >= THRESHOLD_VALUE) :
        sweet_value = 1         
    else :
        sweet_value = 0

    # 쓴맛
    rr = uniform(0.4, 1.0)
    if(rr * 0.9 >= THRESHOLD_VALUE) :
        bitter_value = 1         
    else :
        bitter_value = 0

    # 산미
    rr = uniform(0.4, 1.0)
    if(rr * 1.2 >= THRESHOLD_VALUE) :
        sour_value = 1         
    else :
        sour_value = 0

     # 바디감
    rr = uniform(0.4, 1.0)
    if(rr * 1.1 >= THRESHOLD_VALUE) :
        body_value = 1         
    else :
        body_value = 0

    
     # 고소함
    rr = uniform(0.4, 1.0)
    if(rr * 1.2 >= THRESHOLD_VALUE) :
        salty_value = 1         
    else :
        salty_value = 0

    # 화려함
    rr = uniform(0.4, 1.0)
    if(rr * 1.2 >= THRESHOLD_VALUE) :
        fancy_value = 1         
    else :
        fancy_value = 0

    # 스파이시
    rr = uniform(0.4, 1.0)
    if(rr * 1.1 >= THRESHOLD_VALUE) :
        spicy_value = 1         
    else :
        spicy_value = 0

    # 깔끔함
    rr = uniform(0.4, 1.0)
    if(rr * 1.4 >= THRESHOLD_VALUE) :
        represhing_value = 1         
    else :
        represhing_value = 0

    # 탄산감
    rr = uniform(0.4, 1.0)
    if(rr * 1.1 >= THRESHOLD_VALUE) :
        carbonated_value = 1         
    else :
        carbonated_value = 0

    # 탁도
    rr = uniform(0.4, 1.0)
    if(rr * 1.2 >= THRESHOLD_VALUE) :
        cloudy_value = 1         
    else :
        cloudy_value = 0

    # 향
    rr = uniform(0.4, 1.0)
    if(rr * 1.3 >= THRESHOLD_VALUE) :
        flavor_value = 1         
    else :
        flavor_value = 0
   

    userdata.loc[i] = {
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

userdata.to_csv("./userData.csv")