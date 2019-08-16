"""django_intro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from pages import views

# www.ssafy.com/admin/  => 성공
# www.ssafy.com/login/  => 페이지 없음 404 not found
# www.ssafy.com/index/  => views.index

urlpatterns = [
    # path('사용자가 접속하는 경로', views.함수이름),
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
    path('admin/', admin.site.urls),
]
