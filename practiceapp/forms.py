#practiceapp/forms.py

from django import forms
from .models import Superhero

class SuperheroForm(forms.ModelForm):

    class Meta:
        model=Superhero
        fields=('superhero_name','photo_url','real_name','place_of_birth','superpowers','occupation','group_affiliation','relatives','first_appear','publisher',)



      