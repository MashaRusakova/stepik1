import random

from django.shortcuts import render

from django.views import View


from .data import tours
from .data import title
from .data import departures
from .data import subtitle
from .data import description


class MainView(View):
    def get(self, request):
        tours_list = list(tours.items())
        tours_randomized = random.sample(tours_list, 6)

        return render(request, 'index.html', context={
            "tours": tours_randomized,
            "title": title,
            "subtitle": subtitle,
            "description": description,
            "departures": departures,
            }
        )


class DepartureView(View):
    def get(self, request, departure):
        tours_departure = [[tour_id, tour] for tour_id, tour in tours.items()
                           if tour["departure"] == departure]
        min_price = min([t[1]["price"] for t in tours_departure])
        max_price = max([t[1]["price"] for t in tours_departure])
        min_nights = min([t[1]["nights"] for t in tours_departure])
        max_nights = max([t[1]["nights"] for t in tours_departure])

        return render(
            request, 'departure.html', context={
                "title": title,
                "tours": tours_departure,
                "departure": departures[departure],
                "departures": departures,
                "min_price": min_price,
                "max_price": max_price,
                "min_nights": min_nights,
                "max_nights": max_nights,
            }
        )


class TourView(View):
    def get(self, request, id):
        return render(
            request, 'tour.html', context={
                "tours": tours[id],
                "title": title,
                "departures": departures,
            }
        )
