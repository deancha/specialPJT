# -*- coding: utf-8 -*-

from Setdata.settingdata import get_drink_dataframe
from Liquor.serializer import Liquorserializer
from Liquor import models
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import MinMaxScaler
import sys
import os
import numpy as np
import pandas as pd


def recommendation_drink_of_contents_based(keywordnum="", stopword=[], top=6):
    # 실제 각행렬간 유사도 계산된것은 이미 DB에 있거나 pickle에 저장된상태
    # 새로운술이 들어오거나 기존의 술이 삭제되었을때에, 계산해둔다.

    columnList = ["출처지역", "종류", "도수(%)", "가격", "원재료", "단맛", "산미", "탁도",
                  "탄산감", "담백", "바디", "씁쓸", "화려", "스파이시", "고소", "신맛", "타닌", "향", "설명"]
    indexList = ["1", "0", '오매백주', '오산막걸리', '세종대왕어주 탁주', '술공방 9.0', '수제탁주 바랑', '백년향', '문희 가향주', '구름을 벗삼아', '문희 탁주', '오미자 생막걸리', '오희', '복순도가 손 막걸리', '담은', '펀치 쌀바나나', '세종 알밤주', '괴산 세종 찰옥수수', '조은술 세종 바나나', '우도 땅콩 전통주', '우리술 오늘 탁주', '기다림 34', '기다림 25', '기다림 16', '택이', '천비향 탁주', '술그리다 ', '술예쁘다', '술취한 원숭이', '삼양춘 생탁주', '토박이 한산소곡주', '삼양춘 청주', '복단지', '경성과하주', '세종대왕어주 약주', '구기홍주', '하타', '단상지교', '고흥 유자주', '수제 약주 별바랑', '삼양춘 생약주', '순향주', '우렁이쌀 청주', '술아 국화주', '맑은 문희주', '대윤가야곡 왕주', '니모메', '오메기술13 세트', '청명주 약주', '술아 순곡주', '우리술 오늘 약주', '술아 연화주', '술아 매화주', '솔송주', '천비향 약주', '살아있는 기운 한 모금! 홍삼명주', '감사', '면천두견주', '부자진', '꿀샘16', '독산53', '독산30', '신례명주',
                 '진맥소주22', '진맥소주40', '진맥소주53', '귀감', '겨울소주', '설성사또', '병영소주', '문배술 헤리티지23', '문배술 헤리티지25', '문배술 헤리티지40', '안동소주', '설레온', '고소리술', '이도', '고구마증류주', '담솔', '고울달오크', '고울달백자', '문경바람백자', '문경바람오크', '화주', '추사40', '매실원주13', '서울의밤', '미르25', '미르40', '미르54', '술샘16', '오미로제연', '2016크라테산머루레드와인스위트', '혼다주', '요새로제', '더그런치', '스위마마', '댄싱파파', '마셔블랑', '젤코바프리미엄레드', '고도리프리미엄청수화이트', '젤코바스위트와인', '씨엘고도리와이너리화이트', '고도리복숭아와인', 'LESDOM 내추럴 스파클링 로제', 'LESDOM 로제시드르', 'LESDOM 시드르', '참뽕와인', '세인트하우스 아로니아와인', '세인트하우스 오미자와인', '세인트하우스 모과와인', '세인트하우스 가시오가피와인', '세인트하우스 딸기와인', '한스오차드 애플', '애피소드애플', '애피소드상그리아', '오미로제프리미엄와인', '허니비와인', '오미로제스파클링결', '허니문와인', '추사애플와인', '추사블루스위트']

    # DB에서 가져와야한다.
    drink_dataframe = get_drink_dataframe()

    keyword = indexList[keywordnum+2]
    # 사용자가 못먹는 원재료가 들어간 술은 추천에서 제외
    drink_dataframe.drop(index=[indexList[i+2] for i, item in enumerate(
        drink_dataframe["원재료"]) if len(list(set(stopword) & set(item.split(",")))) > 0], inplace=True)

    # 출처지역,종류,원재료를 제외한 숫자데이터에서 유사도 추출

    drink_dataframe_without_literal = drink_dataframe.drop(
        columns=["출처지역", "종류", "원재료"])

    # MinMax Scaling을 통한 데이터 정규화
    # 정규화시킬List를 선정
    scaler = MinMaxScaler()
    scaleList = ["도수(%)", "가격", "단맛", "산미", "탁도", "탄산감", "담백",
                 "바디", "씁쓸", "화려", "스파이시", "고소", "신맛", "타닌", "향"]
    drink_dataframe_without_literal[scaleList] = scaler.fit_transform(
        drink_dataframe_without_literal[scaleList])

    drink_datafrmae_with_normalization = drink_dataframe_without_literal[scaleList]

    # 피어슨&코사인 유사도 계산 dictionary
    similarity_dict = dict()

    # 피어스 유사도 추출 후 가장 항목이 높은 5가지 전통주 추천
    pearson_similarity_metrix = drink_datafrmae_with_normalization.T.corr(
        method="pearson").to_numpy()
    index = indexList.index(keyword)-2

    topid = sorted(range(len(
        pearson_similarity_metrix[index])), key=lambda i: pearson_similarity_metrix[index][i])[-top:]
    recommendation_drink_of_contents_based_top_five = []
    for i in range(top-2, 0, -1):
        recommendation_drink_of_contents_based_top_five.append([np.array(indexList[2:])[
                                                               topid][:-1][i], round(pearson_similarity_metrix[index][topid][:-1][i]*100, 3)])
    similarity_dict["pearson"] = recommendation_drink_of_contents_based_top_five

    # 코사인 유사도 추출후 가장 항목이 높은 5가지 전통주 추천

    cosine_similarity_metrix = cosine_similarity(
        drink_datafrmae_with_normalization)

    # Test용 index 한개 similarity metrix의 행 번호
    index = indexList.index(keyword)-2

    topid = sorted(range(len(
        cosine_similarity_metrix[index])), key=lambda i: cosine_similarity_metrix[index][i])[-top:]
    recommendation_drink_of_contents_based_top_five = []
    for i in range(top-2, 0, -1):
        recommendation_drink_of_contents_based_top_five.append([np.array(indexList[2:])[
                                                               topid][:-1][i], round(cosine_similarity_metrix[index][topid][:-1][i]*100, 3)])
    similarity_dict["cosine"] = recommendation_drink_of_contents_based_top_five
    return similarity_dict


if __name__ == "__main__":
    print(os.getcwd())
    # print(recommendation_drink_of_contents_based(keywordnum="1"))
    query_set = Liquor.objects.all()
    serializer = Liquorserializer(query_set, many=True)
    print(serializer.data)
