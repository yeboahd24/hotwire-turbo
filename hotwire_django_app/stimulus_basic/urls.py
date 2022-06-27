from django.urls import path
from .views import counter_view, turbo_frame_load_view


app_name = "stimulus-basic"
urlpatterns = [
    path("counter/", counter_view, name="counter"),
    path("turbo_frame_load/", turbo_frame_load_view, name="turbo_frame_load"),
]
