from django.urls import path, include
from .views import get_group_lessons_v2

urlpatterns = [
    path('', get_group_lessons_v2),
]
