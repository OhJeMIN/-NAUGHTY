from django.shortcuts import render, get_object_or_404, redirect
from .models import UserInfo,Review,Comment,Item
# Create your views here.
def index(request):
    return render(request, 'index.html')

def item(request, id):
    item = Item.objects.filter(gender = id)
    print(item)
    return render(request, 'item.html', {'arr':item})

def item1(request):
    item1 = Item.objects.filter(gender__in = [1,2,3])
    return render(request, 'item1.html', {'arr': item1})

def item2(request):
    item2 = Item.objects.filter(gender = 3)
    print(item2)
    return render(request, 'item2.html', {'arr':item2})

def login(request):
    return render(request, 'login.html')

def join1(request):
    return render(request, 'join1.html')

def join2(request):
    return render(request, 'join2.html')

def info1(request):
    return render(request, 'info1.html')

def info2(request):
    return render(request, 'info2.html')

def info3(request):
    return render(request, 'info3.html')

def info4(request):
    return render(request, 'info4.html')

def info5(request):
    return render(request, 'info5.html')

def result1(request):
    return render(request, 'result1.html')

def result2(request):
    return render(request, 'result2.html')

def survey(request):
    return render(request, 'survey.html')
    
def mypage(request):
    return render(request, 'mypage.html')

def order(request):
    return render(request, 'order.html')

def detail(request):
    return render(request, 'detail.html')

def loading(request):
    return render(request, 'loading.html')
