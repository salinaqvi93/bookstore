from django.shortcuts import render
from django.views.generic import TemplateView

from.models import Book


def index(request):
    return render(request, 'template.html')

def store(request):
    count = Book.objects.all().count()
    context = {
        'count': count
    }
    request.session['location'] = "unknown"
    if request.user.is_authenticated:
        request.session['location'] = "Earth"
    else :
        print('user is false')
    print('redirecting...')
    return render(request, 'store.html', context)

class RegistrationCompleteView(TemplateView):
    template_name = "registration_complete.html"