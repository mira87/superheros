from django.shortcuts import render

from .models import SuperHero
# Create your views here.

def superhero_list(request):
    heros=SuperHero.objects.all()
    return render(request, 'practiceapp/superhero_list.html',{'heros':heros})

def superhero_detail(request,pk):
    hero=SuperHero.objects.get(id=pk)
    return render(request, 'practiceapp/superhero_detail.html',{'hero':hero})