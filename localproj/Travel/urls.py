from django.urls import path, include
from Travel.views import *

app_name = 'Travel'
urlpatterns = [
    path('', index, name = 'index'),
    path('hotel', hotel, name = 'hotel'),
    path('Flights', Flights, name = 'Flights'),
    path('Tours', Tours, name = 'Tours'),
    path('ContactUs', ContactUs, name = 'ContactUs'),
    path('testlang', testlang, name = 'testlang')

]