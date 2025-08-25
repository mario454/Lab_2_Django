from django.shortcuts import render
from django.http import HttpResponse
from .models import Trainee
# Create your views here.

def Alltrainee(request):
    context={}
    context['trainees'] = Trainee.objects.all()
    return render(request, 'trainee/list.html', context)

def Insert(request):
    if request.method == 'POST':
       name = request.POST['trName']
       email = request.POST['trEmail']
       image = request.FILES.get('trImage')
       Trainee.objects.create(name=name, email=email, image=image)
       
    return render(request, 'trainee/insert.html')

def Update(request, id):
    return HttpResponse(f"<h1>Trainee {id} updated</h1>")

def Delete(request, id):
    return HttpResponse(f"<h1>Trainee {id} deleted</h1>")

