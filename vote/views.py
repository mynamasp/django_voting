from django.shortcuts import render
from django.http import HttpResponsePermanentRedirect
from django.urls import reverse
from django.http import HttpResponse


# Create your views here.
def HomePageView(request):
    return render(request, 'index.html')


def Conditions(request):
    password = request.POST['pass']
    if password == "deedee15665":
        return render(request, 'conditions.html')
    else:
        return render(request,'index.html')


def test(request):
    return render(request, 'thankyou.html')


def Vote_1(request):
    return render(request, 'vote.html')


def Vote_2(request):
    return render(request, 'vote2.html')


