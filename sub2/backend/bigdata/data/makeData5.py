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
    

    # 이메일 값 넣는거임
    list_data.append([])
    list_data[i].append(i)


    # ---------------------여기부터 값 매기기 시작
    rr = uniform(0, 1.0)
    if rr > t_w : 
        v오매백주 = uniform(1.0, 5.0)
    else : 
        v오매백주 = 0                    
    list_data[i].append(v오매백주)

    rr = uniform(0, 1.0)
    if rr > t_w : 
        v오산막걸리 = uniform(1.0, 5.0)
    else : 
        v오산막걸리 = 0
    list_data[i].append(v오산막걸리)

    rr = uniform(0, 1.0)
    if rr > t_w : 
        v세종대왕어주탁주 = uniform(1.0, 5.0)
    else : 
        v세종대왕어주탁주 = 0
    list_data[i].append(v세종대왕어주탁주)

    rr = uniform(0, 1.0)
    if rr > t_w : 
        v술공방 = uniform(1.0, 5.0)
    else : 
        v술공방 = 0
    list_data[i].append(v술공방)

    rr = uniform(0, 1.0)
    if rr > t_w : 
        v수제탁주바랑 = uniform(1.0, 5.0)
    else : 
        v수제탁주바랑 = 0
    list_data[i].append(v수제탁주바랑)
    
    rr = uniform(0, 1.0)
    if rr > t_w : 
        v백년향 = uniform(1.0, 5.0)
    else : 
        v백년향 = 0
    list_data[i].append(v백년향)

    rr = uniform(0, 1.0)
    if rr > t_w : 
        v문희가향주 = uniform(1.0, 5.0)
    else : 
        v문희가향주 = 0
    list_data[i].append(v문희가향주)
    
    rr = uniform(0, 1.0)
    if rr > t_w : 
        v구름을벗삼아 = uniform(1.0, 5.0)
    else : 
        v구름을벗삼아 = 0
    list_data[i].append(v구름을벗삼아)

    rr = uniform(0, 1.0)
    if rr > t_w : 
        v문희탁주 = uniform(1.0, 5.0)
    else : 
        v문희탁주 = 0
    list_data[i].append(v문희탁주)
    
    rr = uniform(0, 1.0)
    if rr > t_w : 
        v오미자생막걸리 = uniform(1.0, 5.0)
    else : 
        v오미자생막걸리 = 0
    list_data[i].append(v오미자생막걸리)

    rr = uniform(0, 1.0)
    if rr > t_w : 
        v오희 = uniform(1.0, 5.0)
    else : 
        v오희 = 0
    list_data[i].append(v오희)

    rr = uniform(0, 1.0)
    if rr > t_w : 
        v복순도가손막걸리 = uniform(1.0, 5.0)
    else : 
        v복순도가손막걸리 = 0
    list_data[i].append(v복순도가손막걸리)

    rr = uniform(0, 1.0)
    if rr > t_w : 
        v담은 = uniform(1.0, 5.0)
    else : 
        v담은 = 0
    list_data[i].append(v담은)

    rr = uniform(0, 1.0)
    if rr > t_w : 
        v펀치쌀바나나 = uniform(1.0, 5.0)
    else : 
        v펀치쌀바나나 = 0
    list_data[i].append(v펀치쌀바나나)

    rr = uniform(0, 1.0)
    if rr > t_w : 
        v세종알밤주 = uniform(1.0, 5.0)
    else : 
        v세종알밤주 = 0 
    list_data[i].append(v세종알밤주)


    rr = uniform(0, 1.0)
    if rr > t_w : 
        v괴산세종찰옥수수 = uniform(1.0, 5.0)
    else : 
        v괴산세종찰옥수수 = 0 
    list_data[i].append(v괴산세종찰옥수수)
    
    rr = uniform(0, 1.0)
    if rr > t_w : 
        v조은술세종바나나 = uniform(1.0, 5.0)
    else : 
        v조은술세종바나나 = 0 
    list_data[i].append(v조은술세종바나나)

    rr = uniform(0, 1.0)
    if rr > t_w : 
        v우도땅콩전통주 = uniform(1.0, 5.0)
    else : 
        v우도땅콩전통주 = 0 
    list_data[i].append(v우도땅콩전통주)

    rr = uniform(0, 1.0)
    if rr > t_w : 
        v우리술오늘탁주 = uniform(1.0, 5.0)
    else : 
        v우리술오늘탁주 = 0 
    list_data[i].append(v우리술오늘탁주)

    rr = uniform(0, 1.0)
    if rr > t_w : 
        v기다림34 = uniform(1.0, 5.0)
    else : 
        v기다림34 = 0 
    list_data[i].append(v기다림34)

    rr = uniform(0, 1.0)
    if rr > t_w : 
        v기다림25 = uniform(1.0, 5.0)
    else : 
        v기다림25 = 0 
    list_data[i].append(v기다림25)

    rr = uniform(0, 1.0)
    if rr > t_w : 
        v기다림16 = uniform(1.0, 5.0)
    else : 
        v기다림16 = 0 
    list_data[i].append(v기다림16)

    rr = uniform(0, 1.0)
    if rr > t_w : 
        v택이 = uniform(1.0, 5.0)
    else : 
        v택이 = 0 
    list_data[i].append(v택이)

    rr = uniform(0, 1.0)
    if rr > t_w : 
        v천비향탁주 = uniform(1.0, 5.0)
    else : 
        v천비향탁주 = 0 
    list_data[i].append(v천비향탁주)

    rr = uniform(0, 1.0)
    if rr > t_w : 
        v술그리다 = uniform(1.0, 5.0)
    else : 
        v술그리다 = 0 
    list_data[i].append(v술그리다)

    rr = uniform(0, 1.0)
    if rr > t_w : 
        v술예쁘다 = uniform(1.0, 5.0)
    else : 
        v술예쁘다 = 0 
    list_data[i].append(v술예쁘다)

    rr = uniform(0, 1.0)
    if rr > t_w : 
        v술취한원숭이 = uniform(1.0, 5.0)
    else : 
        v술취한원숭이 = 0
    list_data[i].append(v술취한원숭이)

    rr = uniform(0, 1.0)
    if rr > t_w : 
        v삼양춘생탁주 = uniform(1.0, 5.0)
    else : 
        v삼양춘생탁주 = 0 
    list_data[i].append(v삼양춘생탁주)

