from django.shortcuts import render
from .forms import RegForm
from .forms import loginform



def homesolved(request):
    context={}
    name="not loggedin in"
    email="not loggedin in"
    password="not loggedin in"
    process="not loggedin in"
    terms="not loggedin in"
    form=loginform(request.POST or None)

    if request.method=='POST':
        newform=loginform(request.POST)
        if newform.is_valid():
            name=newform.cleaned_data['name']
            email=newform.cleaned_data['email']
            password=newform.cleaned_data['password']
            process=newform.cleaned_data['process']
            terms=newform.cleaned_data['terms']
    context={'name':name, 'email':email, 'password':password, 'process':process, 'terms':terms, 'form':form}
    return render(request, 'loggedin.html',context)



    


def login(request):
    form=loginform(request.POST or None)
    context={'form':form}
    return render(request, 'login.html', context)




def loggedin(request):
    return render(request,'loggedin.html')






# Create your views here.
