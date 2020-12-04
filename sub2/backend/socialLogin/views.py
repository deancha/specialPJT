from django.shortcuts import render

# views.py
from django.http import HttpResponse, JsonResponse

from django.shortcuts import redirect
import urllib
import requests

from update import models

local_url = "http://localhost:8080/"
server_url= "http://j3a403.p.ssafy.io/api/"

# code 요청


def kakao_login(request):
    app_rest_api_key = "f279ff5a44356cd0eb83be80ec334259"
    redirect_uri = server_url +"account/login/kakao/callback"
    return redirect(
        f"https://kauth.kakao.com/oauth/authorize?client_id={app_rest_api_key}&redirect_uri={redirect_uri}&response_type=code"
    )


# access token 요청
def kakao_callback(request):
    app_rest_api_key = "f279ff5a44356cd0eb83be80ec334259"
    redirect_uri = server_url+"account/login/kakao/callback"
    user_token = request.GET.get("code")
    print(user_token)
    token_request = requests.get(
        f"https://kauth.kakao.com/oauth/token?grant_type=authorization_code&client_id={app_rest_api_key}&redirect_uri={redirect_uri}&code={user_token}")

    token_response_json = token_request.json()
    error = token_response_json.get("error", None)

    # if there is an error from token_request
    if error is not None:
        raise RuntimeError()
    access_token = token_response_json.get("access_token")
    print(access_token)

    # post request
    profile_request = requests.post(
        "https://kapi.kakao.com/v2/user/me",
        headers={"Authorization": f"Bearer {access_token}"},
    )
    profile_json = profile_request.json()

    kakao_account = profile_json.get("kakao_account")

    userimg = str(kakao_account.get("profile").get("profile_image_url"))
    name = str(kakao_account.get("profile").get("nickname"))
    email =str(kakao_account.get("email"))
    age_range =  str(kakao_account.get("age_range"))
    if not age_range or int(age_range.split("~")[0]) <20:
        message ="young"
        url = "http://j3a403.p.ssafy.io/#/login"
        url += "?message=" +message
        return redirect(url)
    # useremail로 cf구매내역db에 0000으로 초기값 설정

    user = models.cforder.objects.filter(kakaoemail=email)
    print(type(user))
    if user.exists():
        print("해당유저 이미존재")
        pass

    else:
        orderlist = []
        orderlist.append(email)
        models.cforder.objects.create(
            kakaoemail=email,
            liquor1=0,
            liquor2=0,
            liquor3=0,
            liquor4=0,
            liquor5=0,
            liquor6=0,
            liquor7=0,
            liquor8=0,
            liquor9=0,
            liquor10=0,
            liquor11=0,
            liquor12=0,
            liquor13=0,
            liquor14=0,
            liquor15=0,
            liquor16=0,
            liquor17=0,
            liquor18=0,
            liquor19=0,
            liquor20=0,
            liquor21=0,
            liquor22=0,
            liquor23=0,
            liquor24=0,
            liquor25=0,
            liquor26=0,
            liquor27=0,
            liquor28=0,
            liquor29=0,
            liquor30=0,
            liquor31=0,
            liquor32=0,
            liquor33=0,
            liquor34=0,
            liquor35=0,
            liquor36=0,
            liquor37=0,
            liquor38=0,
            liquor39=0,
            liquor40=0,
            liquor41=0,
            liquor42=0,
            liquor43=0,
            liquor44=0,
            liquor45=0,
            liquor46=0,
            liquor47=0,
            liquor48=0,
            liquor49=0,
            liquor50=0,
            liquor51=0,
            liquor52=0,
            liquor53=0,
            liquor54=0,
            liquor55=0,
            liquor56=0,
            liquor57=0,
            liquor58=0,
            liquor59=0,
            liquor60=0,
            liquor61=0,
            liquor62=0,
            liquor63=0,
            liquor64=0,
            liquor65=0,
            liquor66=0,
            liquor67=0,
            liquor68=0,
            liquor69=0,
            liquor70=0,
            liquor71=0,
            liquor72=0,
            liquor73=0,
            liquor74=0,
            liquor75=0,
            liquor76=0,
            liquor77=0,
            liquor78=0,
            liquor79=0,
            liquor80=0,
            liquor81=0,
            liquor82=0,
            liquor83=0,
            liquor84=0,
            liquor85=0,
            liquor86=0,
            liquor87=0,
            liquor88=0,
            liquor89=0,
            liquor90=0,
            liquor91=0,
            liquor92=0,
            liquor93=0,
            liquor94=0,
            liquor95=0,
            liquor96=0,
            liquor97=0,
            liquor98=0,
            liquor99=0,
            liquor100=0,
            liquor101=0,
            liquor102=0,
            liquor103=0,
            liquor104=0,
            liquor105=0,
            liquor106=0,
            liquor107=0,
            liquor108=0,
            liquor109=0,
            liquor110=0,
            liquor111=0,
            liquor112=0,
            liquor113=0,
            liquor114=0,
            liquor115=0,
            liquor116=0,
            liquor117=0,
            liquor118=0,
            liquor119=0,
            liquor120=0,
        )
    # 프론트 메인으로 연결? 
    # for aws
    # url = "http://j3a403.p.ssafy.io/#/"
    url = "http://j3a403.p.ssafy.io/#/login"
    url += "?userimg="+userimg
    url += "&name="+name
    url += "&email="+email
    url += "&age_range="+age_range
    url += "&access_token="+access_token
    return redirect(url)