# -----------약주--------------
    rr = uniform(0, 1.0)
    if rr > y_w : 
        v토박이한산소곡주 = uniform(1.0, 5.0)
    else : 
        v토박이한산소곡주 = 0 
    list_data[i].append(v토박이한산소곡주)
    
    rr = uniform(0, 1.0)
    if rr > y_w : 
        v삼양춘청주 = uniform(1.0, 5.0)
    else : 
        v삼양춘청주 = 0 
    list_data[i].append(v삼양춘청주)

    rr = uniform(0, 1.0)
    if rr > y_w : 
        v복단지 = uniform(1.0, 5.0)
    else : 
        v복단지 = 0 
    list_data[i].append(v복단지)

    rr = uniform(0, 1.0)
    if rr > y_w : 
        v경성과하주 = uniform(1.0, 5.0)
    else : 
        v경성과하주 = 0 
    list_data[i].append(v경성과하주)

    rr = uniform(0, 1.0)
    if rr > y_w : 
        v세종대왕어주약주 = uniform(1.0, 5.0)
    else : 
        v세종대왕어주약주 = 0 
    list_data[i].append(v세종대왕어주약주)

    rr = uniform(0, 1.0)
    if rr > y_w : 
        v구기홍주 = uniform(1.0, 5.0)
    else : 
        v구기홍주 = 0 
    list_data[i].append(v구기홍주)

    rr = uniform(0, 1.0)
    if rr > y_w : 
        v하타 = uniform(1.0, 5.0)
    else : 
        v하타 = 0 
    list_data[i].append(v하타)

    rr = uniform(0, 1.0)
    if rr > y_w : 
        v단상지교 = uniform(1.0, 5.0)
    else : 
        v단상지교 = 0 
    list_data[i].append(v단상지교)

    rr = uniform(0, 1.0)
    if rr > y_w : 
        v고흥유자주 = uniform(1.0, 5.0)
    else : 
        v고흥유자주 = 0 
    list_data[i].append(v고흥유자주)

    rr = uniform(0, 1.0)
    if rr > y_w : 
        v수제약주별바랑 = uniform(1.0, 5.0)
    else : 
        v수제약주별바랑 = 0 
    list_data[i].append(v수제약주별바랑)

    rr = uniform(0, 1.0)
    if rr > y_w : 
        v삼양춘생약주 = uniform(1.0, 5.0)
    else : 
        v삼양춘생약주 = 0 
    list_data[i].append(v삼양춘생약주)

    rr = uniform(0, 1.0)
    if rr > y_w : 
        v순향주 = uniform(1.0, 5.0)
    else : 
        v순향주 = 0 
    list_data[i].append(v순향주)

    rr = uniform(0, 1.0)
    if rr > y_w : 
        v우렁이쌀청주 = uniform(1.0, 5.0)
    else : 
        v우렁이쌀청주 = 0 
    list_data[i].append(v우렁이쌀청주)

    rr = uniform(0, 1.0)
    if rr > y_w : 
        v술아국화주 = uniform(1.0, 5.0)
    else : 
        v술아국화주 = 0
    list_data[i].append(v술아국화주)

    rr = uniform(0, 1.0)
    if rr > y_w : 
        v맑은문희주 = uniform(1.0, 5.0)
    else : 
        v맑은문희주 = 0 
    list_data[i].append(v맑은문희주)

    rr = uniform(0, 1.0)
    if rr > y_w : 
        v대윤가야곡왕주 = uniform(1.0, 5.0)
    else : 
        v대윤가야곡왕주 = 0 
    list_data[i].append(v대윤가야곡왕주)

    rr = uniform(0, 1.0)
    if rr > y_w : 
        v니모메 = uniform(1.0, 5.0)
    else : 
        v니모메 = 0 
    list_data[i].append(v니모메)

    rr = uniform(0, 1.0)
    if rr > y_w : 
        v오메기술13세트 = uniform(1.0, 5.0)
    else : 
        v오메기술13세트 = 0 
    list_data[i].append(v오메기술13세트)

    rr = uniform(0, 1.0)
    if rr > y_w : 
        v청명주약주 = uniform(1.0, 5.0)
    else : 
        v청명주약주 = 0 
    list_data[i].append(v청명주약주)

    rr = uniform(0, 1.0)
    if rr > y_w : 
        v술아순곡주 = uniform(1.0, 5.0)
    else : 
        v술아순곡주 = 0 
    list_data[i].append(v술아순곡주)

    rr = uniform(0, 1.0)
    if rr > y_w : 
        v우리술오늘약주 = uniform(1.0, 5.0)
    else : 
        v우리술오늘약주 = 0 
    list_data[i].append(v우리술오늘약주)

    rr = uniform(0, 1.0)
    if rr > y_w : 
        v술아연화주 = uniform(1.0, 5.0)
    else : 
        v술아연화주 = 0 
    list_data[i].append(v술아연화주)

    rr = uniform(0, 1.0)
    if rr > y_w : 
        v술아매화주 = uniform(1.0, 5.0)
    else : 
        v술아매화주 = 0 
    list_data[i].append(v술아매화주)

    rr = uniform(0, 1.0)
    if rr > y_w : 
        v솔송주 = uniform(1.0, 5.0)
    else : 
        v솔송주 = 0 
    list_data[i].append(v솔송주)
    
    rr = uniform(0, 1.0)
    if rr > y_w : 
        v천비향약주 = uniform(1.0, 5.0)
    else : 
        v천비향약주 = 0 
    list_data[i].append(v천비향약주)

    rr = uniform(0, 1.0)
    if rr > y_w : 
        v살아있는기운한모금홍삼명주 = uniform(1.0, 5.0)
    else : 
        v살아있는기운한모금홍삼명주 = 0 
    list_data[i].append(v살아있는기운한모금홍삼명주)

    rr = uniform(0, 1.0)
    if rr > y_w : 
        v감사 = uniform(1.0, 5.0)
    else : 
        v감사 = 0 
    list_data[i].append(v감사)

    rr = uniform(0, 1.0)
    if rr > y_w : 
        v면천두견주 = uniform(1.0, 5.0)
    else : 
        v면천두견주 = 0 
    list_data[i].append(v면천두견주)
   


