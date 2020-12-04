# -*- coding: utf-8 -*-
import pandas as pd
import sys, os
def get_drink_dataframe():
    columnList = ["출처지역", "종류", "도수(%)", "가격", "원재료", "단맛", "산미", "탁도",
              "탄산감", "담백", "바디", "씁쓸", "화려", "스파이시", "고소", "신맛", "타닌", "향", "설명","URL"]
    indexList = ["1", "0", '오매백주', '오산막걸리', '세종대왕어주 탁주', '술공방 9.0', '수제탁주 바랑', '백년향', '문희 가향주', '구름을 벗삼아', '문희 탁주', '오미자 생막걸리', '오희', '복순도가 손 막걸리', '담은', '펀치 쌀바나나', '세종 알밤주', '괴산 세종 찰옥수수', '조은술 세종 바나나', '우도 땅콩 전통주', '우리술 오늘 탁주', '기다림 34', '기다림 25', '기다림 16', '택이', '천비향 탁주', '술그리다 ', '술예쁘다', '술취한 원숭이', '삼양춘 생탁주', '토박이 한산소곡주', '삼양춘 청주', '복단지', '경성과하주', '세종대왕어주 약주', '구기홍주', '하타', '단상지교', '고흥 유자주', '수제 약주 별바랑', '삼양춘 생약주', '순향주', '우렁이쌀 청주', '술아 국화주', '맑은 문희주', '대윤가야곡 왕주', '니모메', '오메기술13 세트', '청명주 약주', '술아 순곡주', '우리술 오늘 약주', '술아 연화주', '술아 매화주', '솔송주', '천비향 약주', '살아있는 기운 한 모금! 홍삼명주', '감사', '면천두견주', '부자진', '꿀샘16', '독산53', '독산30', '신례명주',
             '진맥소주22', '진맥소주40', '진맥소주53', '귀감', '겨울소주', '설성사또', '병영소주', '문배술 헤리티지23', '문배술 헤리티지25', '문배술 헤리티지40', '안동소주', '설레온', '고소리술', '이도', '고구마증류주', '담솔', '고울달오크', '고울달백자', '문경바람백자', '문경바람오크', '화주', '추사40', '매실원주13', '서울의밤', '미르25', '미르40', '미르54', '술샘16', '오미로제연', '2016크라테산머루레드와인스위트', '혼디주', '요새로제', '더그런치', '스윗마마', '댄싱파파', '마셔블랑', '젤코바프리미엄레드', '고도리프리미엄청수화이트', '젤코바스위트와인', '씨엘고도리와이너리화이트', '고도리복숭아와인', 'LESDOM 내추럴 스파클링 로제', 'LESDOM 로제시드르', 'LESDOM 시드르', '참뽕와인', '세인트하우스 아로니아와인', '세인트하우스 오미자와인', '세인트하우스 모과와인', '세인트하우스 가시오가피와인', '세인트하우스 딸기와인', '한스오차드 애플', '애피소드애플', '애피소드상그리아', '오미로제프리미엄와인', '허니비와인', '오미로제스파클링결', '허니문와인', '추사애플와인', '추사블루스위트']
    DrinkDf = pd.read_excel("Setdata/liquordata.xlsx", sheet_name="시트1", header=None, index_col=1)
    DrinkDf.drop(columns=0, inplace=True)
    DrinkDf.index = indexList
    DrinkDf.columns = columnList
    DrinkDf.drop(index=["1", "0"], inplace=True)
    DrinkDf.dropna(axis=1, inplace=True)
    return DrinkDf

def get_order_dataframe():
    OrderDf = pd.read_excel("Setdata/orderdata.xlsx", sheet_name="Sheet1")
    return OrderDf

def get_cforder_dataframe():
    # heavy 
    cforderDf = pd.read_excel("Setdata/userNewData5.xlsx", sheet_name="userNewData5")
    # light
    # cforderDf = pd.read_excel("Setdata/userorderdata2.xlsx", sheet_name="userNewData2")
    return cforderDf

def get_review_dataframe():
    reviewdf = pd.read_excel("Setdata/reviewdata.xlsx", sheet_name="reviewdata")
    return reviewdf


