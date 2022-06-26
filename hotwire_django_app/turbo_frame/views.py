import http
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from hotwire_django_app.tasks.models import Task
from hotwire_django_app.tasks.forms import TaskForm


def list_view(request):
    object_list = Task.objects.all().order_by("-pk")
    context = {
        "object_list": object_list,
    }
    return render(request, "turbo_frame/list_page.html", context)


def create_view(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            instance = form.save()
            messages.success(request, "Task created successfully")
            return redirect(
                reverse("turbo-frame:task-detail", kwargs={"pk": instance.pk})
            )
        status = http.HTTPStatus.UNPROCESSABLE_ENTITY
    else:
        status = http.HTTPStatus.OK
        form = TaskForm()
    return render(
        request, "turbo_frame/create_page.html", {"form": form}, status=status
    )


def update_view(request, pk):
    instance = get_object_or_404(Task, pk=pk)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            messages.success(request, "Task update successfully")
            return redirect(
                reverse("turbo-frame:task-detail", kwargs={"pk": instance.pk})
            )
        status = http.HTTPStatus.UNPROCESSABLE_ENTITY
    else:
        status = http.HTTPStatus.OK
        form = TaskForm(instance=instance)
    return render(
        request, "turbo_frame/update_page.html", {"form": form}, status=status
    )


def delete_view(request, pk):
    instance = get_object_or_404(Task, pk=pk)
    if request.method == "POST":
        instance.delete()
        messages.success(request, "Task deleted successfully")
        return redirect("turbo-frame:task-list")
    return render(request, "turbo_frame/delete_page.html", {"instance": instance})


def detail_view(request, pk):
    instance = get_object_or_404(Task, pk=pk)
    return render(request, "turbo_frame/detail_page.html", {"instance": instance})
