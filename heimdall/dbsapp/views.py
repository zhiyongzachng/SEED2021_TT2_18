from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def login(request):
    if request.method == "POST":
        user = request.POST.get('username')
        if user == "mark":
            return HttpResponse('hello mark')

    return render(request, "dbsapp/login.html")

def logout(request):
    return render(request, 'dbsapp/logout.html') 

def overview(request):
    return render(request, 'dbsapp/overview.html', {'title': 'About'})

def transaction(request):
    return render(request, 'dbsapp/transaction.html', {'title': 'About'})


