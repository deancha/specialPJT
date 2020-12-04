from django.shortcuts import render
# -*- coding: utf-8 -*-
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework import viewsets

# Liquor model
from Liquor import models, serializer

# redis cache
from django.core.cache import cache
from django.db.models import Q

# random 추출 
import random 
@api_view(['GET'])
@csrf_exempt
def RandomLiquor(request, email):
    if request.method == "GET":
        fromcache = cache.get("user"+email)
        if fromcache is None:
            return JsonResponse({"message":"cache is none"}, status=200 , safe=False)
        query_set = models.Liquor.objects.all()
        lserializer = serializer.Liquorserializer(models.Liquor.objects.filter(~Q(liquornumber__in=fromcache)), many=True)
        li= list(lserializer.data)
        choiceLIst = []
        choiceLIst = [random.choice(li) for i in range(5) if i not in choiceLIst]
        return JsonResponse(choiceLIst, safe=False)
        
