from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

# Create your views here.
def home(req):
    return render(req, './home/index.html')


# def taskList(req):
#     tasks = Task.objects.all().order_by('-created_at')
#     return render(req, './tasks/list.html', {'tasks': tasks})

# def taskView(req, id):
#     task = get_object_or_404(Task, pk=id)
#     return render(req, './tasks/task.html', {'task': task})

# def yourName(req, name):
#     return render(req, './tasks/yourname.html', {'name': name})

# def newTask(req):
#     if req.method == 'POST':
#         form = TaskForm(req.POST)

#         if form.is_valid():
#             task = form.save(commit=False)
#             task.done = 'doing'
#             task.save()
#             return redirect('/task-list')
#     else:
#         form = TaskForm()
#         return render(req, './tasks/addtask.html', {'form': form})
