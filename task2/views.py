from django.shortcuts import render


def func_index(request):
    return render(request, 'index.html')

def func_index2(request):
    return render(request, 'index2.html')