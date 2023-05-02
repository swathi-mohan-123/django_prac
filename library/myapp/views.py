from django.shortcuts import render
from .models import bookmodel,studentmodel,issuemodel
from .forms import bookform,issueform,deleteform,issueform2

def addbook(request):
    context={}
    bookid=0
    bookname=""
    bookdesc=""
    bookobj=""
    form=bookform()
    form=bookform(request.POST or None)
    if request.method=='POST':
        newform=bookform(request.POST)
        if newform.is_valid():
            bookid=newform.cleaned_data['bookid']
            bookname=newform.cleaned_data['bookname']
            bookdesc=newform.cleaned_data['bookdesc']
            bookobj=bookmodel.objects.create(bookid=bookid,bookname=bookname,bookdesc=bookdesc)
    context={'form':form}
    return render(request,'addbook.html',context)

def viewbook(request):
    context={}
    bookobj=""
    form=deleteform()
    bookobj=bookmodel.objects.all()
    context={'bookobj':bookobj,'form':form}
    return render(request,'viewbook.html',context)

def issuebook(request):
    context={}
    bookid=0
    bookname=""
    bookdesc=""
    studname=""
    studid=0
    form=issueform()
    form=issueform(request.POST or None)
    if request.method=='POST':
        newform=issueform(request.POST)
        if newform.is_valid():
            bookid=newform.cleaned_data['bookid']
            studid=newform.cleaned_data['studid']
            bookname=newform.cleaned_data['bookname']
            studname=newform.cleaned_data['studname']
            bookdesc=newform.cleaned_data['bookdesc']
            studobj=studentmodel.objects.create(studid=studid,studname=studname,bookid=bookid)
            issueobj=issuemodel.objects.create(studid=studid,studname=studname,bookid=bookid,bookdesc=bookdesc,bookname=bookname)
    context={'form':form}
    return render(request,'issuebook.html',context)

def viewissuebook(request):
    context={}
    issueobj=""
    issueobj=issuemodel.objects.all()
    context={'issueobj':issueobj}
    return render(request,'viewissuebook.html',context)

def delete(request):
    context={}
    bookid=0
    studobj=""
    bookobj=""
    newbookobj=""
    issueobj=""
    form=deleteform()
    if request.method=='POST':
        newform=deleteform(request.POST)
        if newform.is_valid():
            bookid=newform.cleaned_data['bookid']
            bookobj=bookmodel.objects.all().filter(bookid=bookid)
            studobj=studentmodel.objects.all().filter(bookid=bookid)
            issueobj=issuemodel.objects.all().filter(bookid=bookid)
            for book in bookobj:
                book.delete()
            for stud in studobj:
                stud.delete()
            for issue in issueobj:
                issue.delete()
    newbookobj=bookmodel.objects.all()
    context={'bookobj':newbookobj,'form':form}
    return render(request,'viewbook.html',context)

def issuebook2(request):
    bookid=0
    studid=0
    context={}
    form=issueform2()
    form=issueform2(request.POST or None)
    if request.method=='POST':
        newform=issueform2(request.POST)
        if newform.is_valid():
            bookid=newform.cleaned_data['bookid']
            studid=newform.cleaned_data['studid']
    context={'form':form,'bookid':bookid,'studid':studid}
    return render(request,'issuebook2.html',context)


def viewissuebook2(request,bookid):
    context={}
    studobj=""
    bookobj=""
    studobj=studentmodel.objects.all().filter(bookid=bookid)
    bookobj=bookmodel.objects.all().filter(bookid=bookid)
    context={'studobj':studobj,'bookobj':bookobj}
    return render(request,'viewissuebook2.html',context)











    




# Create your views here.
