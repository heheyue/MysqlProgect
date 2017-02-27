from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import request

# Create your views here.

def HostAdd(request):
    if request.method == 'POST':
        return HttpResponse('dasjkjaakl')
    else:
        return render(request,'web/hostadd.html')