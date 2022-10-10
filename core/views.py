from django.shortcuts import render, HttpResponse
from .models import Bottle
from django.views import View


def contacts(request):
    return render(request, 'core/contacts.html')


def about(request):
    return render(request, 'about.html')


def makers_list(request):
    context = {}
    bottles_list = Bottle.objects.all()
    context['bottles_list'] = bottles_list
    html_page = render(request, 'makers.html', context)
    return html_page


def base(request):
    return render(request, 'base.html')


class MyView(View):
    def get(self, request):
        return render(request, 'about.html')
