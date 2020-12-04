from django.urls import path
from Liquor import views


urlpatterns = [

    path(r"<int:number>", views.Liquorone),
    path(r"", views.Liquorlist),

]
