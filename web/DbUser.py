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
            ProjectIdAdd = ProjectInfo.objects.get(ID=ProjectId)
            HostMsg.objects.create(HostId=HostIdAdd,ProjectId=ProjectIdAdd)
            msg['TrueBit'] = True
        except Exception,e:
            msg['TrueBit'] = False
            if int(e[0])==1062:
                msg['ErrorMsg'] = '添加的IP隶属于其他项目，不能重复添加'
            else:
                msg['ErrorMsg'] = e
        return msg
    def SelectFromProjectId(self,ProjectId):
        msg={}
        HostOne = {}
        HostIpMag = []
        try:
            HostID = HostMsg.objects.filter(ProjectId__ID=ProjectId)
            for item in HostID:
                HostOne['Ip'] = item.HostId.HostIp
                HostOne['HostDescription'] = item.HostId.HostDescription
                HostIpMag.append(HostOne)
            msg['TrueBit'] = True
            msg['HostIp'] = HostIpMag
        except Exception,e:
            msg['TrueBit'] = False
            msg['ErrorMsg']=e
        return msg