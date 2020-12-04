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
from scipy.sparse.linalg import svds
from sklearn.preprocessing import MinMaxScaler
import sys
import os
import numpy as np
import pandas as pd

# redis cache
from django.core.cache import cache

## 데이터를 DB에서 불러와서 추천
from update import models
from Liquor import serializer
from Liquor import models as lmodels
#시간 측정
import time


@api_view(['GET'])
@csrf_exempt
def recommend(Request, email):
    print(email +" 의 유저기반추천시작")
    if Request.method == "GET":
        start = time.time()
        fromcache = cache.get("user"+email)
        # 추천의 유효성을 위해 3병이상 시킨것도 체크해주어야 한다.
        if fromcache is None:
            fromcache= recommendation_drink_of_collaborative_filtering(email) 
            print("Redis에 없어서 Redis에 저장완료")
            cache.set("user"+email ,fromcache , 60*60 )
        print("걸린시간 :", time.time() - start)
        lserializer = serializer.Liquorserializer(lmodels.Liquor.objects.filter(liquornumber__in=fromcache), many=True)
        return JsonResponse(lserializer.data, safe=False)
   
def recommendation_drink_of_collaborative_filtering(useremail, top=6):
    
    # DB에서 가져와야한다.
    user_purchased_dataframe = pd.DataFrame(models.cforder.objects.all().values())
    user_target_email = useremail
    
    indexList = list(user_purchased_dataframe['kakaoemail'])
    targetindex = indexList.index(user_target_email)
    # 이메일은 제거
    user_purchased_dataframe_without_literal = user_purchased_dataframe.drop(
        columns=["id","kakaoemail"])
    user_liquor_df = user_purchased_dataframe_without_literal
    liquor_user_df = user_purchased_dataframe_without_literal.T
    
    # user avgrating 정보가 필요
    # col 별로 뺀값이 필요 
    matrix = user_liquor_df.as_matrix()
    user_liquor_df_mean = np.mean( matrix , axis=1)
    matrix_liquor_df_mean = matrix - user_liquor_df_mean.reshape(-1,1)
    
    # svd 
    u , s , vt = svds(matrix_liquor_df_mean, k=100)
    s = np.diag(s)
    
    # 다시 원래 행렬로 돌리면서 값이 높은거 추천해볼까?
    svd_user_predict = np.dot(np.dot(u,s),vt) + user_liquor_df_mean.reshape(-1,1)
    user_data_predict = svd_user_predict[targetindex]
    user_purchased_data =list(user_purchased_dataframe_without_literal.iloc[targetindex])
    # user_data_predict 값이 큰 index중 user_purchased_data에 없는것?
    result = sorted(range(len(list(user_data_predict))), key=lambda i: user_data_predict[i] )
    # result의 맨뒤부터 5개 not in 유저 구매
    return  [i for i in reversed(result) if user_purchased_data[i]==0.0][:5]
   
    