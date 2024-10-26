from django.shortcuts import render

def func_brand(request):
    title = 'Марки автомобилей'
    list_mark = ['BMW', 'CHANGAN', 'MERSEDES', 'AUDI', 'VOLVO', 'ZEEKR', 'LOTUS']
    context = {
        'title': title
    }
    for key, item in enumerate(list_mark):
        context[str(key)+'m']=item

    return render(request, 'brand.html', context)

def func_dealership(request):
    title = 'Список автосалонов'
    dealerships = ['BMW','CHANGAN','MERSEDES']
    context = {
        'title': title
    }
    for key, item in enumerate(dealerships):
        context[str(key)+'s']=item

    return render(request, 'car_dealership.html', context)
