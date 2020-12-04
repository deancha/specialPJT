# -*- coding: utf-8 -*-
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# 내가 쓸것들 IMPORT
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view

# DRF IMPORT
from rest_framework.parsers import JSONParser
from rest_framework import viewsets

# Model IMPORT
from .models import Subscription
from .serializer import Subscriptionserializer



@api_view(['POST'])
@csrf_exempt
def subscriptioninsert(request):
    if request.method == "POST":
        data = JSONParser().parse(request)
        print(data)
        serializer = Subscriptionserializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,  safe=False)
        return JsonResponse({"message": "구독 저장시 오류발생"}, status=200)

# 정기구독여부 확인


# 정기구독여부 확인
@api_view(['GET'])
@csrf_exempt
def issubscription(request, email):
    print("issubscription")
    if request.method == "GET":
        data = Subscription.objects.filter(kakaoemail=email)
        serial = Subscriptionserializer(data, many=True)
        return JsonResponse(serial.data, safe=False)


@api_view(['GET', 'PUT', 'DELETE'])
@csrf_exempt
def subscriptionone(request, email):
    print("subscriptionone")
    # 현재 정기구독 정보 확인
    if request.method == "GET":
        data = Subscription.objects.filter(kakaoemail=email)
        serial = Subscriptionserializer(data, many=True)
        return JsonResponse(serial.data, safe=False)

    # 정기구독 갱신 시
    elif request.method == "PUT":
        data = Subscription.objects.filter(kakaoemail=email)
        serializer = Subscriptionserializer(data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse({"message": "수정실패"}, status=200)

    # 정기구독 취소
    elif request.method == "DELETE":
        data = Subscription.objects.filter(kakaoemail=email)
        data.delete()
        return JsonResponse({"message": "삭제완료"}, status=200)
