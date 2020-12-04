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

# requests IMPORT
import requests
import time

@api_view(['GET'])
@csrf_exempt
def liquor(request):
    if request.method == 'GET':
        print("redis update")
        server_url= "http://j3a403.p.ssafy.io/api/"
        URL = server_url+'contentsbasedrecommendation/'
        for i in range(1,120):
            time.sleep(3)
            response = requests.get(URL + str(i))
            
        return JsonResponse({"message": "liquor redis update is ok"}, status=404)





