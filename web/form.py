#_*_coding:utf-8_*_
from django import forms

class HOSTADD(forms.Form):
    HostIp = forms.GenericIPAddressField(error_messages={'invalid':('IP格式错误')})
    HostName = forms.CharField()
    HostDescription = forms.CharField()
class DbUserAdd(forms.Form):
    DbUser = forms.CharField()
    DbPasword = forms.CharField()