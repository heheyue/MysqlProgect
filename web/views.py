# _*_ coding:utf-8 _*_
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import request

from models import HostInfo

from DbUser import *

from form import HOSTADD

# Create your views here.

def HostAdd(request):
    if request.method == 'POST':
        HostIp = request.POST.get('HostIp')
        HostName = request.POST.get('HostName')
        HostDescription = request.POST.get('HostDescription')
        # print HostIp
        # print HostName
        # print HostDescription
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

def ProjectAdd(request):
    if request.method == 'POST':
        ProjectName = request.POST.get('ProjectName')
        ProjectDescription = request.POST.get('ProjectDescription')
        if ProjectDescription and ProjectName:
            ProjectInfo = PROJECTINFO()
            Msg = ProjectInfo.ProjectAdd(ProjectName,ProjectDescription)
            if Msg['TrueBit']:
                return render(request, 'web/success.html', {'url': 'http://192.168.130.18/web/projectadd'})
            else:
                return render(request, 'web/dbuseradd.html', {'msg': Msg['ErrorMsg']})
        else:
            return render(request, 'web/progectadd.html',{'msg':'必填项存在空，请从新填写'})
    else:
        return render(request,'web/progectadd.html')

def DbUserAdd(request):
    DbUserInfo = DBUSERINFO()
    IpId = DbUserInfo.SelectHostIp()
    # print IpId
    if request.method=='POST':
        ChoseIp = int(request.POST.get('ChoseIp'))
        HostUser = request.POST.get('HostUser')
        HostPwd = request.POST.get('HostPwd')
        # print ChoseIp
        # print HostUser
        # print HostPwd
        if ChoseIp == 0:
            return render(request, 'web/dbuseradd.html', {'IpId': IpId, 'msg': '必填项存在空，请从新填写'})
        else:
            if ChoseIp and HostUser and HostPwd:
                msg = DbUserInfo.Add(ChoseIp,HostUser,HostPwd)
                # print msg['TrueBit']
                # print msg['ErrorMsg']
                if msg['TrueBit']:
                    return render(request, 'web/success.html', {'url': 'http://192.168.130.18/web/dbuseradd'})
                else:
                    return render(request, 'web/dbuseradd.html', {'IpId': IpId,'msg':msg['ErrorMsg']})
            else:
                return render(request, 'web/dbuseradd.html', {'IpId': IpId,'msg':'必填项存在空，请从新填写'})
    else:
        return render(request,'web/dbuseradd.html',{'IpId':IpId})

def HostProjectAdd(request):
    return render(request,'')