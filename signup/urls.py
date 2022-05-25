from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('signup',views.index,name='index'),
    path('home1',views.about,name='about'),
    path('signin',views.signin,name='signin'),
    path('sample2',views.sample2,name='sample2'),
    path('',views.home,name='home'),
    path('sample3',views.sample3,name='about page'),
    path('sample4',views.sample4,name='contact page'),
    path('sample5',views.sample5,name='javascript'),
    path('facebook',views.facebook,name='facebook page'),
    path('sample7',views.sample7,name='jquary page'),
    path('sample8',views.sample8,name='jquary page 2'),
    path('java',views.java,name='javascript'),
    path('java2',views.java2,name='javascript2'),
]