from django.shortcuts import render
from django.shortcuts import render, redirect  
from django.http import HttpResponseRedirect, HttpResponse
# Create your views here.
def list(r):   
    return HttpResponse ('Here are your students')  

def insert(request):  
    return render(request, 'insertstudent.html')  

def update(request):    
    return render(request, 'updatestudent.html') 

def delete(r):   
    return redirect("/student/list")  

# def index(request): #view for / 
#  return HttpResponseRedirect(“/posts”) 
 
# def get_posts(request): #view for /posts 
#  return HttpResponse (“Here are your posts”)