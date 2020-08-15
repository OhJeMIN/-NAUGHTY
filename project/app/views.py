from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def item(request):
    return render(request, 'item.html')

def login(request):
    return render(request, 'login.html')
    
def mypage(request):
    return render(request, 'mypage.html')

def order(request):
    return render(request, 'order.html')
<<<<<<< HEAD

def detail(request):
    return render(request, 'detail.html')
=======
def loding(request):
    return render(request, 'loding.html')
>>>>>>> f6c6dae258fb18aeac68a4e13461a84826973058
