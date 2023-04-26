from django.shortcuts import render
from django.shortcuts import render, redirect  
from django.http import HttpResponseRedirect, HttpResponse
# Create your views here.
def list(r):   
    return HttpResponse ('Here are your staff')  

def insert(request):  
    return render(request, 'insertstaff.html')  

def update(request):    
    return render(request, 'updatestaff.html') 

def delete(r):   
    return redirect("/staff/list") 