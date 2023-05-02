from django.shortcuts import render

# Create your views here.
def tech(request):
    return render(request,'tech.html')

def userform(request):
       
    return render(request, 'userform.html')