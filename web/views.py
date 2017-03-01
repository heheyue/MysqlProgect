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
            HostAddCheckBit = HostAddCheck.is_valid()
            if HostAddCheckBit:
                try:
                    HostInfo.objects.create(HostIp=HostIp,HostName=HostName,HostDescription=HostDescription)
                    return render(request,'web/success.html',{'url':'http://192.168.130.18/web/hostadd'})
                except Exception,e:
                    if e[0] == 1062:
                        return render(request, 'web/hostadd.html', {'msg':'添加失败','error':'IP地址重复'})
                    else:
                        return render(request, 'web/hostadd.html', {'msg': '添加失败', 'error': e})
            else:
                CheckAddError = HostAddCheck.errors.as_data().values()[0][0].messages[0]
                return render(request, 'web/hostadd.html', {'msg': CheckAddError})
        else:
            return render(request,'web/hostadd.html',{'msg':'必填项存在空，请从新填写'})
    else:
        return render(request,'web/hostadd.html')