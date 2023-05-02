from django.shortcuts import render
from .forms import displayform, humanform
from .models import humanmodel

def index4(request):
    return render(request,'index4.html')

def display1(request):
    context={}
    fname="none"
    lname=""
    phone=0
    addr=""
    city=""
    form=displayform(request.POST or None)
    if request.method=='POST':
        newform=displayform(request.POST)
        if newform.is_valid():
            fname=newform.cleaned_data['fname']
            humanmodel.objects.create(fname=fname,lname=lname,phone=phone,addr=addr,city=city)
    context={'fname':fname,'form':form}
    return render(request,'display1.html',context)


def display2(request):
    context={}
    fname="none"
    lname=""
    phone=0
    addr=""
    city=""
    form=humanform()
    if request.method=='POST':
        newform=humanform(request.POST)
        if newform.is_valid():
            lname=newform.cleaned_data['lname']
            phone=newform.cleaned_data['phone']
            addr=newform.cleaned_data['addr']
            city=newform.cleaned_data['city']
            
    
    context={'form':form}
    return render(request,'display1.html',context)




# Create your views here.
