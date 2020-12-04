from django.urls import path
from randomrecommendation import views


urlpatterns = [
 path(r"<str:email>", views.RandomLiquor),
]
