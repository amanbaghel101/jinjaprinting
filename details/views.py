from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def simple(request):
    return HttpResponse('<h1>hiiii </h1>')

def html(request):
    return render(request,'index.html')

dict={'name':'aman baghel'}
def jinjaprinting(request):
    return render(request,'index.html',context=dict)