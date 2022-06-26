from django.urls import path
from .views import list_view, create_view, update_view, delete_view, detail_view

app_name = "turbo-frame"

urlpatterns = [
    path("list/", list_view, name="task-list"),
    path("create/", create_view, name="task-create"),
    path("<int:pk>/", detail_view, name="task-detail"),
    path("<int:pk>/update/", update_view, name="task-update"),
    path("<int:pk>/delete/", delete_view, name="task-delete"),
]
