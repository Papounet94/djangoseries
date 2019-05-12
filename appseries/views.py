from django.shortcuts import render
from django.http import HttpResponse
from appseries.models import Serie


# Create your views here.

def liste(request):

    series = Serie.objects.all().order_by('airing_date', 'title')
    #print(series)
    context = {
        'titre': 'Date de diffusion des Séries',
        'series': series,
    }

    return render(request, 'appseries/liste_series.html', context)

