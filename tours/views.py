from django.conf import settings
from django.shortcuts import render

from django.views import View

title = "Stepik Travel"
subtitle = "Для тех, кого отвлекают дома"
description = "Лучшие направления, где никто не будет вам мешать сидеть на берегу и изучать программирование, дизайн, разработку игр и управление продуктами"
departures = {"msk":"Из Москвы","spb":"Из Петербурга","nsk":"Из Новосибирска","ekb":"Из Екатеринбурга","kazan":"Из Казани"}

tours = {
    1: {
        "title": "Marina Lake Hotel & Spa",
        "description" : "Отель выглядит уютно. Он был построен из красного соснового дерева и украшен синими камнями.  Высокие округлые окна добавляют общий стиль дома и были добавлены в дом в довольно симметричном образце.",
        "departure":"nsk",
        "picture": "https://images.unsplash.com/photo-1551882547-ff40c63fe5fa?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=800&q=60",
        "price": 62000,
        "stars": "4",
        "country": "Куба",
		"nights":6,
		"date": "2 марта",
    },
    2: {
        "title": "Baroque Hotel",
        "description" : "Здание отеля имеет форму короткой буквы U. Два расширения связаны стеклянными нависающими панелями. Второй этаж такого же размера, как и первый, который был построен точно над полом под ним. Этот этаж имеет совершенно другой стиль, чем этаж ниже.",
        "departure": "ekb",
        "picture": "https://images.unsplash.com/photo-1445019980597-93fa8acb246c?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=800&q=60",
        "price": 85000,
        "stars": "5",
        "country":"Вьетнам",
		"nights":8,
		"date": "12 января",
    },
    3: {
        "title": "Voyager Resort",
        "description": "Снаружи отель выглядит красиво и традиционно. Он был построен с белыми камнями и имеет еловые деревянные украшения. Высокие, большие окна добавляют к общему стилю дома и были добавлены в дом в основном симметричным способом.",
        "departure": "nsk",
        "picture": "https://images.unsplash.com/photo-1569660072562-48a035e65c30?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=800&q=60",
        "price": 63000,
        "stars": "3",
        "country":"Пакистан",
		"nights": 11,
		"date": "7 февраля",
        },
    4: {
        "title": "Orbit Hotel",
        "description": "Каждый домик оборудован средней кухней и одной небольшой ванной комнатой, в нем также есть уютная гостиная, две спальни, скромная столовая и большой подвал.  Небольшие треугольные окна добавляют к общему стилю дома и были добавлены в дом в основном симметричным способом.",
        "departure": "msk",
        "picture": "https://images.unsplash.com/photo-1520250497591-112f2f40a3f4?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=800&q=60",
        "price": 62000,
        "stars": "4",
        "country":"Индия",
		"nights":9,
		"date": "22 января",
    },
    5: {
        "title": "Atlantis Cabin Hotel",
        "description": "Этот дом среднего размера имеет футуристический вид и находится в среднем состоянии. Интерьер выполнен в насыщенных тонах. Двор небольшой и выглядит очень формально. Кроме того, странные огни были замечены движущимися в доме ночью.",
        "departure": "msk",
        "picture": "https://images.unsplash.com/photo-1566073771259-6a8506099945?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=800&q=60",
        "price": 68000,
        "stars": "4",
        "country":"Доминикана",
		"nights":8,
		"date": "18 января",
    },
    6: {
        "title": "Light Renaissance Hotel",
        "description": "Этот крошечный дом выглядит довольно современно и находится в ужасном состоянии. Интерьер выполнен в цветах, которые напоминают вам о тропическом лесу. Двор небольшой и заросший дикими растениями. Кроме того, это было однажды показано в телесериале, демонстрирующем необычно украшенные дома.",
        "departure": "spb",
        "picture": "https://images.unsplash.com/photo-1571896349842-33c89424de2d?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=800&q=60",
        "price": 53000,
        "stars": "3",
        "country": "Пакистан",
		"nights":13,
		"date": "15 февраля",
    },
    7: {
        "title": "King's Majesty Hotel",
        "description": "Этот дом средних размеров выглядит немного старомодно и находится в среднем состоянии. Интерьер выполнен в цветах, которые напоминают о весеннем цветнике. Двор среднего размера и напоминает луг. Кроме того, он был построен над остатками дома, который был разрушен в результате пожара.",
        "departure": "ekb",
        "picture": "https://images.unsplash.com/photo-1468824357306-a439d58ccb1c?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=800&q=60",
        "price": 72000,
        "stars": "5",
        "country": "Мексика",
		"nights": 9,
		"date": "22 января",
    },
    8: {
        "title": "Crown Hotel",
        "description": "Этот огромный дом почти выглядит инопланетянином и находится в среднем состоянии. Интерьер выполнен в цветах, напоминающих апельсиновое дерево. Двор среднего размера и напоминает луг. Кроме того, это место печально известного убийства.",
        "departure": "kazan",
        "picture": "https://images.unsplash.com/photo-1549109786-eb80da56e693?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=800&q=60",
        "price": 44000,
        "stars": "4",
        "country": "Тайланд",
		"nights":7,
		"date": "3 февраля",
    },
    9: {
        "title": "Seascape Resort",
        "description": "Этот большой дом имеет сказочный вид и находится в отличном состоянии. Интерьер выполнен в ярких цветах. Двор маленький и аккуратно подстрижен. На заднем дворе есть большой участок недавно созданной земли, а дом имеет большой решетчатый забор через него. На заднем дворе живут различные животные. Многие владельцы приложили согласованные усилия для поддержания этой собственности.",
        "departure": "nsk",
        "picture": "https://images.unsplash.com/photo-1570214476695-19bd467e6f7a?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=800&q=60",
        "price": 39000,
        "stars": "3",
        "country": "Индия",
		"nights":10,
		"date": "1 февраля",
    },
    10: {
        "title": "Rose Sanctum Hotel",
        "description": "Снаружи этот дом выглядит старым, но чудесным. Он был построен из желтого соснового дерева и украшен белым кирпичом. Короткие, широкие окна пропускают много света и были добавлены в дом очень симметричным способом.",
        "departure": "msk",
        "picture": "https://images.unsplash.com/photo-1560200353-ce0a76b1d438?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=800&q=60",
        "price": 52000,
        "stars": "4",
        "country": "Куба",
		"nights":10,
		"date": "30 января",
    },
    11: {
        "title": "Viridian Obelisk Hotel & Spa",
        "description": "В доме очень хороший двор с большими камнями, похожими на озеро. В задней части дома окна просторные, с большими окнами, они светлее, чтобы улучшить впечатление. Снаружи есть пять маленьких деревьев. Двор в очень хорошем состоянии и очень живописный. Есть пруд для развлечения",
        "departure": "spb",
        "picture": "https://images.unsplash.com/photo-1477120128765-a0528148fed2?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=800&q=60",
        "price": 68000,
        "stars": "5",
        "country": "Индия",
		"nights":9,
		"date": "1 марта",
    },
    12: {
        "title": "Saffron Tundra Hotel & Spa",
        "description": "Дом оборудован огромной кухней и одной современной ванной комнатой, а также имеет огромную гостиную, две спальни, небольшую столовую, гостиную и скромную кладовую.  Дом чистый, хорошо построенный и в хорошем состоянии, но, к сожалению, кровати сгорели в мае этого года и, к сожалению, все еще нуждаются в ремонте. Возможно, понадобится целая команда, чтобы заменить старую медную топку.",
        "departure": "kazan",
        "picture": "https://images.unsplash.com/photo-1440151050977-247552660a3b?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=800&q=60",
        "price": 72000,
        "stars": "4",
        "country": "Мексика",
		"nights":12,
		"date": "17 февраля",
    },
    13: {
        "title": "Traveller Resort",
        "description": "Снаружи этот дом выглядит очень элегантно. Он был построен из коричневого кирпича и имеет коричневые кирпичные украшения. Высокие, большие окна добавляют к общему стилю дома и были добавлены к дому в довольно асимметричном образце. Крыша высокая и наклонена в одну сторону и покрыта коричневой черепицей. Один большой дымоход высовывает центр крыши. На крыше нет окон. Сам дом окружен великолепным садом с виноградными лозами, пагодой, прудом и множеством разных цветов.",
        "departure": "ekb",
        "picture": "https://images.unsplash.com/photo-1553653924-39b70295f8da?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=60",
        "price": 49000,
        "stars": "3",
        "country": "Куба",
		"nights":8,
		"date": "26 января"
    },
    14: {
        "title": "History Hotel & Spa",
        "description": "Крыша высокая, треугольная, многослойная, покрыта пшеничной соломой. Две большие трубы находятся по обе стороны от дома. Многие меньшие окна пропускают много света в комнаты под крышей.Сам дом окружен асфальтированной землей, с местом для еды и отдыха на открытом воздухе и различными горшечными растениями.",
        "departure": "kazan",
        "picture": "https://images.unsplash.com/photo-1509600110300-21b9d5fedeb7?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=800&q=60",
        "price": 91000,
        "stars": "5",
        "country": "Вьетнам",
		"nights":9,
		"date": "3 февраля",
    },
    15: {
        "title": "Riverside Lagoon Hotel & Spa",
        "description": "Здание имеет форму круга. Дом частично окружен деревянными нависающими панелями с двух сторон. Второй этаж меньше первого, что позволило создать несколько балконов по бокам дома. Этот этаж следует тому же стилю, что и этаж ниже.",
        "departure": "spb",
        "picture": "https://images.unsplash.com/photo-1568084680786-a84f91d1153c?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=800&q=60",
        "price": 82000,
        "stars": "4",
        "country": "Доминикана",
		"nights":8,
		"date": "5 февраля",
    },
    16: {
         "title": "History Hotel & Spa",
         "description": "Это высокое здание из старого кирпича. Крыша высокая, треугольная, многослойная, покрыта пшеничной соломой. В тесной квадратной спальне установлена деревянная и стеклянная мебель. Пол деревянный, а стены текстурированы и окрашены.Настенные и напольные светильники обеспечивают свет. Комната оформлена в цветах, напоминающих облачное небо, и в целом выглядит очень старомодно. Первое, что вы заметите, это тщеславие.",
         "departure": "spb",
         "picture": "https://images.unsplash.com/photo-1564056095795-4d63b6463dbf?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=800&q=60",
         "price": 74000,
         "stars": "5",
         "country": "Вьетнам",
		"nights":12,
		"date": "24 января",
     }

}

data = { "title":title,
         "subtitle":subtitle,
         "description":description,
         "departures":departures,
         "tours":tours}


class MainView(View):
    def get(self, request, *args, **kwargs):
        return render(
            request, 'tours/index.html', context=data
        )


class DepartureView(View):
    def get(self, request, *args, **kwargs):
        return render(
            request, 'tours/departure.html', context=data
        )


class TourView(View):
    def get(self, request, *args, **kwargs):
            return render(
                request, 'tours/tour.html', context=data
                )
