from django.shortcuts import render
from .forms import studentform







def secondpage(request):
    context={}
    name="none"
    roll="none"
    subject="none"
    form=studentform(request.POST or None)

    if request.method=='POST':
        newform=studentform(request.POST)
        if newform.is_valid():
            name=newform.cleaned_data['name']
            roll=newform.cleaned_data['roll']
            subject=newform.cleaned_data['subject']
    context={'name':name, 'roll':roll, 'subject':subject, 'form':form}
    return render(request,'secondpage.html', context)







def firstpage(request):
    form=studentform(request.POST or None)
    context={'form':form}
    return render(request, 'firstpage.html', context)


# Create your views here.


def home2(request):
    form=studentform()
    context={'form':form}
    return render(request, 'firstpage.html',context)