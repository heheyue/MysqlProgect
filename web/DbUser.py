#_*_coding:utf-8 _*_

from models import HostInfo
from models import DbUserInfo

class DBUSERINFO:
    def SelectHostIp(self):
        IpId= HostInfo.objects.all()
        return IpId
    def SelectHostIpByObjeck(self,ObjNum):
        pass
    def SelectHostIpByIp(self,Ip):
        pass