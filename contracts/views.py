from django.shortcuts import render

from contracts.models import Contract


def contracts(request):
    data = {'contracts': Contract.objects.all()}
    return render(request, 'contracts.html', data)
