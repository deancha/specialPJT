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
from django.db.models import Count

# DRF IMPORT
from rest_framework.parsers import JSONParser
from rest_framework import viewsets

# Model IMPORT
from .models import Order
from .serializer import Orderserializer
from mycart.models import Cart

from Liquor import models
from Liquor import serializer as lserializer
from django.db.models import Q
# redis cache
from django.core.cache import cache


# 사용자 이메일로 주문 목록을 가져온다.
@api_view(['GET'])
@csrf_exempt
def orderlist(request, email):
    print("email : " + email)
    if request.method == "GET":
        query = Order.objects.filter(kakaoemail=email)
        serializer = Orderserializer(query, many=True)
        return JsonResponse(serializer.data, safe=False)


# 사용자 이메일로 장바구니 목록을 가져온 후 그걸 그대로 주문 DB에 저장


@api_view(['POST', 'GET'])
@csrf_exempt
def orderinsert(request):

    if request.method == 'GET':
        # 판매량순으로 정렬해서 리턴! 상위 5개
        query = Order.objects.values("liquornumber").annotate(
            total=Count('liquornumber')).order_by("-total")
        numlist = [i['liquornumber'] for i in list(query)]

        if len(numlist) > 5:
            numlist = numlist[:5]
        query = models.Liquor.objects.filter(liquornumber__in=numlist)
        llserializer = lserializer.Liquorserializer(query, many=True)
        return JsonResponse(llserializer.data, safe=False)
    if request.method == "POST":
        data = JSONParser().parse(request)
        print(data)
        cartlist = data['order'].split(",")
        for cartid in cartlist[:-1]:
            # print("cartid : ", cartid)
            obj = Cart.objects.get(pk=cartid.split(":")[0])
            liquornumber = obj.liquornumber
            liquorname = obj.liquorname
            liquorprice = obj.liquorprice
            quantity = cartid.split(":")[1]
            # print("술이름 : ",liquorname, ", 가격 : ", liquorprice, ", 수량 : ", quantity)

            orderobj = {
                "tid": data['tid'],
                "username": data['username'],
                "kakaoemail": data['kakaoemail'],
                "liquornumber": liquornumber,
                "liquorname": liquorname,
                "liquorprice": liquorprice,
                "quantity": quantity,
                "address": data['address'],
                "phonenumber": data['phonenumber'],
                "uniqueness": data['uniqueness'],
                "created_at": data['created_at'],
            }

            Order.objects.create(
                tid=orderobj['tid'],
                username=orderobj['username'],
                kakaoemail=orderobj['kakaoemail'],
                liquornumber=orderobj['liquornumber'],
                liquorname=orderobj['liquorname'],
                liquorprice=orderobj['liquorprice'],
                quantity=orderobj['quantity'],
                address=orderobj['address'],
                phonenumber=orderobj['phonenumber'],
                uniqueness=orderobj['uniqueness'],
                created_at=orderobj['created_at']
            )
            obj.delete()
        return JsonResponse({"message": "success"}, status=200)

# 사용자 이메일과 주문번호로 접근하여 삭제시킨다.

@api_view(["GET","DELETE"])
@csrf_exempt
def orderone(request, email, number):
    print("email : " + email)
    print("number : " + str(number))
    if request.method == "DELETE":
        obj = Order.objects.get(kakaoemail=email, order_id=number)
        obj.delete()
        return JsonResponse({"message": "삭제완료"}, status=200)
    
    #사용자 이메일과 술번호로삭제?
    if request.method=='GET':
        print(email + "이 " + str(number) + " 의 술을 구매하였는가?")
        queryset = Order.objects.filter(kakaoemail=email,liquornumber=number)
        serializer = Orderserializer(queryset, many=True)
        return JsonResponse(serializer.data, safe=False)