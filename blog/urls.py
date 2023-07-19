
from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('',views.blog,name= 'index'),
    path('single/<str:id>',views.blog_single,name ='single'),
    path('test/',views.Test),
    path('category/<str:pk>',views.blog_category,name='category'),
    #path('category/<str:cat_name>',views.blog_category,name='categories')
    
]
