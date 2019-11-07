#practiceapp/forms.py

from django import forms
from .models import SuperHero


class SuperheroForm(forms.ModelForm):

    class Meta:
        model=SuperHero
        fields=('superhero_name','photo_url','real_name','place_of_birth','superpowers','occupation','group_affiliation','relatives','first_appear','publisher',)



  