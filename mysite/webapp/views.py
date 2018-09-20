from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from .models import Student


# Create your views here.
def index(request):
    return render(request,'acc/home.html')
    
def contact(request):
    text = open("webapp\ReadIt.txt","r")
    content=[]
    for f in text:
        content.append(f)
    return render(request,'acc/cont.html',{'content' : content})


def info(request):
    data = Student.objects.all()
    return render(request,'acc/info.html',{'content' : data})


def studentForms(request):
    name = request.POST["name"]
    hobby = request.POST["hobby"]
    address = request.POST["address"]
    stu_info = Student(name=name,hobby=hobby,address=address)
    stu_info.save()
    return render(request,'acc/studentForms.html')

def fileWrite(request):
    
    content = request.POST.get("con",False)
    file = open("webapp\ReadIt.txt","w")
    file.write(str(content))
    file.close()
    return render(request,'acc/writeFile.html')
