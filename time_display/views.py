from django.shortcuts import render, HttpResponse
from time import gmtime, strftime
    
def index(request):
    context = {
        "time": strftime("%A %B %dth, %Y %H:%M %p", gmtime())
    }
    return render(request,'index.html', context)

def time_display(request):
    context = {
        "time": strftime("%Y-%m-%d %H:%M %p", gmtime())
    }
    return render(request,'index.html', context)





