#_*_coding:utf-8 _*_

from models import *
class HOSTINFO:
    def SelectHostAll(self):
        IpId= HostInfo.objects.all()
        return IpId

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
    def SelectProjectId(self):
        SelectProjectId = ProjectInfo.objects.all()
        return SelectProjectId

class HOSTMSG:
    def HostMsgAdd(self,HostId,ProjectId):
        msg = {}
        try:
            HostIdAdd = HostInfo.objects.get(ID=HostId)
            ProjectIdAdd = ProjectInfo.objects.get(ID=ProjectInfo)
            HostMsg.objects.create(HostId=HostIdAdd,ProjectId=ProjectIdAdd)
            msg['TrueBit'] = True
        except Exception,e:
            msg['TrueBit'] = False
            msg['ErrorMsg'] = e
        return msg
    def SelectFromProjectId(self,ProjectId):
        pass