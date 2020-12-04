# -*- coding: utf-8 -*-
from django.shortcuts import render
from RecommendationSystem.Content_Based_Recommendation import get_drink_dataframe

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from .serializer import ReviewSerializer
from rest_framework.parsers import JSONParser
from .models import review

# 리뷰 등록 - 인자 필요없음


@api_view(['POST'])
@csrf_exempt
def reviewInsert(request):
    if request.method == "POST":
        data = JSONParser().parse(request)
        serializer = ReviewSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors, status=404)

# 리뷰 수정 및 삭제기능 - review_id로 판별


@api_view(['PUT'])
@csrf_exempt
def reviewOneParam(request, review_id):
    obj = review.objects.get(pk=review_id)
    # print(review_id)
    if request.method == "PUT":
        # print(obj)
        serializer = ReviewSerializer(obj, data=JSONParser().parse(request))
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors, status=404)

    elif request.method == "DELETE":
        obj.delete()
        return JsonResponse({"message": "삭제완료"}, status=200)

# 리뷰 리스트 반환 - liquornumber로 찾아줌 - 시간순서대로 가져와야함


@api_view(['GET'])
@csrf_exempt
def reviewGetByLiquornumber(request, number):
    print(number)
    if request.method == "GET":
        objs = review.objects.filter(liquornumber=number)

        serializer = ReviewSerializer(objs, many=True)
        return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def reviewGetByUseremail(request, kakaoemail):
    print(kakaoemail)
    if request.method == "GET":
        objs = review.objects.filter(kakaoemail=kakaoemail)
        serializer = ReviewSerializer(objs, many=True)
        return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
@csrf_exempt
def reviewAvgOfLiquor(request, number):
    if request.method == "GET":
        objs = review.objects.filter(liquornumber=number)
        if len(objs) == 0:
            return JsonResponse({"avg": 0}, status=200)
        sum = 0
        cnt = 0
        for obj in objs:
            sum += obj.score
        return JsonResponse({"avg": round(sum/len(objs), 2)}, status=200)
    return JsonResponse({"message": "GET방식으로 통신해야함"}, status=404)
