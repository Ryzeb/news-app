from django.urls import path
from.views import index, bbc,sports, business,tech
urlpatterns = [
   path('',index, name = 'index'),
   path('bbc/',bbc, name = 'bbc'),
   path('sports/',sports, name = 'sports'),
   path('business/',business,name = 'business'),
   path('tech/',tech , name = 'tech')



]