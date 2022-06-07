from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,'main_project/signup.html')
def about(request):
    return render(request,'sample/sample.html')
    
def signin(request):
    return render(request,'main_project/signin.html' )

def sample2(request):
    return render(request,'sample/sample2.html')

def home(request):
    return render(request,'main_project/home.html')   

def sample3(request):
    return render(request,'sample/sample3.html')

def sample4(request):
    return render(request,'sample/sample4.html')

def sample5(request):
    return render(request,'sample/sample5.html')


def facebook(request):
    return render(request,'sample/facebook.html')  

def sample7(request):
    return render(request,'sample/sample7.html')

def sample8(request):
    return render(request,'sample/sample8.html')

def java(request):
    return render(request,'sample/javascript.html')  

def java2(request):
    return render(request,'sample/javascript2.html')     

def java3(request):
    return render(request, 'sample/javascript3.html')                   