from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def item(request):
    return render(request, 'item.html')

<<<<<<< HEAD
def login(request):
    return render(request, 'login.html')
=======
def detail(request):
    return render(request, 'detail.html')

def order(request):
    return render(request, 'order.html')
>>>>>>> 4ffd8eed8cc618a3757f4e19caf4d88f02ffc019
