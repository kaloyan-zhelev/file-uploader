from django.forms import forms
from django.utils import timezone

from file_uploader.models import FileUploader


class CreateUploadForm(forms.Form):
    file = forms.FileField()

    def create_upload(self, user):
        FileUploader.objects.create(
            created_at=timezone.now(),
            file=self.cleaned_data['file'],
            user=user,
        )
