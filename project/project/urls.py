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
from django.conf import settings
from django.conf.urls.static import static
import app.views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', app.views.index, name = 'index'),
    path('item', app.views.item, name = 'item'),
    path('item1', app.views.item1, name = 'item1'),
    path('item2', app.views.item2, name = 'item2'),
    path('login', app.views.login, name='login'),
    path('logout', app.views.logout, name='logout'),
    path('mypage/<int:userinfo_id>', app.views.mypage, name = 'mypage'),
    path('order', app.views.order, name='order'),
    path('detail/<int:id>', app.views.detail, name='detail'),
    path('join1', app.views.join1, name='join1'),
    path('join2', app.views.join2, name='join2'),
    path('info1/<int:userinfo_id>', app.views.info1, name='info1'),
    path('info2/<int:userinfo_id>', app.views.info2, name='info2'),
    path('info3/<int:userinfo_id>', app.views.info3, name='info3'),
    path('info4/<int:userinfo_id>', app.views.info4, name='info4'),
    path('info5/<int:userinfo_id>', app.views.info5, name='info5'),
    path('infocreate', app.views.infocreate, name='infocreate'),
    path('goinfo/<int:userinfo_id>', app.views.goinfo, name='goinfo'),
    path('infogenderud/<int:userinfo_id>', app.views.infogenderud, name='infogenderud'),
    path('infocoupleud/<int:userinfo_id>', app.views.infocoupleud, name='infocoupleud'),
    path('infotypeud/<int:userinfo_id>', app.views.infotypeud, name='infotypeud'),
    path('survey', app.views.survey, name='survey'),
    path('result1', app.views.result1, name='result1'),
    path('result2', app.views.result2, name='result2'),
    path('loading', app.views.loding, name='loading'),
    path('change_order', app.views.chanege_order, name='change_order'),
    path('review_create', app.views.review_create, name='review_create'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

