# -*- coding: utf-8 -*-
from django.shortcuts import render
from Setdata.settingdata import get_drink_dataframe
from Setdata.settingdata import get_order_dataframe
from Setdata.settingdata import get_review_dataframe
from Setdata.settingdata import get_cforder_dataframe
# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .serializer import Liquorserializer
from rest_framework.parsers import JSONParser
from Liquor import models, serializer
from rest_framework import viewsets
from .models import Liquor

from update import views as uviews
from order import models as OrderModels
from order import serializer as OrderSerializer
from update.models import cforder as updateModel
from rest_framework.decorators import api_view
from review import models as ReivewModels
from Liquor import views

from django.utils import timezone
import requests
import time


# redis cache
from django.core.cache import cache

@api_view(['GET','POST'])
@csrf_exempt
def Liquorlist(request):
    if request.method == "GET":
        query_set = Liquor.objects.all()
        serializer = Liquorserializer(query_set, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == "POST":
        # 술 등록
        data = JSONParser().parse(request)
        serializer = Liquorserializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=404)


@api_view(['GET'])
@csrf_exempt
def LiquorSimilar(request, number):
    if request.method == "GET":
        obj = Liquor.objects.get(pk=number)
        liquorname = Liquorserializer(obj).data["liquorname"]


@api_view(['GET',"DELETE"])
@csrf_exempt
def Liquorone(request, number):
    obj = Liquor.objects.get(pk=number)
    if request.method == "GET":
        # PK의 술을  JSON 반환
        serializer = Liquorserializer(obj)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == "DELETE":
        obj.delete()
        return JsonResponse({"message": "삭제완료"}, status=200)




