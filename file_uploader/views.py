from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from file_uploader.application import UploadApplication
from file_uploader.forms import CreateUploadForm
from file_uploader.models import FileUploader
from file_uploader.utils import generate_csv_template


def index(request):
    data = {'uploads': FileUploader.objects.all()}
    return render(request, 'uploaded_files.html', data)


def create_upload(request):
    if request.method == 'POST':
        form = CreateUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.create_upload(request.user)
            return redirect('index')

    form = CreateUploadForm()
    data = {
        'form': form,
    }
    return render(request, 'create_upload.html', data)


def apply_upload(request, upload_id):
    upload = FileUploader.objects.get(pk=upload_id)

    applier = UploadApplication(upload, request.user)
    applier.apply_file()

    upload.status = True
    upload.save()

    return redirect('index')


def download_template(request):
    return generate_csv_template()


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('signup')
