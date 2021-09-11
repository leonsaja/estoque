from django import forms
from estoque.models import Estoque
class EstoqueForm(forms.ModelForm):

    class Meta:
        model=Estoque
        fields = ['nf']