#-------증류주--------

    rr = uniform(0, 1.0)
    if rr > g_w : 
        v부자진 = uniform(1.0, 5.0)
    else : 
        v부자진 = 0 
    list_data[i].append(v부자진)

    rr = uniform(0, 1.0)
    if rr > g_w : 
        v꿀샘16 = uniform(1.0, 5.0)
    else : 
        v꿀샘16 = 0 
    list_data[i].append(v꿀샘16)

    rr = uniform(0, 1.0)
    if rr > g_w : 
        v독산53 = uniform(1.0, 5.0)
    else : 
        v독산53 = 0 
    list_data[i].append(v독산53)

    rr = uniform(0, 1.0)
    if rr > g_w : 
        v독산30 = uniform(1.0, 5.0)
    else : 
        v독산30 = 0 
    list_data[i].append(v독산30)

    rr = uniform(0, 1.0)
    if rr > g_w : 
        v신례명주 = uniform(1.0, 5.0)
    else : 
        v신례명주 = 0 
    list_data[i].append(v신례명주)

    rr = uniform(0, 1.0)
    if rr > g_w : 
        v진맥소주22 = uniform(1.0, 5.0)
    else : 
        v진맥소주22 = 0 
    list_data[i].append(v진맥소주22)

    rr = uniform(0, 1.0)
    if rr > g_w : 
        v진맥소주40 = uniform(1.0, 5.0)
    else : 
        v진맥소주40 = 0 
    list_data[i].append(v진맥소주40)

    rr = uniform(0, 1.0)
    if rr > g_w : 
        v진맥소주53 = uniform(1.0, 5.0)
    else : 
        v진맥소주53 = 0 
    list_data[i].append(v진맥소주53)

    rr = uniform(0, 1.0)
    if rr > g_w : 
        v귀감 = uniform(1.0, 5.0)
    else : 
        v귀감 = 0 
    list_data[i].append(v귀감)

    rr = uniform(0, 1.0)
    if rr > g_w : 
        v겨울소주 = uniform(1.0, 5.0)
    else : 
        v겨울소주 = 0 
    list_data[i].append(v겨울소주)

    rr = uniform(0, 1.0)
    if rr > g_w : 
        v설성사또 = uniform(1.0, 5.0)
    else : 
        v설성사또 = 0 
    list_data[i].append(v설성사또)

    rr = uniform(0, 1.0)
    if rr > g_w : 
        v병영소주 = uniform(1.0, 5.0)
    else : 
        v병영소주 = 0 
    list_data[i].append(v병영소주)

    rr = uniform(0, 1.0)
    if rr > g_w : 
        v문배술헤리티지23 = uniform(1.0, 5.0)
    else : 
        v문배술헤리티지23 = 0 
    list_data[i].append(v문배술헤리티지23)

    rr = uniform(0, 1.0)
    if rr > g_w : 
        v문배술헤리티지25 = uniform(1.0, 5.0)
    else : 
        v문배술헤리티지25 = 0 
    list_data[i].append(v문배술헤리티지25)

    rr = uniform(0, 1.0)
    if rr > g_w : 
        v문배술헤리티지40 = uniform(1.0, 5.0)
    else : 
        v문배술헤리티지40 = 0 
    list_data[i].append(v문배술헤리티지40)

    rr = uniform(0, 1.0)
    if rr > g_w : 
        v안동소주 = uniform(1.0, 5.0)
    else : 
        v안동소주 = 0 
    list_data[i].append(v안동소주)

    rr = uniform(0, 1.0)
    if rr > g_w : 
        v설레온 = uniform(1.0, 5.0)
    else : 
        v설레온 = 0 
    list_data[i].append(v설레온)

    rr = uniform(0, 1.0)
    if rr > g_w : 
        v고소리술 = uniform(1.0, 5.0)
    else : 
        v고소리술 = 0 
    list_data[i].append(v고소리술)

    rr = uniform(0, 1.0)
    if rr > g_w : 
        v이도 = uniform(1.0, 5.0)
    else : 
        v이도 = 0 
    list_data[i].append(v이도)

    rr = uniform(0, 1.0)
    if rr > g_w : 
        v고구마증류주 = uniform(1.0, 5.0)
    else : 
        v고구마증류주 = 0 
    list_data[i].append(v고구마증류주)

    rr = uniform(0, 1.0)
    if rr > g_w : 
        v담솔 = uniform(1.0, 5.0)
    else : 
        v담솔 = 0 
    list_data[i].append(v담솔)

    rr = uniform(0, 1.0)
    if rr > g_w : 
        v고울달오크 = uniform(1.0, 5.0)
    else : 
        v고울달오크 = 0 
    list_data[i].append(v고울달오크)

    rr = uniform(0, 1.0)
    if rr > g_w : 
        v고울달백자 = uniform(1.0, 5.0)
    else : 
        v고울달백자 = 0 
    list_data[i].append(v고울달백자)

    rr = uniform(0, 1.0)
    if rr > g_w : 
        v문경바람백자 = uniform(1.0, 5.0)
    else : 
        v문경바람백자 = 0 
    list_data[i].append(v문경바람백자)

    rr = uniform(0, 1.0)
    if rr > g_w : 
        v문경바람오크 = uniform(1.0, 5.0)
    else : 
        v문경바람오크 = 0 
    list_data[i].append(v문경바람오크)

    rr = uniform(0, 1.0)
    if rr > g_w : 
        v화주 = uniform(1.0, 5.0)
    else : 
        v화주 = 0 
    list_data[i].append(v화주)

    rr = uniform(0, 1.0)
    if rr > g_w : 
        v추사40 = uniform(1.0, 5.0)
    else : 
        v추사40 = 0 
    list_data[i].append(v추사40)

    rr = uniform(0, 1.0)
    if rr > g_w : 
        v매실원주13 = uniform(1.0, 5.0)
    else : 
        v매실원주13 = 0 
    list_data[i].append(v매실원주13)

    rr = uniform(0, 1.0)
    if rr > g_w : 
        v서울의밤 = uniform(1.0, 5.0)
    else : 
        v서울의밤 = 0 
    list_data[i].append(v서울의밤)

    rr = uniform(0, 1.0)
    if rr > g_w : 
        v미르25 = uniform(1.0, 5.0)
    else : 
        v미르25 = 0 
    list_data[i].append(v미르25)

    rr = uniform(0, 1.0)
    if rr > g_w : 
        v미르40 = uniform(1.0, 5.0)
    else : 
        v미르40 = 0 
    list_data[i].append(v미르40)

    rr = uniform(0, 1.0)
    if rr > g_w : 
        v미르54 = uniform(1.0, 5.0)
    else : 
        v미르54 = 0 
    list_data[i].append(v미르54)

    rr = uniform(0, 1.0)
    if rr > g_w : 
        v술샘16 = uniform(1.0, 5.0)
    else : 
        v술샘16 = 0 
    list_data[i].append(v술샘16)


