from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.urls import path, include
from drf_yasg.views import get_schema_view
from rest_framework.permissions import AllowAny, IsAuthenticated, BasePermission
from drf_yasg import openapi
from django.conf.urls import url
from rest_framework import permissions
from django.urls import path, include, re_path
from Liquor import views
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from socialLogin.views import kakao_login, kakao_callback
# DB init 을위한 Liquor views 호출 -> 서버에 올릴시는 빼고
from Liquor import views
from socialLogin.views import kakao_login, kakao_callback
# fmt: off


schema_url_patterns = [


    # 관리자 페이지 ID :SSAFY / PW : SSAFY
    path("admin/", admin.site.urls),

    # 데이터베이스 초기화 URL -> FILE BASED의 데이터가 SQLITE3로 자동으로 넣어진다.
    path("DBINIT/", views.databaseinit),

    # 주문 처리를 위한 APP
    path("order/",include("order.urls")),

    # 전통주 목록조회를 위한 APP
    path("liquor/" , include("Liquor.urls")),

    # 장바구니를 위한 APP
    path("cart/", include("mycart.urls")),

    # 정기 결제를위한 APP
    path("subscription/", include("subscription.urls")),

    # ITEM BASED 추천을위한 APP
    path("contentsbasedrecommendation/", include("contentsbasedrecommendation.urls")),

    # kakao Login
    path('account/login/kakao/', kakao_login, name='kakao_login'),
    path('account/login/kakao/callback/', kakao_callback, name='kakao_callback'),



    # USER BASED 추천을 위한 APP
    path("collaborativefilteringRecommendation/", include("collaborativefilteringRecommendation.urls")),


    path("review/", include("review.urls")),
    # 카카오 페이
    path("pay/", include('kakaopay.urls')),

    # 유사도 redis update
    path("update/", include('update.urls')),

    # 랜덤추천
    path("randomrecommendation/",include('randomrecommendation.urls'))

]

schema_view = get_schema_view(


    openapi.Info(
        title="주당주당",
        default_version="v1",
        description='''
        주당주당 API 문서입니다
        
        ''',
        terms_of_service = 'https://google.com/policies/terms/',
        contact =openapi.Contact(email="gotkddnjs@naver.com"),
        license =openapi.License(name="JUDANGJUDANG"),
    ),
    validators =['flex'],
    public = True,
    permission_classes=(AllowAny,),
    patterns = schema_url_patterns,
)



urlpatterns = [

    # SWAGGER같은 yasg 연결을 위한 URL
    path('swagger<str:format>',schema_view.without_ui(cache_timeout=0),name='schema-json'),
    path('swagger/',schema_view.with_ui("swagger",cache_timeout=0),name='schema-swagger-ui'),
    path("redoc/",schema_view.with_ui('redoc',cache_timeout=0),name ='schema-redoc'),

    # 관리자 페이지 ID :SSAFY / PW : SSAFY
    path("admin/", admin.site.urls),

    # 데이터베이스 초기화 URL -> FILE BASED의 데이터가 SQLITE3로 자동으로 넣어진다.
    path("DBINIT/", views.databaseinit),

    # 주문 처리를 위한 APP
    path("order/",include("order.urls")),

    # 전통주 목록조회를 위한 APP
    path("liquor/" , include("Liquor.urls")),

    # 장바구니를 위한 APP
    path("cart/", include("mycart.urls")),

    # 정기 결제를위한 APP
    path("subscription/", include("subscription.urls")),

    # ITEM BASED 추천을위한 APP
    path("contentsbasedrecommendation/", include("contentsbasedrecommendation.urls")),

    # USER BASED 추천을 위한 APP
    path("collaborativefilteringRecommendation/", include("collaborativefilteringRecommendation.urls")),

    # kakao Login
    path('account/login/kakao/', kakao_login, name='kakao_login'),
    path('account/login/kakao/callback/', kakao_callback, name='kakao_callback'),


    # 리뷰 작성 
    path("review/", include("review.urls")),
    # 카카오 페이
    path("pay/", include('kakaopay.urls')),

    # 유사도 redis update
    path("update/", include('update.urls')),

    # 랜덤추천
    path("randomrecommendation/",include('randomrecommendation.urls'))
]
