import csv

from django.http import HttpResponse

from file_uploader.models import FileUploader


def generate_csv_template():
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=template.csv'

    new_file = csv.writer(response)
    new_file.writerow(FileUploader.TEMPLATE_HEADER)

    return response
