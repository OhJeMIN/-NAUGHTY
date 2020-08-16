"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
import app.views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', app.views.index, name = 'index'),
    path('item', app.views.item, name = 'item'),
    path('login', app.views.login, name='login'),
    path('mypage', app.views.mypage, name = 'mypage'),
    path('order', app.views.order, name='order'),
    path('detail', app.views.detail, name='detail'),
    path('join1', app.views.join1, name='join1'),
    path('join2', app.views.join2, name='join2'),
    path('info1', app.views.info1, name='info1'),
    path('info2', app.views.info2, name='info2'),
    path('info3', app.views.info3, name='info3'),
    path('info4', app.views.info4, name='info4'),
    path('info5', app.views.info5, name='info5'),
    path('survey', app.views.survey, name='survey'),
    path('l', app.views.loding, name='loding')
]

