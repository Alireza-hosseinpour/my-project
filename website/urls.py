
from django.urls import path
from . import views

app_name = 'website'

urlpatterns = [
    path('',views.home,name='home'),
    path('about/',views.about,name= 'about'),
    path('contact/',views.contact,name ='contact'),
    path('newsletter',views.newsletter_view,name='newsletter')
]
