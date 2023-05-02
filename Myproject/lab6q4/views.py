from django.shortcuts import render
from .forms import billform

# Create your views here.

mobcost={'HP':1000, 'Samsung':2000, 'Nokia':3000, 'Motorola':4000, 'Apple':5000}
lapcost={'HP':10000, 'Samsung':20000, 'Nokia':30000, 'Motorola':40000, 'Apple':50000}

def home4(request):
    context={}
    company="none"
    mobile="False"
    laptop="False"
    quantity=0
    price=0
    form=billform(request.POST or None)

    if request.method=='POST':
        newform=billform(request.POST)
        if newform.is_valid():
            company=newform.cleaned_data['company']
            quantity=newform.cleaned_data['quantity']
            mobile=newform.cleaned_data['mobile']
            laptop=newform.cleaned_data['laptop']

    if mobile==True:
        price=price+int(quantity)*mobcost[str(company)]
    if laptop==True:
        price=price+int(quantity)*lapcost[str(company)]

    context={'company':company,'mobile':mobile,'laptop':laptop,'quantity':quantity,'price':price}
    return render(request, 'bill.html', context)

def index4(request):
    form=billform(request.POST)
    context={'form':form}
    return render(request, 'index4.html', context)

def bill(request):
    form=billform()
    context={'form':form}
    return render(request, 'bill.html',context)
    




