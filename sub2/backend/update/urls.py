from django.urls import path
from update import views

urlpatterns = [
    path("liquor", views.liquor),
]
