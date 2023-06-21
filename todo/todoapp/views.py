from django.shortcuts import render,redirect
from .models import todo
from .forms import todoform,editform

# Create your views here.
def  index(request):
    todos=todo.objects.all()
    
    if request.method=='POST':
        form=todoform(request.POST)   
        if form.is_valid:
            form.save()
        
        return redirect('/')
    else:
        form=todoform()

    context={
            'list':todos,
            'form':form,
            
        }

    return render(request,'main/index.html',context)

def edit(request,id):
    todos=todo.objects.get(id=id)
    if request.method=='POST':
        form=editform(request.POST,instance=todos)
        if form.is_valid:
            form.save()
            print('hello')
        return redirect('/')
    else:
        form=editform(instance=todos)
    
    context={
        'form':form
    }
    


    return render(request,'main/edit.html',context)

def delete(request,id):
    instance=todo.objects.get(id=id)
    if request.method=='POST':
        instance.delete()
        return redirect('/')
    else:
        return render(request,'main/delete.html')

        