from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def item(request):
    return render(request, 'item.html')

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
    
def mypage(request):
    return render(request, 'mypage.html')

def order(request):
    return render(request, 'order.html')

def detail(request):
    return render(request, 'detail.html')
    
def loding(request):
    return render(request, 'loding.html')
