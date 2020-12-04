from django.shortcuts import render, redirect
import requests
from django.http import HttpResponse, JsonResponse
from django.core.cache import cache
from rest_framework.parsers import JSONParser

# Create your views here.

app_admin_key = "df663b4293270b8b48e13cdf15e98e5a"

local_url = "http://localhost:8080/"
server_url= "http://j3a403.p.ssafy.io/"

def pay(request):
    if request.method == "POST":
        data = JSONParser().parse(request)
        print(data)
        URL = 'https://kapi.kakao.com/v1/payment/ready'
        headers = {
            "Authorization": "KakaoAK " + app_admin_key,
            "Content-type": "application/x-www-form-urlencoded;charset=utf-8",  # 변경불가
        }

        params = {
            "cid": "TC0ONETIME",    # 테스트용 코드
            "partner_order_id": "1001",     # 주문번호
            "partner_user_id": "userid",    # 유저 아이디
            "item_name": data['item_name'],        # 구매 물품 이름
            "quantity": "1",                # 구매 물품 수량
            "total_amount": data['total_amount'],        # 구매 물품 가격
            "tax_free_amount": "0",         # 구매 물품 비과세
            "approval_url": server_url+"#/pay",  # /approval",
            "cancel_url": server_url+"500/결제가 취소되었습니다.",
            "fail_url": server_url+"500/결제가 실패하였습니다",
        }

        print("들어옵니까?")
        res = requests.post(URL, headers=headers, params=params)
        # print(res.json())
        # request.cookies = {"tid" : res.json()['tid'] }
        # request.session['tid'] = res.json()['tid']  # 결제 승인시 사용할 tid를 세션에 저장
        tid = res.json()['tid']
        print(tid)
        # cache.set('tid', tid, 60*60)
        # res.set_cookie('tid', tid, 60*60)
        # print("tid : " , cache.get("tid"))
        next_url = res.json()['next_redirect_pc_url']   # 결제 페이지로 넘어갈 url을 저장

        # return redirect(next_url)
        res = JsonResponse(res.json())
        # res.set_cookie('tid', tid)
        # request.session['tid'] = tid
        return res

        # res.set_cookie("tid", tid)
        # return res


def payapproval(request):
    if request.method == "GET":
        print("여기는 승인페이지")
        # print("tid : ", request.COOKIES['tid'])
        URL = 'https://kapi.kakao.com/v1/payment/approve'
        headers = {
            "Authorization": "KakaoAK " + app_admin_key,
            "Content-type": "application/x-www-form-urlencoded;charset=utf-8",  # 변경불가
        }

        params = {
            "cid": "TC0ONETIME",    # 테스트용 코드
            # request.COOKIES['tid'],  # 결제 요청시 세션에 저장한 tid
            "tid": request.GET.get("tid"),
            "partner_order_id": "1001",     # 주문번호
            "partner_user_id": "userid",    # 유저 아이디
            "pg_token": request.GET.get("pg_token"),     # 쿼리 스트링으로 받은 pg토큰
        }

        res = requests.post(URL, headers=headers, params=params)
        # amount = res.json()['amount']['total']
        print(res.json())
        # context = {
        #     'res': res,
        #     'amount': amount,
        # }
        # return render(request, '#/pay', context)
        # return JsonResponse(res.json())
        return JsonResponse(res.json())


def subscription(request):
    if request.method == "POST":
        URL = 'https://kapi.kakao.com/v1/payment/ready'
        headers = {
            "Authorization": "KakaoAK " + app_admin_key,
            "Content-type": "application/x-www-form-urlencoded;charset=utf-8",  # 변경불가
        }
        params = {
            "cid": "TCSUBSCRIP",    # 테스트용 코드
            "partner_order_id": "1001",     # 주문번호
            "partner_user_id": "userid",    # 유저 아이디
            "item_name": "주당주당 정기구독",        # 구매 물품 이름
            "quantity": "1",                # 구매 물품 수량
            "total_amount": "19900",        # 구매 물품 가격
            "tax_free_amount": "0",         # 구매 물품 비과세
            "approval_url": server_url+"#/subpay",
            "cancel_url": server_url+"500/결제가 취소되었습니다",
            "fail_url": server_url+"500/결제가 실패하였습니다",
        }
        print("들어옵니까?")
        res = requests.post(URL, headers=headers, params=params)
        # print(res.json())
        # request.cookies = {"tid" : res.json()['tid'] }
        # request.session['tid'] = res.json()['tid']  # 결제 승인시 사용할 tid를 세션에 저장
        tid = res.json()['tid']
        print(tid)
        # cache.set('tid', tid, 60*60)
        # res.set_cookie('tid', tid, 60*60)
        # print("tid : " , cache.get("tid"))
        next_url = res.json()['next_redirect_pc_url']   # 결제 페이지로 넘어갈 url을 저장

        # return redirect(next_url)
        res = JsonResponse(res.json())
        # res.set_cookie('tid', tid)
        # request.session['tid'] = tid
        return res

        # res.set_cookie("tid", tid)
        # return res


def subscriptionapproval(request):
    if request.method == "GET":
        print("여기는 승인페이지")
        # print("tid : ", request.COOKIES['subtid'])
        URL = 'https://kapi.kakao.com/v1/payment/approve'
        headers = {
            "Authorization": "KakaoAK " + app_admin_key,
            "Content-type": "application/x-www-form-urlencoded;charset=utf-8",  # 변경불가
        }

        params = {
            "cid": "TCSUBSCRIP",    # 테스트용 코드
            "tid": request.GET.get("subtid"),  # 결제 요청시 세션에 저장한 tid
            "partner_order_id": "1001",     # 주문번호
            "partner_user_id": "userid",    # 유저 아이디
            "pg_token": request.GET.get("pg_token"),     # 쿼리 스트링으로 받은 pg토큰
        }

        res = requests.post(URL, headers=headers, params=params)
        # amount = res.json()['amount']['total']
        # print(res.json())
        # context = {
        #     'res': res,
        #     'amount': amount,
        # }
        return JsonResponse(res.json())
