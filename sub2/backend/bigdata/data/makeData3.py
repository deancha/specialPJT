# -*- coding: utf-8 -*-

import pandas as pd
from tqdm import tqdm
from tqdm import trange
from random import *

'''
docs / 데이터 생성 가설.md 파일 참고
'''
THRESHOLD_VALUE = 0.8

data_columns = (
    'email',
    '오매백주', '오산막걸리', '세종대왕어주 탁주', '술공방 9.0', '수제탁주 바랑', '백년향', '문희 가향주', '구름을 벗삼아', '문희 탁주', '오미자 생막걸리', '오희', '복순도가 손 막걸리', '담은', '펀치 쌀바나나', '세종 알밤주', '괴산 세종 찰옥수수', '조은술 세종 바나나', '우도 땅콩 전통주', '우리술 오늘 탁주', '기다림 34', '기다림 25', '기다림 16', '택이', '천비향 탁주', '술그리다 ', '술예쁘다', '술취한 원숭이', '삼양춘 생탁주', '토박이 한산소곡주', '삼양춘 청주', '복단지', '경성과하주', '세종대왕어주 약주', '구기홍주', '하타', '단상지교', '고흥 유자주', '수제 약주 별바랑', '삼양춘 생약주', '순향주', '우렁이쌀 청주', '술아 국화주', '맑은 문희주', '대윤가야곡 왕주', '니모메', '오메기술13 세트', '청명주 약주', '술아 순곡주', '우리술 오늘 약주', '술아 연화주', '술아 매화주', '솔송주', '천비향 약주', '살아있는 기운 한 모금! 홍삼명주', '감사', '면천두견주', '부자진', '꿀샘16', '독산53', '독산30', '신례명주',
    '진맥소주22', '진맥소주40', '진맥소주53', '귀감', '겨울소주', '설성사또', '병영소주', '문배술 헤리티지23', '문배술 헤리티지25', '문배술 헤리티지40', '안동소주', '설레온', '고소리술', '이도', '고구마증류주', '담솔', '고울달오크', '고울달백자', '문경바람백자', '문경바람오크', '화주', '추사40', '매실원주13', '서울의밤', '미르25', '미르40', '미르54', '술샘16', '오미로제연', '2016크라테산머루레드와인스위트', '혼다주', '요새로제', '더그런치', '스위마마', '댄싱파파', '마셔블랑', '젤코바프리미엄레드', '고도리프리미엄청수화이트', '젤코바스위트와인', '씨엘고도리와이너리화이트', '고도리복숭아와인', 'LESDOM 내추럴 스파클링 로제', 'LESDOM 로제시드르', 'LESDOM 시드르', '참뽕와인', '세인트하우스 아로니아와인', '세인트하우스 오미자와인', '세인트하우스 모과와인', '세인트하우스 가시오가피와인', '세인트하우스 딸기와인', '한스오차드 애플', '애피소드애플', '애피소드상그리아', '오미로제프리미엄와인', '허니비와인', '오미로제스파클링결', '허니문와인', '추사애플와인', '추사블루스위트'
)

userdata = pd.DataFrame(columns = data_columns)

list_data = []

