import http
from django.shortcuts import render, redirect, reverse
from hotwire_django_app.tasks.forms import TaskForm
from hotwire_django_app.tasks.models import Task
from django.contrib import messages


def create_view(request):
    import time
    time.sleep(1)
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
    # new
        status = http.HTTPStatus.UNPROCESSABLE_ENTITY
        messages.success(request, 'Task created successfully')
        return redirect(reverse('turbo-drive:task-list'))
    else:
        status = http.HTTPStatus.OK
        form = TaskForm()
    # update
    return render(request, 'turbo_drive/create.html', {'form': form}, status=status)


def list_view(request):
    import time
    time.sleep(1)
    # new
    object_list = Task.objects.all().order_by('-pk')
    context = {
    "object_list": object_list,
    }
    return render(request, 'turbo_drive/list.html', context)