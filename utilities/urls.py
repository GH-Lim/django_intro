from django.urls import path
from . import views
urlpatterns = [
    path('index/', views.index),    # url과 view 함수를 매핑
]
