from decimal import Decimal

from django.shortcuts import redirect
from django.http import HttpResponse
import logfire

from .models import FishSauce


def show_fish(request):
    sauces = FishSauce.objects.all()
    names = ', '.join(f'name={sauce.name} price={sauce.price}' for sauce in sauces)
    return HttpResponse(f'all the fish: {names}')


def add_fish(request):
    name = request.GET.get('name', '')
    price = Decimal(request.GET.get('price', '123'))
    logfire.info('add_fish view {name=} {price=}', name=name, price=price)
    FishSauce.objects.create(name=name, price=price)
    return redirect('index')
