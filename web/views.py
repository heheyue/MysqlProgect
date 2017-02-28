# _*_ coding:utf-8 _*_
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import request

from models import HostInfo


from form import HOSTADD

# Create your views here.

def HostAdd(request):
    if request.method == 'POST':
        HostIp = request.POST.get('HostIp')
        HostName = request.POST.get('HostName')
        HostDescription = request.POST.get('HostDescription')
        print HostIp
        print HostName
        print HostDescription
        if HostName and HostIp and HostDescription:
            HostAddCheck = HOSTADD(request.POST)
            HostAddCheckRq = HostAddCheck.is_valid()

            HostInfo.objects.create(HostIp=HostIp,HostName=HostName,HostDescription=HostDescription)
            return HttpResponse('asdjkasj')
        else:
            return render(request,'web/hostadd.html',{'msg':'必填项存在空，请从新填写'})
    else:
        return render(request,'web/hostadd.html')