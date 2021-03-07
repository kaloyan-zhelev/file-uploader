import csv

from django.utils import timezone

from contracts.models import Contract
from file_uploader.models import FileUploader


class ContractAttributes:
    def __init__(self, **kwargs):
        self.created_at = timezone.now()
        self.updated_at = timezone.now()
        self.currency_type = kwargs.get('currency_type')
        self.expiration_date = kwargs.get('expiration_date')
        self.client_email = kwargs.get('client_email')


class UploadApplication:
    def __init__(self, upload, user):
        self.upload = upload
        self.attributes_class = ContractAttributes
        self.user = user

    def _parse_upload(self):
        reader = csv.reader(row.decode('utf-8') for row in self.upload.file)
        for line in reader:
            # Skip empty rows
            if all(not item for item in line):
                continue
            if line[0] == 'currency_type':
                continue

            product_attributes = {
                attr: value for (attr, value) in zip(FileUploader.TEMPLATE_HEADER, line)
            }

            yield self.attributes_class(**product_attributes)

    def apply_file(self):
        for contract_data in self._parse_upload():
            Contract.create_record(contract_data, self.user)
