import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics.pairwise import cosine_similarity
from Setdata.settingdata import get_cforder_dataframe

def recommendation_drink_of_collaborative_filtering(useremail, top=6):
    
   
    # DB에서 가져와야한다.
    user_purchased_dataframe = get_cforder_dataframe()
    user_target_email = useremail
    
    # 
    user_purchased_dataframe_without_literal = user_purchased_dataframe.drop(
        columns=["kakaoemail"])

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