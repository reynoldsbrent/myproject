from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    context = {
        'name': 'Brent',
        'age': 20,
        'nationality': 'American',
    }
    return render(request, 'index.html', context)
