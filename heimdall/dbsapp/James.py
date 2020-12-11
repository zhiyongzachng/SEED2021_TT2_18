from django.shortcuts import render
from django.http import HttpResponse

import requests 
import json

# Create your views here.
def login(request):
	if request.method == "POST":
		MAIN_URL = "https://u8fpqfk2d4.execute-api.ap-southeast-1.amazonaws.com/techtrek2020/transaction/view"
		result = requests.post(MAIN_URL, headers={'x-api-key': '1elJCmVDjP45as0PT9fsEmHvP03074O8h05lQUmh'},data={"custID":'18'})
		result_dict = result.json()
		context = {
                'accountName' : result_dict['accountName'],
                'accountNumber' : result_dict['accountNumber'],
                'availableBal' : result_dict['availableBal'],
                'linked' : result_dict['linked']
			}
		return render(request, 'account_info.html', context['accuntName'])
def logout(request):
	return render(request, 'dbsapp/logout.html') 

def overview(request):
	return render(request, 'dbsapp/overview.html', {'title': 'About'})

def transaction(request):
	return render(request, 'dbsapp/transaction.html', {'title': 'About'})


