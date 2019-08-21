from django.urls import path
from . import views

urlpatterns = [
    path('num/push/', views.push),
    path('num/pull/', views.pull),

    path('static_example/', views.static_example),

    path('lotto_result/', views.lotto_result),
    path('lotto_pick/', views.lotto_pick),

    path('result/', views.result),
    path('search/', views.search),

    path('lotto/', views.lotto),
    path('isityourbirthday/<str:birthday>/', views.isityourbirthday),
    path('isitbirthday/', views.isitbirthday),
    path('template_language/', views.template_language),
    path('times/<int:num1>/<int:num2>/', views.times),
    path('strtimes/<str:numxnum>/', views.strtimes),
    path('greeting/<str:name>/', views.greeting),
    path('image/', views.image),
    path('dinner/<str:name>/', views.dinner),
    path('introduce/', views.introduce),
    path('index/', views.index),    # url과 view 함수를 매핑
]
