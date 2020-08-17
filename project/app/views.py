from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def item(request):
    return render(request, 'item.html')

def item1(request):
    return render(request, 'item1.html')

def item2(request):
    return render(request, 'item2.html')

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

def loding(request):
    return render(request, 'loding.html')
