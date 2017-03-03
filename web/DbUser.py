#_*_coding:utf-8 _*_

from models import *

class DBUSERINFO:
    def Add(self,HostId,HostUser,HostPwd):
        msg={}
        try:
            IdAdd = HostInfo.objects.get(ID=HostId)
            DbUserInfo.objects.create(HostId=IdAdd,HostUser=HostUser,HostPwd=HostPwd)
            msg['TrueBit'] = True
        except Exception, e:
            msg['TrueBit'] = False
            msg['ErrorMsg'] = e
        return msg
    def SelectHostIp(self):
        IpId= HostInfo.objects.all()
        return IpId

    def SelectHostIpByObjeck(self,ObjNum):
        pass
    def SelectHostIpByIp(self,Ip):
        pass

class PROJECTINFO:
    def ProjectAdd(self,ProgectName,ProgecDescription):
        msg={}
        try:
            ProjectInfo.objects.create(ProgectName=ProgectName,ProgectDescription=ProgecDescription)
            msg['TrueBit'] = True
        except Exception,e:
            msg['TrueBit'] = False
            msg['ErrorMsg'] = e
        return msg