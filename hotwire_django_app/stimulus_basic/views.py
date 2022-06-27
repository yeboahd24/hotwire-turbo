from django.shortcuts import render

# Create your views here.
def counter_view(request):
    return render(request, "stimulus_basic/counter.html")


def turbo_frame_load_view(request):
    return render(request, "stimulus_basic/turbo_frame_load.html")
