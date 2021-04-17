from django.shortcuts import render,redirect
from .models import Task
from .forms import TodoForms
from django.views.generic import ListView,DetailView
from django.views.generic.edit import UpdateView,DeleteView
from django.urls import reverse_lazy

# Create your views here.


class TaskListView(ListView):
    model = Task
    template_name = 'tasklist.html'
    context_object_name = 'tasks'

class TaskDetailView(DetailView):
    model = Task
    template_name = 'detail.html'
    context_object_name = 'i'

class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'update.html'
    context_object_name = 'task'
    fields = ('name','priority','date')

    def get_success_url(self):
        return reverse_lazy('detail',kwargs={'pk':self.object.id})

class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'delete.html'
    success_url = reverse_lazy('taskListview')

def taskList(request):

    objects = Task.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        priority = request.POST.get('priority')
        date = request.POST.get('date')
        obj = Task(name=name, priority=priority,date=date)
        obj.save()
    return render(request, 'tasklist.html',{'tasks':objects})


# def task(request):
#     if request.method == "POST":
#         name = request.POST.get('name')
#         priority = request.POST.get('priority')
#         obj = Task(name=name, priority=priority)
#         obj.save()
#     return render(request,'task.html')


def delete(request,id):
    obj = Task.objects.get(id=id)
    if request.method == 'POST':
        obj.delete()
        return  redirect('/')
    return render(request,'delete.html',{'task':obj})


def update(request,id):
    obj = Task.objects.get(id=id)
    form = TodoForms(request.POST or None , instance=obj)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'task':obj,'form':form})

