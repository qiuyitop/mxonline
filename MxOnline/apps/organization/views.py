#_*_encoding:utf-8_*_
from django.shortcuts import render
from django.views.generic.base import View


class OrgView(View):
    '''课程机构'''
    def get(self,request):
        return render(request,'org-list.html')