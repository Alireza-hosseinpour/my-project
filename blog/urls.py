
from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('',views.blog,name= 'index'),
    path('single/<str:id>',views.blog_single,name ='single'),
]