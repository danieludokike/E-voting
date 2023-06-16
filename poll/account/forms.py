from django import forms

from pollapp.models import Candidate


class PositionSelectForm(forms.ModelForm):
    
    class Meta:
        model = Candidate
        fields = ("position",)