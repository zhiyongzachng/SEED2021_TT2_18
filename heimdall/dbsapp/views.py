from django.shortcuts import render
from django.http import HttpResponse
import requests
import logging
from django.contrib.auth.decorators import login_required

# Create your views here.

def login(request):
    if request.method == "POST":
        user = request.POST.get('username')
        password = request.POST.get('password')
        try:
            aws_login_url = "https://u8fpqfk2d4.execute-api.ap-southeast-1.amazonaws.com/techtrek2020/login"
            result = requests.post(aws_login_url, headers={"x-api-key":"1elJCmVDjP45as0PT9fsEmHvP03074O8h05lQUmh"}, json={"username": user,"password":password})
            print(result.json())
            print(result.status_code)
            print("Login Successful")
            return render(request, 'dbsapp/account_info.html')
        except Exception:
            print("Authentication failed")

    return render(request, "dbsapp/login.html")

@login_required
def logout(request):
    return render(request, 'dbsapp/logout.html') 
@login_required
def overview(request):
    return render(request, 'dbsapp/account_info.html')
@login_required
def transaction(request):
    return render(request, 'dbsapp/transaction.html')


