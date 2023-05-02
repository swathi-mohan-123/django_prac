from django.shortcuts import render
from .forms import authorform, pubform, bookform,  booksearchform
from .models import authormodel, pubmodel, bookmodel


def index3(request):
    return render(request,'index3.html')

def author(request):
    context={}
    fname="none"
    lname="none"
    email="none"
    form=authorform(request.POST or None)
    if request.method=='POST':
        newform=authorform(request.POST)
        if newform.is_valid():
            fname=newform.cleaned_data['fname']
            lname=newform.cleaned_data['lname']
            email=newform.cleaned_data['email']
            authormodel.objects.create(fname=fname,lname=lname,email=email)
    context={'form':form}
    return render(request,'author.html',context)

def pub(request):
    context={}
    name="none"
    street="none"
    city="none"
    state="none"
    country="none"
    website="none"
    form=pubform(request.POST or None)
    if request.method=='POST':
        newform=pubform(request.POST)
        if newform.is_valid():
            name=newform.cleaned_data['name']
            street=newform.cleaned_data['street']
            city=newform.cleaned_data['city']
            state=newform.cleaned_data['state']
            country=newform.cleaned_data['country']
            website=newform.cleaned_data['website']
            pubmodel.objects.create(name=name,street=street, city=city, state=state,country=country, website=website)
    context={'form':form}
    return render(request,'pub.html',context)

def book(request):
    context={}
    title="none"
    date="none"
    aname=""
    pname="none"
    form=bookform(request.POST or None)
    if request.method=='POST':
        newform=bookform(request.POST)
        if newform.is_valid():
            title=newform.cleaned_data['title']
            date=newform.cleaned_data['date']
            aname=newform.cleaned_data['aname']
            pname=newform.cleaned_data['pname']
            pnameobj=pubmodel.objects.get(name=pname)
            bookmodel.objects.create(title=title, date=date,aname=aname, pname=pnameobj)
    context={'form':form}
    return render(request,'book.html',context)

def booksearch(request):
    context={}
    title="none"
    obj=""
    
    form=booksearchform(request.POST or None)
    if request.method=='POST':
        newform=booksearchform(request.POST)
        if newform.is_valid():
            title=newform.cleaned_data['title']
            obj=bookmodel.objects.get(title=title)
            
    context={'form':form,'obj':obj}
    return render(request,'booksearch.html',context)

# Create your views here.
