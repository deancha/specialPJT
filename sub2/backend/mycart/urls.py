from django.urls import path
from mycart import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path("cartDelete/<str:email>", views.Cartone),
    path("cartGet/<str:email>", views.Cartlist),
    path("cartUD/<int:cart_id>", views.CartDeleteByCartId),
    path("", views.insertCart),
]
