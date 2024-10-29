from django.shortcuts import render

def func_brand(request):
    title = 'Марки автомобилей'
    list_mark = ['BMW', 'CHANGAN', 'MERSEDES', 'AUDI', 'VOLVO', 'ZEEKR', 'LOTUS']
    context = {
        'title': title,
        'list_mark': list_mark
    }

    return render(request, 'third_task/brand.html', context)

def func_dealership(request):
    title = 'Список автосалонов'
    dealerships = ['BMW','CHANGAN','MERSEDES']
    context = {
        'title': title,
        'dealerships':dealerships
    }

    return render(request, 'third_task/car_dealership.html', context)
