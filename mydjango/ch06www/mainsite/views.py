from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.template.loader import get_template


from datetime import datetime



# def index(request):
#     template = get_template('base.html')
#
#     mes = 'Hello! World!'
#     now = datetime.now()
#
#
#     html = template.render(locals())
#
#     return HttpResponse(html)

def index(request, tvno="0"):
    tv_list = [
        {'name': '足球', 'tvcode': 'id_XNDMzODE5MTE0MA'},
        {'name': '最美的安排', 'tvcode': 'id_XNDMzNTkxNDMxNg'},
    ]

    template = get_template('index.html')
    now = datetime.now()
    hours = now.timetuple().tm_hour
    tvno = int(tvno)
    tv = tv_list[tvno]

    html = template.render(locals())
    return HttpResponse(html)


def engtv(request, tvno='0'):
    tv_list = [
        {'name': '足球', 'tvcode': 'id_XNDMzODE5MTE0MA'},
        {'name': '最美的安排', 'tvcode': 'id_XNDMzNTkxNDMxNg'},
    ]

    template = get_template('engtv.html')
    now = datetime.now()
    tvno = int(tvno)
    tv = tv_list[tvno]

    html = template.render(locals())
    return HttpResponse(html)


def carlist(request, maker='0'):
    carmaker = ['SAAB', ' Ford', 'Honda', 'Mazda', 'Nissan', 'Toyota']
    car_list = [[],
                ['Fiesta', 'Focus', 'Modeo', ' EcoSport', 'Kuga', 'Mustang'],
                ['Fit', 'Odyssey', 'CR-V', 'City', 'NSX'],
                ['Mazda3', 'Mazda5', 'Mazda6', 'CX-3', 'CX-5', 'MX-5'],
                ['Tida', 'March', 'Livina', 'Sentra', 'Teana', 'X-Trail', ' Juke', ' Murano'],
                ['Camry', 'Altis', 'Yaris', '86', 'Prius', 'Vios', 'RAV4', 'Wish']
                ]
    maker = int(maker)
    maker_name = carmaker[maker]
    cars = car_list[maker]

    template = get_template('carlist.html')
    html = template.render(locals())

    return  HttpResponse(html)

def carprice(request, maker='0'):
    carmaker = ['Ford', 'Hond', 'Nissan']
    car_list = [
        [{'model': 'Focus', 'price': 360000, 'number': 3},
         {'model': 'Modeo', 'price': 250000, 'number': 2},
         {'model': 'Mustang', 'price': 780000, 'number': 5}
        ],
        [{'model': 'Fit', 'price': 870000, 'number': 4},
         {'model': 'CR-V', 'price': 560000, 'number': 6},
         {'model': 'NSX', 'price': 140000, 'number': 2}
        ],
        [
            {'model': 'Tida', 'price': 320000, 'number': 5},
            {'model': 'Sentra', 'price': 300000, 'number': 6},
            {'model': 'Juke', 'price': 760000, 'number': 2}
        ]
    ]

    maker = int(maker)
    maker_name = carmaker[maker]
    cars = car_list[maker]
    now = datetime.now()

    template = get_template('carprice.html')
    html = template.render(locals())

    return HttpResponse(html)