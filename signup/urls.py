from django.urls import path
from . import views

urlpatterns = [
    path('signup',views.index,name='index'),
    path('sample',views.about,name='about'),
    path('signin',views.signin,name='signin'),
    path('sample2',views.sample2,name='sample2')
]