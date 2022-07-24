from ast import Return
from multiprocessing import context
from django.shortcuts import render

from main.forms import TaskForm
from.models import Task
from django.shortcuts import render,redirect

def index(request):
    tasks=Task.objects.order_by('-id')
    return render(request,'main/index.html',{'title':'Главаня страница сайта','tasks':tasks})


def about(request):
    return render(request,'main/about.html')

def create(request):
    error=''
    if request.method=='POST':
        form=TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error='Форма была не верной'
    form=TaskForm()
    context={
        'form':form,
        'error':error
    }
    return render(request,'main/create.html',context)