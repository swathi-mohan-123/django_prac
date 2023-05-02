from django.shortcuts import render
from .forms import carform





# Create your views here.

def home1(request):
    context={}
    cars="none"
    model="none"
    form=carform(request.POST or None)

    if request.method=="POST":
        newform=carform(request.POST)
        if newform.is_valid():
            cars=newform.cleaned_data['cars']
            model=newform.cleaned_data['model']
    context={'cars':cars, 'model':model, 'form':form}
    return render(request, 'result.html',context)

def myindex(request):
    form=carform(request.POST or None)
    context={'form':form}
    return render(request, 'myindex.html', context)

def result(request):
    return render(request, 'result.html')



