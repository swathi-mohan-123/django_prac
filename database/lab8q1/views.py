from django.shortcuts import render
from .forms import categoryform, pageform
from .models import categorymodel, pagemodel

# Create your views here.
def index1(request):
    return render(request,'index1.html')

def category(request):
    context={}
    nm=''
    nov=0
    nol=0
    form=categoryform(request.POST or None)

    if request.method=='POST':
        newcategoryform=categoryform(request.POST)
        if newcategoryform.is_valid():
            nm=newcategoryform.cleaned_data['name']
            nov=newcategoryform.cleaned_data['numberofvisits']
            nol=newcategoryform.cleaned_data['numberoflikes']
            categorymodel.objects.create(name=nm,numberofvisits=nov, numberoflikes=nol)
    context={'form':form}
    return render(request, 'category.html',context)


def page(request):
    context={}
    category=''
    title=0
    URL=''
    views=0
    form=pageform(request.POST or None)

    if request.method=='POST':
        newpageform=pageform(request.POST)
        if newpageform.is_valid():
            category=newpageform.cleaned_data['category']
            title=newpageform.cleaned_data['title']
            URL=newpageform.cleaned_data['URL']
            views=newpageform.cleaned_data['views']
            pagemodel.objects.create(category=category, title=title, URL=URL, views=views)
    context={'category':category,'title':title,'URL':URL,'form':form}
    return render(request, 'page.html',context)

def display(request):
    context={}
    categories=categorymodel.objects.all()
    pages=pagemodel.objects.all()
    context={'pages':pages,'categories':categories}
    return render(request,'display.html',context)