sweet_value = 0          # 단맛
bitter_value = 0         # 쌉쌀함
sour_value = 0           # 산미
body_value = 0           # 바디감
fancy_value = 0          # 화려함
represhing_value = 0     # 깔끔함
flavor_value = 0         # 향
t_w = 1
y_w = 1
w_w = 1
g_w = 1
v오매백주 = 0
v오산막걸리 = 0
v세종대왕어주탁주 =0
v술공방 = 0
v수제탁주바랑 =0
v백년향 =0
v문희가향주=0
v구름을벗삼아=0
v문희탁주=0
v오미자생막걸리=0
v오희 =0 
v복순도가손막걸리=0 
v담은=0 
v펀치쌀바나나=0
v세종알밤주=0
v괴산세종찰옥수수=0
v조은술세종바나나=0
v우도땅콩전통주=0
v우리술오늘탁주=0
v기다림34=0
v기다림25=0
v기다림16=0
v택이=0
v천비향탁주=0
v술그리다=0
v술예쁘다=0
v술취한원숭이=0
v삼양춘생탁주=0
v토박이한산소곡주=0
v삼양춘청주=0
v복단지=0
v경성과하주=0
v세종대왕어주약주=0
v구기홍주=0
v하타=0
v단상지교=0
v고흥유자주=0
v수제약주별바랑=0
v삼양춘생약주=0
v순향주=0
v우렁이쌀청주=0
v술아국화주=0
v맑은문희주=0
v대윤가야곡왕주=0
v니모메=0
v오메기술13세트=0
v청명주약주=0
v술아순곡주=0
v우리술오늘약주=0
v술아연화주=0
v술아매화주=0
v솔송주=0
v천비향약주=0
v살아있는기운한모금홍삼명주=0
v감사=0
v면천두견주=0
v부자진=0
v꿀샘16=0
v독산53=0
v독산30=0
v신례명주=0 
v진맥소주22=0
v진맥소주40=0
v진맥소주53=0
v귀감=0
v겨울소주=0
v설성사또=0
v병영소주=0
v문배술헤리티지23=0
v문배술헤리티지25=0
v문배술헤리티지40=0
v안동소주=0
v설레온=0
v고소리술=0
v이도=0
v고구마증류주=0
v담솔=0
v고울달오크=0
v고울달백자=0
v문경바람백자=0
v문경바람오크=0
v화주=0
v추사40=0
v매실원주13=0
v서울의밤=0
v미르25=0
v미르40=0
v미르54=0
v술샘16=0
v오미로제연=0
v2016크라테산머루레드와인스위트=0
v혼다주=0
v요새로제=0
v더그런치=0
v스위마마=0
v댄싱파파=0
v마셔블랑=0
v젤코바프리미엄레드=0
v고도리프리미엄청수화이트=0
v젤코바스위트와인=0
v씨엘고도리와이너리화이트=0
v고도리복숭아와인=0
vLESDOM내추럴스파클링로제=0
vLESDOM로제시드르=0
vLESDOM시드르=0
v참뽕와인=0
v세인트하우스아로니아와인=0
v세인트하우스오미자와인=0
v세인트하우스모과와인=0
v세인트하우스가시오가피와인=0
v세인트하우스딸기와인=0
v한스오차드애플=0
v애피소드애플=0
v애피소드상그리아=0
v오미로제프리미엄와인=0
v허니비와인=0
v오미로제스파클링결=0
v허니문와인=0
v추사애플와인=0
v추사블루스위트=0


