# -*- coding: utf-8 -*-
from django.shortcuts import render


# 내가 쓸것들 IMPORT
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework import viewsets

from .models import Cart
from .serializer import Cartserializer

# kakaoemail을 기준으로


@api_view(['GET'])
@csrf_exempt
def Cartlist(request, email):
    print("email : " + email)
    if request.method == "GET":
        query = Cart.objects.filter(kakaoemail=email)
        serializer = Cartserializer(query, many=True)
        return JsonResponse(serializer.data, safe=False)
    

@api_view(['GET',"DELETE","PUT"])
@csrf_exempt
def Cartone(Request, email):
    print("email : " + email)
    if request.method == "DELETE":
        objs = Cart.objects.filter(kakaoemail=email)
        objs.delete()
        return JsonResponse({"message" : "삭제완료"}, status= 200)
   
@csrf_exempt
def CartDeleteByCartId(request, cart_id):
    print(cart_id)
    if request.method =="DELETE":
        obj = Cart.objects.get(pk=cart_id)
        obj.delete()
        return JsonResponse({"message" : "삭제완료"}, status= 200)
    elif request.method == "PUT" :
        data = JSONParser().parse(request)
        serializer = Cartserializer(obj, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)


@api_view(['POST'])
@csrf_exempt
def insertCart(request):
    if request.method == "POST":
        data = JSONParser().parse(request)
        serializer = Cartserializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)

    elif request.method == "DELETE" :
        objs = Cart.objects.all()
        objs.delete();
        return JsonResponse({"message" : "삭제완료"}, status= 200)
    return JsonResponse({"message": "장바구니 저장시 오류발생"}, status=404)
    