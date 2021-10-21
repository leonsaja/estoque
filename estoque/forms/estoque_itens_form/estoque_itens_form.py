from django import forms
from django.forms import inlineformset_factory
from estoque.models import Estoque, EstoqueItens


class EstoqueItensForm(forms.ModelForm):

    class Meta:
        model = EstoqueItens
        fields = '__all__'

    # def clean_quantidade(self):
    #     qta_entrada = self.cleaned_data['quantidade']
    #     QuantEstoque = EstoqueItens.objects.all()
    #     for i in QuantEstoque:
    #         print('teste', i.quantidade)


Estoque_itens_formset = inlineformset_factory(
    Estoque, EstoqueItens, form=EstoqueItensForm, extra=1)