for i in tqdm(range(0,100000),mininterval=1) :

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
    if(rr * 0.84 >= THRESHOLD_VALUE) :
        sour_value = 1         
    else :
        sour_value = 0

     # 바디감
    rr = uniform(0.4, 1.0)
    if(rr * 0.87 >= THRESHOLD_VALUE) :
        body_value = 1         
    else :
        body_value = 0


    # 화려함
    rr = uniform(0.4, 1.0)
    if(rr * 1.0 >= THRESHOLD_VALUE) :
        fancy_value = 1         
    else :
        fancy_value = 0

    

    # 깔끔함
    rr = uniform(0.4, 1.0)
    if(rr * 1.4 >= THRESHOLD_VALUE) :
        represhing_value = 1         
    else :
        represhing_value = 0


    # 향
    rr = uniform(0.4, 1.0)
    if(rr * 0.9 >= THRESHOLD_VALUE) :
        flavor_value = 1         
    else :
        flavor_value = 0
   

   #----------------------------

    # 탁주
    if sweet_value ==1 and sour_value ==1  :
        t_w = 0.982     # 이 비율은 안 사먹은 비율임
    elif sweet_value ==1 and sour_value == 0 :
        t_w = 0.987
    else :
        t_w = 0.994

    # 약주
    if bitter_value == 1 :
        y_w = 0.97
    else :
        y_w = 0.99

    # 와인
    if sour_value == 1 and body_value ==1 :
        w_w = 0.980
    elif sour_value ==1 or body_value ==1 or flavor_value ==1 :
        w_w = 0.985
    else : 
        w_w = 0.993

    # 증류주
    if represhing_value ==1 :
        g_w = 0.989
    else : 
        g_w = 0.996
    
    # ---------------------여기부터 값 매기기 시작
    rr = uniform(0, 1.0)
    if rr > t_w : 
        v오매백주 = 1
    else : 
        v오매백주 = 0
    
    rr = uniform(0, 1.0)
    if rr > t_w : 
        v오산막걸리 = 1
    else : 
        v오산막걸리 = 0
    
    rr = uniform(0, 1.0)
    if rr > t_w : 
        v세종대왕어주탁주 = 1
    else : 
        v세종대왕어주탁주 = 0


    rr = uniform(0, 1.0)
    if rr > t_w : 
        v술공방 = 1
    else : 
        v술공방 = 0


    rr = uniform(0, 1.0)
    if rr > t_w : 
        v수제탁주바랑 = 1
    else : 
        v수제탁주바랑 = 0
    
    rr = uniform(0, 1.0)
    if rr > t_w : 
        v백년향 = 1
    else : 
        v백년향 = 0

    rr = uniform(0, 1.0)
    if rr > t_w : 
        v문희가향주 = 1
    else : 
        v문희가향주 = 0

    rr = uniform(0, 1.0)
    if rr > t_w : 
        v구름을벗삼아 = 1
    else : 
        v구름을벗삼아 = 0

    rr = uniform(0, 1.0)
    if rr > t_w : 
        v문희탁주 = 1
    else : 
        v문희탁주 = 0
        
    
    rr = uniform(0, 1.0)
    if rr > t_w : 
        v오미자생막걸리 = 1
    else : 
        v오미자생막걸리 = 0

    rr = uniform(0, 1.0)
    if rr > t_w : 
        v오희 = 1
    else : 
        v오희 = 0

    rr = uniform(0, 1.0)
    if rr > t_w : 
        v복순도가손막걸리 = 1
    else : 
        v복순도가손막걸리 = 0

    rr = uniform(0, 1.0)
    if rr > t_w : 
        v담은 = 1
    else : 
        v담은 = 0

    rr = uniform(0, 1.0)
    if rr > t_w : 
        v펀치쌀바나나 = 1
    else : 
        v펀치쌀바나나 = 0

    rr = uniform(0, 1.0)
    if rr > t_w : 
        v세종알밤주 = 1
    else : 
        v세종알밤주 = 0 

    rr = uniform(0, 1.0)
    if rr > t_w : 
        v괴산세종찰옥수수 = 1
    else : 
        v괴산세종찰옥수수 = 0 
    
    rr = uniform(0, 1.0)
    if rr > t_w : 
        v조은술세종바나나 = 1
    else : 
        v조은술세종바나나 = 0 

    rr = uniform(0, 1.0)
    if rr > t_w : 
        v우도땅콩전통주 = 1
    else : 
        v우도땅콩전통주 = 0 

    rr = uniform(0, 1.0)
    if rr > t_w : 
        v우리술오늘탁주 = 1
    else : 
        v우리술오늘탁주 = 0 

    rr = uniform(0, 1.0)
    if rr > t_w : 
        v기다림34 = 1
    else : 
        v기다림34 = 0 

    rr = uniform(0, 1.0)
    if rr > t_w : 
        v기다림25 = 1
    else : 
        v기다림25 = 0 

    rr = uniform(0, 1.0)
    if rr > t_w : 
        v기다림16 = 1
    else : 
        v기다림16 = 0 

    rr = uniform(0, 1.0)
    if rr > t_w : 
        v택이 = 1
    else : 
        v택이 = 0 

    rr = uniform(0, 1.0)
    if rr > t_w : 
        v천비향탁주 = 1
    else : 
        v천비향탁주 = 0 

    rr = uniform(0, 1.0)
    if rr > t_w : 
        v술그리다 = 1
    else : 
        v술그리다 = 0 

    rr = uniform(0, 1.0)
    if rr > t_w : 
        v술예쁘다 = 1
    else : 
        v술예쁘다 = 0 

    rr = uniform(0, 1.0)
    if rr > t_w : 
        v술취한원숭이 = 1
    else : 
        v술취한원숭이 = 0

    rr = uniform(0, 1.0)
    if rr > t_w : 
        v삼양춘생탁주 = 1
    else : 
        v삼양춘생탁주 = 0 


