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
<<<<<<< HEAD
    path('login', app.views.login, name='login')
=======
    path('detail', app.views.detail, name = 'detail'),
    path('order', app.views.order, name='order')
>>>>>>> 4ffd8eed8cc618a3757f4e19caf4d88f02ffc019
]
