from django.shortcuts import render

# Create your views here.
def dashboard(request):
    template_name = "back/base.html"
    context = {
        'title':'dashboard',
    }
    return render(request, template_name, context)