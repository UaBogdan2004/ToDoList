from django.shortcuts import render, redirect, get_object_or_404
from django.template.defaultfilters import title

from .models import Task

def task_list(request):
    filter_status = request.GET.get('status', 'all')
    if filter_status == 'completed':
        tasks = Task.objects.filter(is_completed=True).order_by('-created_at')
    elif filter_status == 'incomplete':
        tasks = Task.objects.filter(is_completed=False).order_by('-created_at')
    else:
        tasks = Task.objects.all().order_by('created_at')
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

def create_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        Task.objects.create(title=title, description=description)
        return redirect('task_list')
    return render(request, 'tasks/create_task.html')

def toggle_task_status(request, task_id):
    task = Task.objects.get(id=task_id)
    task.is_completed = not task.is_completed
    task.save()
    return redirect('task_list')

def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('task_list')