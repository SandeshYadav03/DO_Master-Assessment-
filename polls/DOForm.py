from django import forms 
from .models import *

class DO_Form(forms.ModelForm):
    class Meta:
        model=DO_Master
        fields='__all__'