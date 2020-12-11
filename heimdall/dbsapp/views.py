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

#@login_required(redirect_field_name='dbsapp/login.html')
def logout(request):
    return render(request, 'dbsapp/logout.html') 

#@login_required(redirect_field_name='dbsapp/login.html')
def overview(request):
    
    return render(request, 'dbsapp/account_info.html')

#@login_required(redirect_field_name='dbsapp/login.html')
def transaction(request):
    if request.method == "POST":
        phoneNumber = request.POST.get('PhoneNumber')

        #TODO transfer amount
        Amount = request.POST.get('amount')

    #Get every single user information
    MAIN_URL = "https://u8fpqfk2d4.execute-api.ap-southeast-1.amazonaws.com/techtrek2020/users"
    result = requests.post(
        MAIN_URL, headers={'x-api-key': '1elJCmVDjP45as0PT9fsEmHvP03074O8h05lQUmh'})
    result_dict = result.json()
    context = {
        'result_dict': result_dict[1]['phoneNumber']
    }
    # print(result_dict[0])

    answer = []
    for row in result_dict:
        phoneNumber = row['phoneNumber']
        if (phoneNumber == ):
            userid = row['custID']
        # value = result_dict[row]['phoneNumber']
        # print(value)
        # answer.append(result_dict[row]['id'])
            context = {
                'result_dict': userid
            }
            # return render(request, 'transferfunds.html', context)

    MAIN_URL2 = "https://u8fpqfk2d4.execute-api.ap-southeast-1.amazonaws.com/techtrek2020/accounts/view"
    result2 = requests.post(MAIN_URL2, headers={
                            'x-api-key': '1elJCmVDjP45as0PT9fsEmHvP03074O8h05lQUmh'}, json={'custID': userid})

    context = {
        'result_dict': result2.json()[0]['accountName']
    }
    for row in result2.json():
        accountName = row['accountName']
        if (accountName == 'Current Account'):
            context = {
            'result_dict': row
            }

    return render(request, 'dbsapp/make_transfer.html', context)
