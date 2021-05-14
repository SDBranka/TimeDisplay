from django.shortcuts import render, HttpResponse
from time import gmtime, strftime
import datetime
    
def index(request):
    context = {
        "time": strftime("%A %B %dth, %Y %H:%M %p", gmtime())
    }
    return render(request,'index.html', context)

def time_display(request):
    context = {
        "time": datetime.datetime.now()
    }
    return render(request,'index.html', context)





