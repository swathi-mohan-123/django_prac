from django.shortcuts import render
from .forms import groceryform


# Create your views here.
def homeadd1(request):
    form = groceryform(request.POST or None)
    Price={
        "Wheat":40,
        "Jaggery":80,
        "Dal":100,
   
    }
    dict={}
  
    i=0
   
    itemname='none'
    
    if request.method =='POST':
        newform= groceryform(request.POST)
        if newform.is_valid():
            itemname=newform.cleaned_data['itemname']
    for i in itemname:
        dict.update({i:Price[str(i)]})

   
    
    context={"itemname":itemname,"dict":dict}
    return render(request,'groceryresult.html',context)

def grocery(request):
        form = groceryform(request.POST or None)
        context={'form':form}
        return render(request,'grocery.html',context)
def groceryresult(request):
    return render(request,'groceryresult.html')