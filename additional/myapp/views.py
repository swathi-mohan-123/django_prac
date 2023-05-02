from django.shortcuts import render
from .forms import nameform,restform
from .models import humanmodel

# Create your views here.
def create(request):
    context={}
    fname=""
    form1=""
    form=nameform()
    form=nameform(request.POST or None)
    if request.method=='POST':
        newform=nameform(request.POST)
        if newform.is_valid():
            fname=newform.cleaned_data['fname']
            form1=restform()
            context={'fname':fname,'form':form1}
            if request.method=='POST':
                return render(request,'index2.html',context)
            context={'form':form1}
            return render(request,'index2.html',context)
    context={'form':form}
    
    return render(request,'index.html',context)

def create1(request):
    form=nameform()
    context={'form':form}
    return render(request,'index.html',context)

def create2(request,fname):
    context={}
    form1=""
    lname=""
    phone=0
    addr=""
    city=""
    humanobj=""
    form=restform()
    form=restform(request.POST or None)
    if request.method=='POST':
        newform1=restform(request.POST)
        if newform1.is_valid():
            fname=fname
            lname=newform1.cleaned_data['lname']
            phone=newform1.cleaned_data['phone']
            addr=newform1.cleaned_data['addr']
            city=newform1.cleaned_data['city']
            humanobj=humanmodel.objects.create(fname=fname,lname=lname,phone=phone,addr=addr,city=city)
            form1=nameform()
            context={'form':form1}
            return render(request,'index.html',context)

def delete(request):
    context={}
    fname=""
    humanobj=""
    form1=""
    form=nameform()
    form=nameform(request.POST or None)
    if request.method=='POST':
        newform=nameform(request.POST)
        if newform.is_valid():
            fname=newform.cleaned_data['fname']
            humanobj=humanmodel.objects.all().filter(fname=fname)
            for human in humanobj:
                human.delete()
    context={'form':form,'humanobj':humanobj}
    return render(request,'index.html',context)


    


