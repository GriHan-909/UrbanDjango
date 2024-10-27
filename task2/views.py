from django.shortcuts import render
from django.views.generic import TemplateView

def func_template(request):
    return render(request, 'func_template.html')

class ViewClassTemplate(TemplateView):
    template_name = 'class_template.html'