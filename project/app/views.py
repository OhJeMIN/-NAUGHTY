from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def item(request):
    return render(request, 'item.html')

def login(request):
    return render(request, 'login.html')