# -----------약주--------------
    rr = uniform(0, 1.0)
    if rr > y_w : 
        v토박이한산소곡주 = 1
    else : 
        v토박이한산소곡주 = 0 

    rr = uniform(0, 1.0)
    if rr > y_w : 
        v삼양춘청주 = 1
    else : 
        v삼양춘청주 = 0 

    rr = uniform(0, 1.0)
    if rr > y_w : 
        v복단지 = 1
    else : 
        v복단지 = 0 

    rr = uniform(0, 1.0)
    if rr > y_w : 
        v경성과하주 = 1
    else : 
        v경성과하주 = 0 

    rr = uniform(0, 1.0)
    if rr > y_w : 
        v세종대왕어주약주 = 1
    else : 
        v세종대왕어주약주 = 0 

    rr = uniform(0, 1.0)
    if rr > y_w : 
        v구기홍주 = 1
    else : 
        v구기홍주 = 0 

    rr = uniform(0, 1.0)
    if rr > y_w : 
        v하타 = 1
    else : 
        v하타 = 0 

    rr = uniform(0, 1.0)
    if rr > y_w : 
        v단상지교 = 1
    else : 
        v단상지교 = 0 

    rr = uniform(0, 1.0)
    if rr > y_w : 
        v고흥유자주 = 1
    else : 
        v고흥유자주 = 0 

    rr = uniform(0, 1.0)
    if rr > y_w : 
        v수제약주별바랑 = 1
    else : 
        v수제약주별바랑 = 0 

    rr = uniform(0, 1.0)
    if rr > y_w : 
        v삼양춘생약주 = 1
    else : 
        v삼양춘생약주 = 0 

    rr = uniform(0, 1.0)
    if rr > y_w : 
        v순향주 = 1
    else : 
        v순향주 = 0 
    
    rr = uniform(0, 1.0)
    if rr > y_w : 
        v우렁이쌀청주 = 1
    else : 
        v우렁이쌀청주 = 0 
    
    rr = uniform(0, 1.0)
    if rr > y_w : 
        v술아국화주 = 1
    else : 
        v술아국화주 = 0
    
    rr = uniform(0, 1.0)
    if rr > y_w : 
        v맑은문희주 = 1
    else : 
        v맑은문희주 = 0 

    rr = uniform(0, 1.0)
    if rr > y_w : 
        v대윤가야곡왕주 = 1
    else : 
        v대윤가야곡왕주 = 0 

    rr = uniform(0, 1.0)
    if rr > y_w : 
        v니모메 = 1
    else : 
        v니모메 = 0 

    rr = uniform(0, 1.0)
    if rr > y_w : 
        v오메기술13세트 = 1
    else : 
        v오메기술13세트 = 0 

    rr = uniform(0, 1.0)
    if rr > y_w : 
        v청명주약주 = 1
    else : 
        v청명주약주 = 0 

    rr = uniform(0, 1.0)
    if rr > y_w : 
        v술아순곡주 = 1
    else : 
        v술아순곡주 = 0 

    rr = uniform(0, 1.0)
    if rr > y_w : 
        v우리술오늘약주 = 1
    else : 
        v우리술오늘약주 = 0 

    rr = uniform(0, 1.0)
    if rr > y_w : 
        v술아연화주 = 1
    else : 
        v술아연화주 = 0 

    rr = uniform(0, 1.0)
    if rr > y_w : 
        v술아매화주 = 1
    else : 
        v술아매화주 = 0 

    rr = uniform(0, 1.0)
    if rr > y_w : 
        v솔송주 = 1
    else : 
        v솔송주 = 0 

    
    rr = uniform(0, 1.0)
    if rr > y_w : 
        v천비향약주 = 1
    else : 
        v천비향약주 = 0 

    rr = uniform(0, 1.0)
    if rr > y_w : 
        v살아있는기운한모금홍삼명주 = 1
    else : 
        v살아있는기운한모금홍삼명주 = 0 

    rr = uniform(0, 1.0)
    if rr > y_w : 
        v감사 = 1
    else : 
        v감사 = 0 

    rr = uniform(0, 1.0)
    if rr > y_w : 
        v면천두견주 = 1
    else : 
        v면천두견주 = 0 

   


