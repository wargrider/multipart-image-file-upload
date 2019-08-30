from django.shortcuts import render, redirect

from .models import Picture
from .forms import UserForm


def index(request):
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(display_url)
    else:
        form = UserForm()

    return render(request, "image_upload_app/cover.html", {'form': form})


def display_url(request):
    if request.method == 'GET':
        # getting all the objects of Post.
        image = Picture.objects.all()
        return render(request, "image_upload_app/display_url.html", {'image': image})
