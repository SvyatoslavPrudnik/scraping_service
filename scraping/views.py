from django.shortcuts import render
import datetime
from django.core.paginator import Paginator

from .models import Vacancy
from .forms import FindForm


def home_view(request):
    form = FindForm()

    return render(request, 'scraping/home.html', context={'form': form})

def list_view(request):
    city = request.GET.get('city')
    language = request.GET.get('language')
    context = {'language': language, 'city': city}
    if city or language:
        _filter = {}
        if city:
            _filter['city__slug'] = city
        if language:
            _filter['language__slug'] = language 
        qs = Vacancy.objects.filter(**_filter)
        p = Paginator(qs, 10)
        page_number = request.GET.get('page')
        page_obj = p.get_page(page_number)
        context['object_list'] = page_obj
    return render(request, 'scraping/list.html', context)