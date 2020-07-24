from webapp.models import Task
from django.shortcuts import redirect, get_object_or_404, render, HttpResponseRedirect
from webapp.models import STATUS_CHOICES


def index_view(request):
    tasks = Task.objects.all()
    return render(request, 'index.html', {'tasks': tasks})


def task_create_view(request):
    options = STATUS_CHOICES
    if request.method == 'GET':
        return render(request, 'add.html', {'options': options})
    elif request.method == 'POST':
        description = request.POST.get('description')
        status = request.POST.get('status')
        finish_date = request.POST.get('finish_date')
        detailed_desc = request.POST.get('detailed_desc')
        if not finish_date:
            finish_date = None
        if not detailed_desc:
            detailed_desc = None
        Task.objects.create(description=description, detailed_desc=detailed_desc, status=status, finish_date=finish_date)
        return redirect(index_view)


def delete_view(request, id):
    task = get_object_or_404(Task, id=id)
    if request.method == "POST":
        task.delete()
        return HttpResponseRedirect("/")
    return render(request, "delete_view.html", {'task': task})


def task_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'task_view.html', {'task': task})
