from django.shortcuts import render,redirect

from .models import SuperHero
from .forms import SuperheroForm
# Create your views here.

def superhero_list(request):
    heros=SuperHero.objects.all()
    return render(request, 'practiceapp/superhero_list.html',{'heros':heros})

def superhero_detail(request,pk):
    hero=SuperHero.objects.get(id=pk)
    return render(request, 'practiceapp/superhero_detail.html',{'hero':hero})

def superhero_create(request):
    if request.method=='POST':
        form=SuperheroForm(request.POST)
        if form.is_valid():
            hero=form.save()
            return redirect('superhero_detail', hero.pk)
    else:
        form=SuperheroForm()
    return render(request, 'practiceapp/superhero_form.html',{'form':form})