from django.shortcuts import render
from django.http import HttpResponse
import requests 


# Create your views here.

def home(request):
    MAIN_URL = "https://u8fpqfk2d4.execute-api.ap-southeast-1.amazonaws.com/techtrek2020/users"
    result = requests.post(MAIN_URL, headers={'x-api-key': '1elJCmVDjP45as0PT9fsEmHvP03074O8h05lQUmh'})
    result_dict = result.json()
    return render(request, 'transferfunds.html', result_dict)

def about(request):
    return HttpResponse('<h1>Blog About</h1>')