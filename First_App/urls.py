
from django.urls import path
from First_App import views

app_name = 'First_App'

urlpatterns=[
    
    path('about/',views.about, name='about'),
    path('contact/',views.contact, name='contact'),
       
    
]