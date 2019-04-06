#coding:gbk
#from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request,'home.html')

def count(request):
    len_count=len(request.GET['text'])
    usercount=request.GET['text']
    return render(request,'count.html',{'len_count':len_count,'usercount':usercount})

