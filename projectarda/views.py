from django.shortcuts import render #untuk memanggil file html
from django.http import HttpResponse #format html langsung di tulis didalam HttpResponse


def index(request):
    template_name = 'index.html'
    context = {
        'title':'halaman awal',
    }
    return render(request, template_name, context)