from django.urls import path
from order import views

urlpatterns = [
    path("<str:email>/<int:number>", views.orderone),
    path("<str:email>/", views.orderlist),
    path("", views.orderinsert)
]
