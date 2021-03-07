from django.conf import settings
from django.db import models


class FileUploader(models.Model):
    TEMPLATE_HEADER = ['currency_type', 'expiration_date', 'client_email']

    created_at = models.DateTimeField()
    file = models.FileField(upload_to='uploaded_files/')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    status = models.BooleanField(default=False)

    @property
    def file_name(self):
        return self.file.name.split('/')[-1]
