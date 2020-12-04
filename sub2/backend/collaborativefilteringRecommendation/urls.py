from django.urls import path
from collaborativefilteringRecommendation import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path("<str:email>/", views.recommend)
]
