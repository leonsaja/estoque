from django import forms
from django.forms import inlineformset_factory
from estoque.models import Estoque, EstoqueItens,Produto
from django.core.exceptions import ValidationError
class EstoqueItensForm(forms.ModelForm):
    quantidade=forms
    class Meta:
        model = EstoqueItens
        fields = '__all__'
        
    
    
    
Itens_estoque_formset = inlineformset_factory( Estoque, EstoqueItens, form=EstoqueItensForm, extra=0, min_num=1, can_delete=False)
