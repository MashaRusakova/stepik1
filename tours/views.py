import random

from django.conf import settings
from django.shortcuts import render

from django.views import View

from random import sample
from .data import tours
from .data import title
from .data import departures
from .data import subtitle
from .data import description


class MainView(View):
    def get(self, request):
        tours_list = list(tours.values())
        tours_randomized = random.sample(tours_list, 6)
        return render(request, 'tours/index.html', context = {
            "tour" : tours_randomized,
            "title": title,
            "subtitle": subtitle,
            "description": description,
            "departures": departures
            }
        )


class DepartureView(View):
    def get(self, request, depature):
        return render(
            request, 'tours/departure.html', context = {
                "tour": tours[id],
                "title": title,
                "subtitle": subtitle,
                "description": description,
                "departures": departures[depature]
            }
        )


class TourView(View):
    def get(self, request, id):
        return render(
            request, 'tours/tour.html', context = {
                "tour": tours[id],
                "title" : title,
                "departures" : departures
            }
        )
