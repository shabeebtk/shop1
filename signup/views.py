from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,'signup.html')



def about(request):
    return render(request,'sample.html')
    
def signin(request):
    return render(request,'signin.html' )

def sample2(request):
    return render(request,'sample2.html')