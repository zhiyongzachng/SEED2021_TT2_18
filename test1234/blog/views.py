from django.shortcuts import render
from django.http import HttpResponse
import requests 

#post = [
#    { 'author' : 'CoreyMS'}
#]
# Create your views here.

def home(request):
    MAIN_URL = "https://u8fpqfk2d4.execute-api.ap-southeast-1.amazonaws.com/techtrek2020/users"
    result = requests.post(MAIN_URL, headers={'x-api-key': '1elJCmVDjP45as0PT9fsEmHvP03074O8h05lQUmh'})
    result_dict = result.json()
    context = {
        'result_dict' : result_dict[1]['phoneNumber']
    }
    #print(result_dict[0])
   
    answer = []
    for row in result_dict:
        phoneNumber = row['phoneNumber']
        if (phoneNumber == '(+65) 98271258'):
            userid = row['custID']
        #value = result_dict[row]['phoneNumber']
        #print(value)
        #answer.append(result_dict[row]['id'])
            context = {
                'result_dict' : userid
            }
            return render(request, 'transferfunds.html', context)
         

def about(request):
    return HttpResponse('<h1>Blog About</h1>')