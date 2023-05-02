from django.shortcuts import render
from .models import studentmodel,marksmodel
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import addform,dispform,deleteform,updateform

def index(request):
    return render(request,'index.html')

def add(request):
    context={}
    total=0
    student_number=""
    first_name=""
    last_name=""
    email=""
    field_of_study=""
    gpa=""
    english=0
    physics=0
    chem=0
    total=0
    form=addform()
    form=addform(request.POST or None)
    if request.method=='POST':
        newform=addform(request.POST)
        if newform.is_valid():
            student_number=newform.cleaned_data['student_number']
            first_name=newform.cleaned_data['first_name']
            last_name=newform.cleaned_data['last_name']
            email=newform.cleaned_data['email']
            field_of_study=newform.cleaned_data['field_of_study']
            gpa=newform.cleaned_data['gpa']
            english=newform.cleaned_data['english']
            physics=newform.cleaned_data['physics']
            chem=newform.cleaned_data['chem']
            total=int(physics)+int(chem)+int(english)
            studobj=studentmodel.objects.create(student_number=student_number, first_name=first_name,last_name=last_name, email=email, gpa=gpa, field_of_study=field_of_study)
            marksobj=marksmodel.objects.create(student_number=student_number,chem=chem,english=english,physics=physics,total=total)
            
            

    context={'form':form}
    return render(request, 'add.html',context)

def search(request):
    field_of_study=""
    list=[]
    english=0
    student_number=0
    studobj=""
    marksobj=""
    context={}
    form=dispform()
    form=dispform(request.POST or None)
    if request.method=='POST':
        newform=dispform(request.POST)
        if newform.is_valid():
            field_of_study=newform.cleaned_data['field_of_study']
            english=newform.cleaned_data['english']
            studobj=studentmodel.objects.all().filter(field_of_study=field_of_study)
            marksobj=marksmodel.objects.all().filter(english=english).filter(physics=100)
            for mark in marksobj:
                list.append(studentmodel.objects.get(student_number=mark.student_number))

    context={'form':form,'studobj':studobj,'marksobj':marksobj,'list':list}
    return render(request,'search.html',context)

def display(request):
    context={}
    list=[]
    student_number=""
    studobj=studentmodel.objects.all()
    for stud in studobj:
        list.append(marksmodel.objects.get(student_number=stud.student_number))
        context={'studobj':studobj,'marksobj':list,'s':stud.student_number}
        return render(request,'display.html',context)

def delete(request):
    student_number=""
    studobj=""
    marksobj=""
    context={}
    form=deleteform()
    form=deleteform(request.POST or None)
    if request.method=='POST':
        newform=deleteform(request.POST)
        if newform.is_valid():
            student_number=newform.cleaned_data['student_number']
            studobj=studentmodel.objects.get(student_number=student_number)
            marksobj=marksmodel.objects.get(student_number=student_number)
            studobj.delete()
            marksobj.delete()
    context={'form':form,'student_number':student_number}
    return render(request,'delete.html',context)



def update(request):
    context={}
    student_number=""
    studentobj=""
    marksobj=""

    form=deleteform()
    form=deleteform(request.POST or None)
    if request.method=='POST':
        newform=deleteform(request.POST)
        if newform.is_valid():
            student_number=newform.cleaned_data['student_number']
            studentobj=studentmodel.objects.get(student_number=student_number)
            marksobj=marksmodel.objects.get(student_number=student_number)
            form1=updateform()
            context={'form':form1,'studentobj':studentobj,'marksobj':marksobj}
            return render(request,'update2.html',context)
        else:
            context={'studobj':studentobj,'marksobj':marksobj,'form':form}
            return render(request,'update2.html',context)
    else:
        context={'form':form}
        return render(request,'update.html',context)

def update2(request,id):
    context={}
    fn="none"
    studentobj=""
    form1=updateform()
    form1=updateform(request.POST or None)
    if request.method=='POST':
        newform1=updateform(request.POST)
        if newform1.is_valid():
            student_number=id
            first_name=newform1.cleaned_data['first_name']
            last_name=newform1.cleaned_data['last_name']
            email=newform1.cleaned_data['email']
            field_of_study=newform1.cleaned_data['field_of_study']
            gpa=newform1.cleaned_data['gpa']
            studentobj=studentmodel.objects.get(student_number=id)
            studentobj.first_name=first_name
            studentobj.last_name=last_name
            studentobj.email=email
            studentobj.field_of_study=field_of_study
            studentobj.gpa=gpa
            studentobj.save()
        context={'form':form1,'studentobj':studentobj,"fn":first_name}
        return render(request,'update2.html',context)
    return render(request,'update2.html',context)
    
