from django.shortcuts import render

def func_brand(request):
    title = 'Марки автомобилей'
    context = {
        'title': title,
        'list_mark': ['BMW', 'CHANGAN', 'MERSEDES', 'AUDI', 'VOLVO', 'ZEEKR', 'LOTUS']
    }

    return render(request, 'brand.html', context)

def func_dealership(request):
    title = 'Список автосалонов'
    context = {
        'title': title,
        'dealerships': ['BMW','CHANGAN','MERSEDES']
    }

    return render(request, 'car_dealership.html', context)
