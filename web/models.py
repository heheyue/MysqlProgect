# _*_coding=utf-8_*_
from __future__ import unicode_literals
from django.db import models

# Create your models here.
#主机信息表
class HostInfo(models.Model):
    ID = models.AutoField(primary_key=True)
    HostIp=models.GenericIPAddressField(unique=True)
    HostName = models.CharField(max_length=100,default=None)
    HostDescription = models.CharField(max_length=500)
    DelBit = models.BooleanField(default=False)
    AddTime=models.DateTimeField(auto_now_add=True)
#数据库信息表
class DbInfo(models.Model):
    ID = models.AutoField(primary_key=True)
    HostId = models.OneToOneField(HostInfo)
    DbName = models.CharField(max_length=50)
    TableName = models.CharField(max_length=500)
    UpTime = models.DateTimeField(auto_now=True)
#项目列表
class ProjeckInfo(models.Model):
    ID = models.AutoField(primary_key=True)
    ProgeckName = models.CharField(max_length=500)
    DelBit = models.BooleanField(default=False)
    AddTime=models.DateTimeField(auto_now_add=True,unique=True)
#数据库备份文件路径信息表
class DbFileInfo(models.Model):
    ID = models.AutoField(primary_key=True)
    HostId = models.OneToOneField(HostInfo)
    DbPath = models.CharField(max_length=200)
    TablePath = models.CharField(max_length=200)
#数据库登录信息表
class DbUserInfo(models.Model):
    ID = models.AutoField(primary_key=True)
    HostId = models.OneToOneField(HostInfo)
    HostUser = models.CharField(max_length=20)
    HostPwd = models.CharField(max_length=100)
#主机项目关联表
class HostMsg(models.Model):
    ID = models.AutoField(primary_key=True)
    HostId = models.OneToOneField(HostInfo)
    ProjeckId = models.OneToOneField(ProjeckInfo)