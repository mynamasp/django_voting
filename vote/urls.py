from django.conf.urls import url
from django.urls import path

from .views import HomePageView,Conditions,test,Vote_1,Vote_2
urlpatterns = [
    path('', HomePageView, name='home'),
    path('Conditions', Conditions, name='conditions'),
    path('Vote_1', Vote_1, name='vote'),
    path('Vote_2', Vote_2 ,name='submit'),



]