#-------증류주--------

    rr = uniform(0, 1.0)
    if rr > g_w : 
        v부자진 = 1
    else : 
        v부자진 = 0 

    rr = uniform(0, 1.0)
    if rr > g_w : 
        v꿀샘16 = 1
    else : 
        v꿀샘16 = 0 

    rr = uniform(0, 1.0)
    if rr > g_w : 
        v독산53 = 1
    else : 
        v독산53 = 0 

    rr = uniform(0, 1.0)
    if rr > g_w : 
        v독산30 = 1
    else : 
        v독산30 = 0 

    rr = uniform(0, 1.0)
    if rr > g_w : 
        v신례명주 = 1
    else : 
        v신례명주 = 0 

    rr = uniform(0, 1.0)
    if rr > g_w : 
        v진맥소주22 = 1
    else : 
        v진맥소주22 = 0 

    rr = uniform(0, 1.0)
    if rr > g_w : 
        v진맥소주40 = 1
    else : 
        v진맥소주40 = 0 

    rr = uniform(0, 1.0)
    if rr > g_w : 
        v진맥소주53 = 1
    else : 
        v진맥소주53 = 0 

    rr = uniform(0, 1.0)
    if rr > g_w : 
        v귀감 = 1
    else : 
        v귀감 = 0 

    rr = uniform(0, 1.0)
    if rr > g_w : 
        v겨울소주 = 1
    else : 
        v겨울소주 = 0 

    rr = uniform(0, 1.0)
    if rr > g_w : 
        v설성사또 = 1
    else : 
        v설성사또 = 0 

    rr = uniform(0, 1.0)
    if rr > g_w : 
        v병영소주 = 1
    else : 
        v병영소주 = 0 

    rr = uniform(0, 1.0)
    if rr > g_w : 
        v문배술헤리티지23 = 1
    else : 
        v문배술헤리티지23 = 0 

    rr = uniform(0, 1.0)
    if rr > g_w : 
        v문배술헤리티지25 = 1
    else : 
        v문배술헤리티지25 = 0 

    rr = uniform(0, 1.0)
    if rr > g_w : 
        v문배술헤리티지40 = 1
    else : 
        v문배술헤리티지40 = 0 

    rr = uniform(0, 1.0)
    if rr > g_w : 
        v안동소주 = 1
    else : 
        v안동소주 = 0 

    rr = uniform(0, 1.0)
    if rr > g_w : 
        v설레온 = 1
    else : 
        v설레온 = 0 

    rr = uniform(0, 1.0)
    if rr > g_w : 
        v고소리술 = 1
    else : 
        v고소리술 = 0 

    rr = uniform(0, 1.0)
    if rr > g_w : 
        v이도 = 1
    else : 
        v이도 = 0 

    rr = uniform(0, 1.0)
    if rr > g_w : 
        v고구마증류주 = 1
    else : 
        v고구마증류주 = 0 

    rr = uniform(0, 1.0)
    if rr > g_w : 
        v담솔 = 1
    else : 
        v담솔 = 0 

    rr = uniform(0, 1.0)
    if rr > g_w : 
        v고울달오크 = 1
    else : 
        v고울달오크 = 0 

    rr = uniform(0, 1.0)
    if rr > g_w : 
        v고울달백자 = 1
    else : 
        v고울달백자 = 0 

    rr = uniform(0, 1.0)
    if rr > g_w : 
        v문경바람백자 = 1
    else : 
        v문경바람백자 = 0 

    rr = uniform(0, 1.0)
    if rr > g_w : 
        v문경바람오크 = 1
    else : 
        v문경바람오크 = 0 

    rr = uniform(0, 1.0)
    if rr > g_w : 
        v화주 = 1
    else : 
        v화주 = 0 

    rr = uniform(0, 1.0)
    if rr > g_w : 
        v추사40 = 1
    else : 
        v추사40 = 0 

    rr = uniform(0, 1.0)
    if rr > g_w : 
        v매실원주13 = 1
    else : 
        v매실원주13 = 0 

    rr = uniform(0, 1.0)
    if rr > g_w : 
        v서울의밤 = 1
    else : 
        v서울의밤 = 0 

    rr = uniform(0, 1.0)
    if rr > g_w : 
        v미르25 = 1
    else : 
        v미르25 = 0 

    rr = uniform(0, 1.0)
    if rr > g_w : 
        v미르40 = 1
    else : 
        v미르40 = 0 

    rr = uniform(0, 1.0)
    if rr > g_w : 
        v미르54 = 1
    else : 
        v미르54 = 0 

    rr = uniform(0, 1.0)
    if rr > g_w : 
        v술샘16 = 1
    else : 
        v술샘16 = 0 



