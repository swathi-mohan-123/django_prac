from django.shortcuts import render
from .forms import companyform,searchform
from .models import worksmodel, livesmodel
# Create your views here.

def index2(request):
    return render(request,'index2.html')

def portal(request):
    context={}
    name="none"
    company="none"
    salary=0
    street="none"
    city="none"
    form=companyform(request.POST or None)
    if request.method=='POST':
        newcompanyform=companyform(request.POST)
        if newcompanyform.is_valid():
            name=newcompanyform.cleaned_data['name']
            company=newcompanyform.cleaned_data['company']
            salary=newcompanyform.cleaned_data['salary']
            street=newcompanyform.cleaned_data['street']
            city=newcompanyform.cleaned_data['city']
            worksmodel.objects.create(name=name,company=company,salary=salary)
            livesmodel.objects.create(name=name, street=street,city=city)
    context={'name':name,'company':company,'salary':salary,'street':street,'city':city,'form':form}
    return render(request, 'portal.html',context)  


def search(request):
    comp=""
    details=""
    newdetails=[]
    livesobj=""
    context={}
    form=searchform(request.POST or None)
    if request.method=='POST':
        newsearchform=searchform(request.POST)
        if newsearchform.is_valid():
            comp=newsearchform.cleaned_data['company']
            details=worksmodel.objects.all().filter(company=comp)
            for detail in details:
                newdetails.append(livesmodel.objects.get(name=detail.name))
               
    context={'newdetails':newdetails,'form':form,'livesobj':livesobj}
    return render(request,'search.html',context)

