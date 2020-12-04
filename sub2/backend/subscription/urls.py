from django.urls import path
from . import views

urlpatterns = [
    path("", views.subscriptioninsert),
    path("<str:email>", views.subscriptionone),
    path("check/<str:email>", views.issubscription),
    
]
