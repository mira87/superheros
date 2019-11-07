#practiceapp/forms.py

from django import forms
from .models import SuperHero
from crispy_forms.helper import FormHelper


class SuperheroForm(forms.ModelForm):

    class Meta:
        model=SuperHero
        fields=('superhero_name','photo_url','real_name','place_of_birth','superpowers','occupation','group_affiliation','relatives','first_appear','publisher',)



    __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save hero'))