@api_view(['GET'])
@csrf_exempt
def databaseinit(request):

    print("*"*30+"데이터베이스를 초기화합니다"+"*"*30)
    Liquor.objects.all().delete()
    if request.method == "GET":
        df = get_review_dataframe()
        
        for index , review in df.iterrows():
            review = list(review)
            ReivewModels.review.objects.create(
                liquornumber = review[0],
                kakaoemail = review[1],
                score = review[2],
                content	 =review[3]
            )
        
        
        
        df = get_cforder_dataframe()
        for index, cforder in df.iterrows():
            
            cforder = list(cforder)
        
            updateModel.objects.create(
                kakaoemail= cforder[0],
                liquor1 = cforder[1],
                liquor2 = cforder[2],
                liquor3= cforder[3],
                liquor4= cforder[4],
                liquor5= cforder[5],
                liquor6= cforder[6],
                liquor7= cforder[7],
                liquor8= cforder[8],
                liquor9= cforder[9],
                liquor10= cforder[10],
                liquor11= cforder[11],
                liquor12= cforder[12],
                liquor13= cforder[13],
                liquor14= cforder[14],
                liquor15= cforder[15],
                liquor16= cforder[16],
                liquor17= cforder[17],
                liquor18= cforder[18],
                liquor19= cforder[19],
                liquor20= cforder[20],
                liquor21= cforder[21],
                liquor22= cforder[22],
                liquor23= cforder[23],
                liquor24= cforder[24],
                liquor25= cforder[25],
                liquor26= cforder[26],
                liquor27= cforder[27],
                liquor28= cforder[28],
                liquor29= cforder[29],
                liquor30= cforder[30],
                liquor31= cforder[31],
                liquor32= cforder[32],
                liquor33= cforder[33],
                liquor34= cforder[34],
                liquor35= cforder[35],
                liquor36= cforder[36],
                liquor37= cforder[37],
                liquor38= cforder[38],
                liquor39= cforder[39],
                liquor40= cforder[40],
                liquor41= cforder[41],
                liquor42= cforder[42],
                liquor43= cforder[43],
                liquor44= cforder[44],
                liquor45= cforder[45],
                liquor46= cforder[46],
                liquor47= cforder[47],
                liquor48= cforder[48],
                liquor49= cforder[49],
                liquor50= cforder[50],
                liquor51= cforder[51],
                liquor52= cforder[52],
                liquor53= cforder[53],
                liquor54= cforder[54],
                liquor55= cforder[55],
                liquor56= cforder[56],
                liquor57= cforder[57],
                liquor58= cforder[58],
                liquor59= cforder[59],
                liquor60= cforder[60],
                liquor61= cforder[61],
                liquor62= cforder[62],
                liquor63= cforder[63],
                liquor64= cforder[64],
                liquor65= cforder[65],
                liquor66= cforder[66],
                liquor67= cforder[67],
                liquor68= cforder[68],
                liquor69= cforder[69],
                liquor70= cforder[70],
                liquor71= cforder[71],
                liquor72= cforder[72],
                liquor73= cforder[73],
                liquor74= cforder[74],
                liquor75= cforder[75],
                liquor76= cforder[76],
                liquor77= cforder[77],
                liquor78= cforder[78],
                liquor79= cforder[79],
                liquor80= cforder[80],
                liquor81= cforder[81],
                liquor82= cforder[82],
                liquor83= cforder[83],
                liquor84= cforder[84],
                liquor85= cforder[85],
                liquor86= cforder[86],
                liquor87= cforder[87],
                liquor88= cforder[88],
                liquor89= cforder[89],
                liquor90= cforder[90],
                liquor91= cforder[91],
                liquor92= cforder[92],
                liquor93= cforder[93],
                liquor94= cforder[94],
                liquor95= cforder[95],
                liquor96= cforder[96],
                liquor97= cforder[97],
                liquor98= cforder[98],
                liquor99= cforder[99],
                liquor100=cforder[100], 
                liquor101=cforder[101], 
                liquor102=cforder[102], 
                liquor103=cforder[103], 
                liquor104=cforder[104], 
                liquor105=cforder[105], 
                liquor106=cforder[106], 
                liquor107=cforder[107], 
                liquor108=cforder[108], 
                liquor109=cforder[109], 
                liquor110=cforder[110], 
                liquor111=cforder[111], 
                liquor112=cforder[112], 
                liquor113=cforder[113], 
                liquor114=cforder[114], 
                liquor115=cforder[115], 
                liquor116=cforder[116], 
                liquor117=cforder[117], 
                liquor118=cforder[118], 
                liquor119=cforder[119], 
                liquor120=cforder[120]
            )
        
         
        df = get_drink_dataframe()
        for index, liquor in df.iterrows():
           
            liquor = Liquor.objects.create(
                liquorname=index,
                liquorarea=liquor[0],
                liquorcategory=liquor[1],
                liquoralcohol=liquor[2],
                liquorprice=liquor[3],
                liquoringredient=liquor[4],
                sweet=liquor[5],
                sour=liquor[6],
                cloudy=liquor[7],
                carbonated=liquor[8],
                plain=liquor[9],
                body=liquor[10],
                bitter=liquor[11],
                fancy=liquor[12],
                spicy=liquor[13],
                salty=liquor[14],
                sourness=liquor[15],
                acerbity=liquor[16],
                flavor=liquor[17],
                url=liquor[18]
            )
     
        df = get_order_dataframe()
        for index , order in df.iterrows():
            order = list(order)
            OrderModels.Order.objects.create(
                    tid = order[0],
                    username = order[1],
                    kakaoemail = order[2],
                    liquornumber = order[3],
                    liquorname = order[4],
                    liquorprice = order[5],
                    quantity = order[6],
                    address =order[7],
                    phonenumber = order[8],
                    waynumber=order[9],
                    uniqueness = order[10],
                    created_at = timezone.now()
            )
        
            
        return JsonResponse({"message": "DB초기화 완료"}, status=200)
    

@api_view(['GET'])
@csrf_exempt
def redisinit(request):
    if request.method=='GET':
        for i in range(1,120):
            fromcache= views.recommendation_drink_of_contents_based(i) 
            cache.set( i ,fromcache , 60*60 )
        return JsonResponse({"message":"redis init"} , safe=False)    
