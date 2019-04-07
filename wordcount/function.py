#coding:gbk
#from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request,'home.html')

def count(request):
    len_count=len(request.GET['text'])
    usercount=request.GET['text']
    word_count={}
    for word in usercount:
        if word not in word_count:
            word_count[word] = word_count.get(word,0)+1
        else:
            word_count[word] = word_count.get(word,0)+1
    sor_d = sorted(word_count.items(),key=lambda x:x[1],reverse=True)
    return render(request,'count.html',
                  {'len_count':len_count,'usercount':usercount,
                   'wordcount':word_count,'sorted':sor_d})

def about(request):
    return render(request,'about.html')
