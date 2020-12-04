# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework import viewsets

# 유사도 계산을 위함 module
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import MinMaxScaler
import sys
import os
import numpy as np
import pandas as pd

# redis cache
from django.core.cache import cache

## 데이터를 DB에서 불러와서 추천
from Liquor import models ,serializer

## 시간 측정 
import time

@api_view(['GET'])
@csrf_exempt
def recommend(Request, number):
    
    if Request.method == "GET":
        start = time.time()
        fromcache = cache.get(number)
        if fromcache is None:
            fromcache= recommendation_drink_of_contents_based(number) 
            print("Redis에 없어서 Redis에 저장완료")
            cache.set( number ,fromcache , 60*60 )
        
        lserializer = serializer.Liquorserializer(models.Liquor.objects.filter(liquornumber__in=fromcache), many=True)
        return JsonResponse(lserializer.data, safe=False)
   

@api_view(['GET'])
@csrf_exempt
def recommendwithavoid(Request, number, avoid):
    if Request.method == "GET":
        numlist = recommendation_drink_of_contents_based(keywordnum=number,stopword=avoid)
        lserializer = serializer.Liquorserializer(models.Liquor.objects.filter(liquornumber__in=numlist), many=True)
        return JsonResponse(lserializer.data, safe=False)
   

   
   
# 추천부분

def recommendation_drink_of_contents_based(LiquorNum="", stopword="", top=6):
    # 실제 각행렬간 유사도 계산된것은 이미 REDIS에 저장된상태
    # 새로운술이 들어오거나 기존의 술이 삭제되었을때에, 계산해둔다.
    
    ## DB에서 가져와야한다.
    drink_dataframe = pd.DataFrame(models.Liquor.objects.all().values())
   
    drink_dataframe.set_index(drink_dataframe['liquornumber'] , inplace=True)
    drink_dataframe.drop(columns=['liquornumber'] , inplace=True)
   
   
    
    indexList = list(drink_dataframe['liquorname'])
    target = int(LiquorNum)-1
    keyword = indexList[target]
    print( keyword + " 의 와 유사한 술 계산 .... ")
    # 사용자가 못먹는 원재료가 들어간 술은 추천에서 제외
    if len(stopword) > 0 :  
        drink_dataframe.drop(index=[i for i, item in enumerate(
            drink_dataframe["liquoringredient"]) if len(list(set([stopword]) & set(item.split(",")))) > 0], inplace=True)
    
    # 출처지역,종류,원재료를 제외한 숫자데이터에서 유사도 추출
    exceptList = ["liquorname","liquorarea", "liquoringredient", "url",'liquorcategory']
    drink_dataframe_without_literal = drink_dataframe.drop(columns=exceptList)

    # MinMax Scaling을 통한 데이터 정규화
    scaleList = [ item for item in drink_dataframe_without_literal.columns if item not in exceptList ]
    
    # 정규화시킬List를 선정
    scaler = MinMaxScaler()
    drink_dataframe_without_literal[scaleList] = scaler.fit_transform(
        drink_dataframe_without_literal[scaleList])

    drink_datafrmae_with_normalization = drink_dataframe_without_literal[scaleList]

    # 피어슨&코사인 유사도 계산 dictionary
    similarity_dict = dict()

    # 피어스 유사도 추출 후 가장 항목이 높은 5가지 전통주 추천
    pearson_similarity_metrix = drink_datafrmae_with_normalization.T.corr(
        method="pearson").to_numpy()
    
  

    topid = sorted(range(len(pearson_similarity_metrix[target])), key=lambda i: pearson_similarity_metrix[target][i])[-top:]
    
    return [ i+1 for i in reversed(topid)][1:]

    # For Testing 
    # 코사인 유사도 추출후 가장 항목이 높은 5가지 전통주 추천
    cosine_similarity_metrix = cosine_similarity(drink_datafrmae_with_normalization)
    
    # 내가 찾을 술과 유사한것 1번째는 자기자신일꺼임
    index = LiquorNum

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
    #print(recommendation_drink_of_contents_based(keywordnum="1"))
    query_set = Liquor.objects.all()
    serializer = Liquorserializer(query_set, many=True)
    print(serializer.data)