# ----와인----

    rr = uniform(0, 1.0)
    if rr > w_w : 
        v오미로제연 = uniform(1.0, 5.0)
    else : 
        v오미로제연 = 0 
    list_data[i].append(v오미로제연)

    rr = uniform(0, 1.0)
    if rr > w_w : 
        v2016크라테산머루레드와인스위트 = uniform(1.0, 5.0)
    else : 
        v2016크라테산머루레드와인스위트 = 0 
    list_data[i].append(v2016크라테산머루레드와인스위트)

    rr = uniform(0, 1.0)
    if rr > w_w : 
        v혼다주 = uniform(1.0, 5.0)
    else : 
        v혼다주 = 0 
    list_data[i].append(v혼다주)

    rr = uniform(0, 1.0)
    if rr > w_w : 
        v요새로제 = uniform(1.0, 5.0)
    else : 
        v요새로제 = 0 
    list_data[i].append(v요새로제)

    rr = uniform(0, 1.0)
    if rr > w_w : 
        v더그런치 = uniform(1.0, 5.0)
    else : 
        v더그런치 = 0 
    list_data[i].append(v더그런치)

    rr = uniform(0, 1.0)
    if rr > w_w : 
        v스위마마 = uniform(1.0, 5.0)
    else : 
        v스위마마 = 0 
    list_data[i].append(v스위마마)

    rr = uniform(0, 1.0)
    if rr > w_w : 
        v댄싱파파 = uniform(1.0, 5.0)
    else : 
        v댄싱파파 = 0 
    list_data[i].append(v댄싱파파)

    rr = uniform(0, 1.0)
    if rr > w_w : 
        v마셔블랑 = uniform(1.0, 5.0)
    else : 
        v마셔블랑 = 0 
    list_data[i].append(v마셔블랑)

    rr = uniform(0, 1.0)
    if rr > w_w : 
        v젤코바프리미엄레드 = uniform(1.0, 5.0)
    else : 
        v젤코바프리미엄레드 = 0 
    list_data[i].append(v젤코바프리미엄레드)

    rr = uniform(0, 1.0)
    if rr > w_w : 
        v고도리프리미엄청수화이트 = uniform(1.0, 5.0)
    else : 
        v고도리프리미엄청수화이트 = 0 
    list_data[i].append(v고도리프리미엄청수화이트)

    rr = uniform(0, 1.0)
    if rr > w_w : 
        v젤코바스위트와인 = uniform(1.0, 5.0)
    else : 
        v젤코바스위트와인 = 0 
    list_data[i].append(v젤코바스위트와인)

    rr = uniform(0, 1.0)
    if rr > w_w : 
        v씨엘고도리와이너리화이트 = uniform(1.0, 5.0)
    else : 
        v씨엘고도리와이너리화이트 = 0 
    list_data[i].append(v씨엘고도리와이너리화이트)

    rr = uniform(0, 1.0)
    if rr > w_w : 
        v고도리복숭아와인 = uniform(1.0, 5.0)
    else : 
        v고도리복숭아와인 = 0 
    list_data[i].append(v고도리복숭아와인)

    rr = uniform(0, 1.0)
    if rr > w_w : 
        vLESDOM내추럴스파클링로제 = uniform(1.0, 5.0)
    else : 
        vLESDOM내추럴스파클링로제 = 0 
    list_data[i].append(vLESDOM내추럴스파클링로제)

    rr = uniform(0, 1.0)
    if rr > w_w : 
        vLESDOM로제시드르 = uniform(1.0, 5.0)
    else : 
        vLESDOM로제시드르 = 0 
    list_data[i].append(vLESDOM로제시드르)

    rr = uniform(0, 1.0)
    if rr > w_w : 
        vLESDOM시드르 = uniform(1.0, 5.0)
    else : 
        vLESDOM시드르 = 0 
    list_data[i].append(vLESDOM시드르)

    rr = uniform(0, 1.0)
    if rr > w_w : 
        v참뽕와인 = uniform(1.0, 5.0)
    else : 
        v참뽕와인 = 0 
    list_data[i].append(v참뽕와인)

    rr = uniform(0, 1.0)
    if rr > w_w : 
        v세인트하우스아로니아와인 = uniform(1.0, 5.0)
    else : 
        v세인트하우스아로니아와인 = 0 
    list_data[i].append(v세인트하우스아로니아와인)

    rr = uniform(0, 1.0)
    if rr > w_w : 
        v세인트하우스오미자와인 = uniform(1.0, 5.0)
    else : 
        v세인트하우스오미자와인 = 0 
    list_data[i].append(v세인트하우스오미자와인)

    rr = uniform(0, 1.0)
    if rr > w_w : 
        v세인트하우스모과와인 = uniform(1.0, 5.0)
    else : 
        v세인트하우스모과와인 = 0 
    list_data[i].append(v세인트하우스모과와인)

    rr = uniform(0, 1.0)
    if rr > w_w : 
        v세인트하우스가시오가피와인 = uniform(1.0, 5.0)
    else : 
        v세인트하우스가시오가피와인 = 0 
    list_data[i].append(v세인트하우스가시오가피와인)

    rr = uniform(0, 1.0)
    if rr > w_w : 
        v세인트하우스딸기와인 = uniform(1.0, 5.0)
    else : 
        v세인트하우스딸기와인 = 0 
    list_data[i].append(v세인트하우스딸기와인)

    rr = uniform(0, 1.0)
    if rr > w_w : 
        v한스오차드애플 = uniform(1.0, 5.0)
    else : 
        v한스오차드애플 = 0 
    list_data[i].append(v한스오차드애플)

    rr = uniform(0, 1.0)
    if rr > w_w : 
        v애피소드애플 = uniform(1.0, 5.0)
    else : 
        v애피소드애플 = 0 
    list_data[i].append(v애피소드애플)

    rr = uniform(0, 1.0)
    if rr > w_w : 
        v애피소드상그리아 = uniform(1.0, 5.0)
    else : 
        v애피소드상그리아 = 0 
    list_data[i].append(v애피소드상그리아)

    rr = uniform(0, 1.0)
    if rr > w_w : 
        v오미로제프리미엄와인 = uniform(1.0, 5.0)
    else : 
        v오미로제프리미엄와인 = 0 
    list_data[i].append(v오미로제프리미엄와인)

    rr = uniform(0, 1.0)
    if rr > w_w : 
        v허니비와인 = uniform(1.0, 5.0)
    else : 
        v허니비와인 = 0 
    list_data[i].append(v허니비와인)

    rr = uniform(0, 1.0)
    if rr > w_w : 
        v오미로제스파클링결 = uniform(1.0, 5.0)
    else : 
        v오미로제스파클링결 = 0 
    list_data[i].append(v오미로제스파클링결)

    rr = uniform(0, 1.0)
    if rr > w_w : 
        v허니문와인 = uniform(1.0, 5.0)
    else : 
        v허니문와인 = 0 
    list_data[i].append(v허니문와인)
    
    rr = uniform(0, 1.0)
    if rr > w_w : 
        v추사애플와인 = uniform(1.0, 5.0)
    else : 
        v추사애플와인 = 0 
    list_data[i].append(v추사애플와인)

    rr = uniform(0, 1.0)
    if rr > w_w : 
        v추사블루스위트 = uniform(1.0, 5.0)
    else : 
        v추사블루스위트 = 0 
    list_data[i].append(v추사블루스위트)


    


userdata = pd.DataFrame(columns = data_columns, data=list_data)

userdata.to_csv("./userNewData5.csv")
