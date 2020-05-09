from django.conf import settings
from django.shortcuts import render

from django.views import View

from .data import tours

class MainView(View):
    def get(self, request, *args, **kwargs):
        return render(
            request, 'tours/index.html', context=tours
        )


class DepartureView(View):
    def get(self, request, *args, **kwargs):
        return render(
            request, 'tours/departure.html', context=tours
        )


class TourView(View):
    def get(self, request, id=1):

        return render(
            request, 'tours/tour.html', context = {'tour': tours[id]}
        )
