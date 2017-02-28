#_*_coding:utf-8_*_
from django import forms

class HOSTADD(forms.Form):
    HostIp = forms.GenericIPAddressField()
    HostName = forms.CharField()
    HostDescription = forms.CharField()