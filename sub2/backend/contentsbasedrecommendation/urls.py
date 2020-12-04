from django.urls import path
from contentsbasedrecommendation import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path("<int:number>/<str:avoid>", views.recommendwithavoid),
    path("<int:number>/", views.recommend)
]