# ----와인----

    rr = uniform(0, 1.0)
    if rr > w_w : 
        v오미로제연 = 1
    else : 
        v오미로제연 = 0 

    rr = uniform(0, 1.0)
    if rr > w_w : 
        v2016크라테산머루레드와인스위트 = 1
    else : 
        v2016크라테산머루레드와인스위트 = 0 

    rr = uniform(0, 1.0)
    if rr > w_w : 
        v혼다주 = 1
    else : 
        v혼다주 = 0 

    rr = uniform(0, 1.0)
    if rr > w_w : 
        v더그런치 = 1
    else : 
        v더그런치 = 0 

    rr = uniform(0, 1.0)
    if rr > w_w : 
        v스위마마 = 1
    else : 
        v스위마마 = 0 

    rr = uniform(0, 1.0)
    if rr > w_w : 
        v댄싱파파 = 1
    else : 
        v댄싱파파 = 0 

    rr = uniform(0, 1.0)
    if rr > w_w : 
        v마셔블랑 = 1
    else : 
        v마셔블랑 = 0 

    rr = uniform(0, 1.0)
    if rr > w_w : 
        v젤코바프리미엄레드 = 1
    else : 
        v젤코바프리미엄레드 = 0 

    rr = uniform(0, 1.0)
    if rr > w_w : 
        v고도리프리미엄청수화이트 = 1
    else : 
        v고도리프리미엄청수화이트 = 0 

    rr = uniform(0, 1.0)
    if rr > w_w : 
        v젤코바스위트와인 = 1
    else : 
        v젤코바스위트와인 = 0 

    rr = uniform(0, 1.0)
    if rr > w_w : 
        v씨엘고도리와이너리화이트 = 1
    else : 
        v씨엘고도리와이너리화이트 = 0 

    rr = uniform(0, 1.0)
    if rr > w_w : 
        v고도리복숭아와인 = 1
    else : 
        v고도리복숭아와인 = 0 

    rr = uniform(0, 1.0)
    if rr > w_w : 
        vLESDOM내추럴스파클링로제 = 1
    else : 
        vLESDOM내추럴스파클링로제 = 0 

    rr = uniform(0, 1.0)
    if rr > w_w : 
        vLESDOM로제시드르 = 1
    else : 
        vLESDOM로제시드르 = 0 

    rr = uniform(0, 1.0)
    if rr > w_w : 
        vLESDOM시드르 = 1
    else : 
        vLESDOM시드르 = 0 

    rr = uniform(0, 1.0)
    if rr > w_w : 
        v참뽕와인 = 1
    else : 
        v참뽕와인 = 0 

    rr = uniform(0, 1.0)
    if rr > w_w : 
        v세인트하우스아로니아와인 = 1
    else : 
        v세인트하우스아로니아와인 = 0 

    rr = uniform(0, 1.0)
    if rr > w_w : 
        v세인트하우스오미자와인 = 1
    else : 
        v세인트하우스오미자와인 = 0 

    rr = uniform(0, 1.0)
    if rr > w_w : 
        v세인트하우스모과와인 = 1
    else : 
        v세인트하우스모과와인 = 0 

    rr = uniform(0, 1.0)
    if rr > w_w : 
        v세인트하우스가시오가피와인 = 1
    else : 
        v세인트하우스가시오가피와인 = 0 

    rr = uniform(0, 1.0)
    if rr > w_w : 
        v세인트하우스딸기와인 = 1
    else : 
        v세인트하우스딸기와인 = 0 

    rr = uniform(0, 1.0)
    if rr > w_w : 
        v한스오차드애플 = 1
    else : 
        v한스오차드애플 = 0 

    rr = uniform(0, 1.0)
    if rr > w_w : 
        v애피소드애플 = 1
    else : 
        v애피소드애플 = 0 

    rr = uniform(0, 1.0)
    if rr > w_w : 
        v애피소드상그리아 = 1
    else : 
        v애피소드상그리아 = 0 

    rr = uniform(0, 1.0)
    if rr > w_w : 
        v오미로제프리미엄와인 = 1
    else : 
        v오미로제프리미엄와인 = 0 

    rr = uniform(0, 1.0)
    if rr > w_w : 
        v허니비와인 = 1
    else : 
        v허니비와인 = 0 

    rr = uniform(0, 1.0)
    if rr > w_w : 
        v오미로제스파클링결 = 1
    else : 
        v오미로제스파클링결 = 0 

    rr = uniform(0, 1.0)
    if rr > w_w : 
        v허니문와인 = 1
    else : 
        v허니문와인 = 0 

    rr = uniform(0, 1.0)
    if rr > w_w : 
        v추사애플와인 = 1
    else : 
        v추사애플와인 = 0 

    rr = uniform(0, 1.0)
    if rr > w_w : 
        v추사블루스위트 = 1
    else : 
        v추사블루스위트 = 0 



    
    userdata.loc[i] = {
        'eamil' : i,
        '오매백주' : v오매백주,
        '오산막걸리' : v오산막걸리,
        '세종대왕어주 탁주' : v세종대왕어주탁주, 
        '술공방 9.0' : v술공방, 
        '수제탁주 바랑' : v수제탁주바랑, 
        '백년향' :v백년향, 
        '문희 가향주' :v문희가향주, 
        '구름을 벗삼아':v구름을벗삼아, 
        '문희 탁주' : v문희탁주, 
        '오미자 생막걸리': v오미자생막걸리, 
        '오희': v오희, 
        '복순도가 손 막걸리': v복순도가손막걸리, 
        '담은': v담은, 
        '펀치 쌀바나나': v펀치쌀바나나, 
        '세종 알밤주': v세종알밤주, 
        '괴산 세종 찰옥수수': v괴산세종찰옥수수, 
        '조은술 세종 바나나': v조은술세종바나나, 
        '우도 땅콩 전통주': v우도땅콩전통주, 
        '우리술 오늘 탁주': v우리술오늘탁주, 
        '기다림 34': v기다림34, 
        '기다림 25': v기다림25, 
        '기다림 16': v기다림16, 
        '택이': v택이, 
        '천비향 탁주': v천비향탁주, 
        '술그리다 ': v술그리다, 
        '술예쁘다': v술예쁘다, 
        '술취한 원숭이': v술취한원숭이, 
        '삼양춘 생탁주': v삼양춘생탁주, 
        '토박이 한산소곡주': v토박이한산소곡주, 
        '삼양춘 청주': v삼양춘청주, 
        '복단지': v복단지, 
        '경성과하주': v경성과하주, 
        '세종대왕어주 약주': v세종대왕어주약주, 
        '구기홍주': v구기홍주, 
        '하타': v하타, 
        '단상지교': v단상지교, 
        '고흥 유자주': v고흥유자주, 
        '수제 약주 별바랑': v수제약주별바랑, 
        '삼양춘 생약주': v삼양춘생약주, 
        '순향주': v순향주, 
        '우렁이쌀 청주': v우렁이쌀청주, 
        '술아 국화주': v술아국화주, 
        '맑은 문희주': v맑은문희주, 
        '대윤가야곡 왕주': v대윤가야곡왕주, 
        '니모메': v니모메, 
        '오메기술13 세트': v오메기술13세트, 
        '청명주 약주': v청명주약주, 
        '술아 순곡주': v술아순곡주, 
        '우리술 오늘 약주': v우리술오늘약주, 
        '술아 연화주': v술아연화주, 
        '술아 매화주': v술아매화주, 
        '솔송주': v솔송주, 
        '천비향 약주': v천비향약주, 
        '살아있는 기운 한 모금! 홍삼명주': v살아있는기운한모금홍삼명주, 
        '감사': v감사, 
        '면천두견주': v면천두견주, 
        '부자진': v부자진, 
        '꿀샘16': v꿀샘16, 
        '독산53': v독산53, 
        '독산30': v독산30, 
        '신례명주': v신례명주,
        '진맥소주22': v진맥소주22, 
        '진맥소주40': v진맥소주40, 
        '진맥소주53': v진맥소주53, 
        '귀감': v귀감, 
        '겨울소주': v겨울소주, 
        '설성사또': v설성사또, 
        '병영소주': v병영소주, 
        '문배술 헤리티지23': v문배술헤리티지23, 
        '문배술 헤리티지25': v문배술헤리티지25, 
        '문배술 헤리티지40': v문배술헤리티지40, 
        '안동소주': v안동소주, 
        '설레온': v설레온, 
        '고소리술': v고소리술, 
        '이도': v이도, 
        '고구마증류주': v고구마증류주, 
        '담솔': v담솔, 
        '고울달오크': v고울달오크, 
        '고울달백자': v고울달백자, 
        '문경바람백자': v문경바람백자, 
        '문경바람오크': v문경바람오크, 
        '화주': v화주, 
        '추사40': v추사40, 
        '매실원주13': v매실원주13, 
        '서울의밤': v서울의밤, 
        '미르25': v미르25, 
        '미르40': v미르40, 
        '미르54': v미르54, 
        '술샘16': v술샘16, 
        '오미로제연': v오미로제연, 
        '2016크라테산머루레드와인스위트': v2016크라테산머루레드와인스위트, 
        '혼다주': v혼다주, 
        '요새로제': v요새로제, 
        '더그런치': v더그런치, 
        '스위마마': v스위마마, 
        '댄싱파파': v댄싱파파, 
        '마셔블랑': v마셔블랑, 
        '젤코바프리미엄레드': v젤코바프리미엄레드, 
        '고도리프리미엄청수화이트': v고도리프리미엄청수화이트, 
        '젤코바스위트와인': v젤코바스위트와인, 
        '씨엘고도리와이너리화이트': v씨엘고도리와이너리화이트, 
        '고도리복숭아와인': v고도리복숭아와인, 
        'LESDOM 내추럴 스파클링 로제': vLESDOM내추럴스파클링로제, 
        'LESDOM 로제시드르': vLESDOM로제시드르, 
        'LESDOM 시드르': vLESDOM시드르, 
        '참뽕와인': v참뽕와인, 
        '세인트하우스 아로니아와인': v세인트하우스아로니아와인, 
        '세인트하우스 오미자와인': v세인트하우스오미자와인, 
        '세인트하우스 모과와인': v세인트하우스모과와인, 
        '세인트하우스 가시오가피와인': v세인트하우스가시오가피와인, 
        '세인트하우스 딸기와인': v세인트하우스딸기와인, 
        '한스오차드 애플': v한스오차드애플, 
        '애피소드애플': v애피소드애플, 
        '애피소드상그리아': v애피소드상그리아, 
        '오미로제프리미엄와인': v오미로제스파클링결, 
        '허니비와인': v허니비와인, 
        '오미로제스파클링결': v오미로제스파클링결, 
        '허니문와인': v허니문와인, 
        '추사애플와인': v추사애플와인, 
        '추사블루스위트': v추사블루스위트

    }

userdata = pd.DataFrame(columns = data_columns)

userdata.to_csv("./userNewData3.csv")
