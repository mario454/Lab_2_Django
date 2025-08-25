from django.shortcuts import render
from django.http import HttpResponse
from .models import Track

# Create your views here.

def alltracks(request):
    context={}
    context['tracks'] = Track.objects.all()
    return render(request, 'track/list.html', context)

def Insert(request):
    if request.method == 'POST':
        name = request.POST['track']
        Track.objects.create(name=name)
    return render(request, 'track/insert.html')

def Update(request, id):
    return HttpResponse(f"<h1>Track {id} updated</h1>")

def Delete(request, id):
    return HttpResponse(f"<h1>Track {id} deleted</h1>")

