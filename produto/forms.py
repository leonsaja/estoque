from django import forms
from produto.models import Produto

class CadastrarProdutoForm(forms.ModelForm):

    class Meta:
        model = Produto
        fields = '__all__'



