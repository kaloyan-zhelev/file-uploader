from django.conf import settings
from django.db import models


class Contract(models.Model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    currency_type = models.CharField(max_length=25)
    expiration_date = models.DateField()
    client_email = models.EmailField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)

    @classmethod
    def create_record(cls, contract_data, user):
        cls.objects.create(
            created_at=contract_data.created_at,
            updated_at=contract_data.updated_at,
            currency_type=contract_data.currency_type,
            expiration_date=contract_data.expiration_date,
            client_email=contract_data.client_email,
            user=user,
        )
