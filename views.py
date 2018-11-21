from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import todoitem
# Create your views here.
def todoview(request):
    todo_all=todoitem.objects.all()
    return render(request,'index.html',{'all_item':todo_all})

def addtodo(request):
    new_item=todoitem(content= request.POST['content'])
    new_item.save()
    return HttpResponseRedirect('/todoview/')
