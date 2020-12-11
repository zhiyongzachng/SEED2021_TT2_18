from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def login(request):
    if request.method == "POST":
		amount = int(request.POST.get('amount'))
		amt = -amount
		MAIN_URL = "https://u8fpqfk2d4.execute-api.ap-southeast-1.amazonaws.com/techtrek2020/transaction/add"
		result = requests.post(MAIN_URL, headers={'x-api-key': '1elJCmVDjP45as0PT9fsEmHvP03074O8h05lQUmh'},data={"custID":'18',
 "amount":amt})
			result_dict = result.json()
			context = {
				'statusCode' : result_dict['statusCode']
			}
			if context.statusCode == "409"
				return HttpResponse('fail')
			else
				custID = request.POST.get('custID')
				amount = int(request.POST.get('amount'))
				amt = amount
				MAIN_URL = "https://u8fpqfk2d4.execute-api.ap-southeast-1.amazonaws.com/techtrek2020/transaction/add"
				result = requests.post(MAIN_URL, headers={'x-api-key': '1elJCmVDjP45as0PT9fsEmHvP03074O8h05lQUmh'},data={"custID":custID,"amount":amt})
				result_dict = result.json()

				custID = request.POST.get('custID')
				payeeID = request.POST.get('payeeID')
				dateTime = request.POST.get('dateTime')
				amount = request.POST.get('amount')
				expensesCat = request.POST.get('expensesCat')
				eGift = request.POST.get('eGift')
				message = request.POST.get('message')
				MAIN_URL = "https://u8fpqfk2d4.execute-api.ap-southeast-1.amazonaws.com/techtrek2020/transaction/add"
				result = requests.post(MAIN_URL, headers={'x-api-key': '1elJCmVDjP45as0PT9fsEmHvP03074O8h05lQUmh'},data={"custID":custID,"payeeID":payeeID,"dateTime":dateTime,"amount":amount,"expensesCat":expensesCat,"eGift":eGift,"message":message})
				result_dict = result.json()
				context = {
					'statusCode' : result_dict['statusCode']
				}
				if context.statusCode == "200"
					return HttpResponse('hello mark')

    return render(request, "dbsapp/login.html")

def logout(request):
    return render(request, 'dbsapp/logout.html') 

def overview(request):
    return render(request, 'dbsapp/overview.html', {'title': 'About'})

def transaction(request):
    return render(request, 'dbsapp/transaction.html', {'title': 'About'})


