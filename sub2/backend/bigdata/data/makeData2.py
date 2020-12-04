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
    "flavor",          # 향
    '오매백주', '오산막걸리', '세종대왕어주 탁주', '술공방 9.0', '수제탁주 바랑', '백년향', '문희 가향주', '구름을 벗삼아', '문희 탁주', '오미자 생막걸리', '오희', '복순도가 손 막걸리', '담은', '펀치 쌀바나나', '세종 알밤주', '괴산 세종 찰옥수수', '조은술 세종 바나나', '우도 땅콩 전통주', '우리술 오늘 탁주', '기다림 34', '기다림 25', '기다림 16', '택이', '천비향 탁주', '술그리다 ', '술예쁘다', '술취한 원숭이', '삼양춘 생탁주', '토박이 한산소곡주', '삼양춘 청주', '복단지', '경성과하주', '세종대왕어주 약주', '구기홍주', '하타', '단상지교', '고흥 유자주', '수제 약주 별바랑', '삼양춘 생약주', '순향주', '우렁이쌀 청주', '술아 국화주', '맑은 문희주', '대윤가야곡 왕주', '니모메', '오메기술13 세트', '청명주 약주', '술아 순곡주', '우리술 오늘 약주', '술아 연화주', '술아 매화주', '솔송주', '천비향 약주', '살아있는 기운 한 모금! 홍삼명주', '감사', '면천두견주', '부자진', '꿀샘16', '독산53', '독산30', '신례명주',
                 '진맥소주22', '진맥소주40', '진맥소주53', '귀감', '겨울소주', '설성사또', '병영소주', '문배술 헤리티지23', '문배술 헤리티지25', '문배술 헤리티지40', '안동소주', '설레온', '고소리술', '이도', '고구마증류주', '담솔', '고울달오크', '고울달백자', '문경바람백자', '문경바람오크', '화주', '추사40', '매실원주13', '서울의밤', '미르25', '미르40', '미르54', '술샘16', '오미로제연', '2016크라테산머루레드와인스위트', '혼다주', '요새로제', '더그런치', '스위마마', '댄싱파파', '마셔블랑', '젤코바프리미엄레드', '고도리프리미엄청수화이트', '젤코바스위트와인', '씨엘고도리와이너리화이트', '고도리복숭아와인', 'LESDOM 내추럴 스파클링 로제', 'LESDOM 로제시드르', 'LESDOM 시드르', '참뽕와인', '세인트하우스 아로니아와인', '세인트하우스 오미자와인', '세인트하우스 모과와인', '세인트하우스 가시오가피와인', '세인트하우스 딸기와인', '한스오차드 애플', '애피소드애플', '애피소드상그리아', '오미로제프리미엄와인', '허니비와인', '오미로제스파클링결', '허니문와인', '추사애플와인', '추사블루스위트'


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


print("20대/남 : 78000건 생성")
for i in tqdm(range(0,78000)) :
    age_value = randint(20,29)
    gender_value = 0
    
    # 친구
    rr = uniform(0.4, 1.0)
    if(rr * 1.7 >= THRESHOLD_VALUE) :
        friend_value = 1
    else :
        friend_value = 0

    # 연인
    rr = uniform(0.4, 1.0)
    if(rr * 0.95 >= THRESHOLD_VALUE) :
        couple_value = 1         
    else :
        couple_value = 0
    
    # 가족
    rr = uniform(0.4, 1.0)
    if(rr * 0.97 >= THRESHOLD_VALUE) :
        family_value = 1         
    else :
        family_value = 0
    
    # 혼자
    rr = uniform(0.4, 1.0)
    if(rr * 0.9 >= THRESHOLD_VALUE) :
        alone_value = 1         
    else :
        alone_value = 0

    # 알콜도수
    alcohol_value = randint(1,4)

    # 단맛 
    rr = uniform(0.4, 1.0)
    if(rr * 1.05 >= THRESHOLD_VALUE) :
        sweet_value = 1         
    else :
        sweet_value = 0

    # 쓴맛
    rr = uniform(0.4, 1.0)
    if(rr * 0.85 >= THRESHOLD_VALUE) :
        bitter_value = 1         
    else :
        bitter_value = 0

    # 산미
    rr = uniform(0.4, 1.0)
    if(rr * 0.83 >= THRESHOLD_VALUE) :
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



print("20대/여 : 3만5천건생성")
for i in tqdm(range(78000,100000)) :

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

