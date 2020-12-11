from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request, 'dbsapp/login.html') 

def logout(request):
    return render(request, 'dbsapp/logout.html') 

def overview(request):
    return render(request, 'dbsapp/overview.html', {'title': 'About'})

def transaction(request):
    return render(request, 'dbsapp/transaction.html', {'title': 'About'})