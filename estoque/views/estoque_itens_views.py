from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from django.shortcuts import redirect
from estoque.forms.estoque_form.estoque_form import EstoqueForm
from estoque.forms.estoque_itens_form.estoque_itens_form import EstoqueItensForm, Estoque_itens_formset
from estoque.models import EstoqueItens, Estoque
from produto.models import Produto


def dar_entrada_estoque(form):
    produtos = list(form)

    for item in produtos:
        produto = Produto.objects.get(pk=item.produto.id)
        produto.estoque += item.quantidade
        produto.save()


def add_entrada_estoque(request):
    estoque_form = Estoque()
    if request.method == 'POST':
        formset = Estoque_itens_formset(
            request.POST or None, instance=estoque_form, prefix='estoque')
        form = EstoqueForm(request.POST or None,
                           instance=estoque_form, prefix='main')
        if formset.is_valid() and form.is_valid():
            form = form.save(commit=False)
            form.funcionario = request.user
            form.movimento = 'E'
            form.save()
            formset = formset.save()
            dar_entrada_estoque(formset)
            return redirect('estoque:estoque_entrada_list')
    else:
        formset = Estoque_itens_formset(
            instance=estoque_form, prefix='estoque')
        form = EstoqueForm(instance=estoque_form, prefix='main')
    return render(request, 'estoque_itens/estoque_entrada_form.html', {'form': form, 'formset': formset})


def dar_baixa_estoque(form):

    produtos = form.estoques.all()

    for item in produtos:
        produto = Produto.objects.get(pk=item.produto.id)
        produto.estoque -= item.quantidade
        produto.save()


@login_required
def dar_saida_estoque(request):
    estoque_form = Estoque()
    if request.method == 'POST':
        formset = Estoque_itens_formset(
            request.POST or None, instance=estoque_form, prefix='estoque')
        form = EstoqueForm(request.POST or None,
                           instance=estoque_form, prefix='main')
        if formset.is_valid() and form.is_valid():
            form = form.save(commit=False)
            print('user', request.user)
            form.funcionario = request.user
            form.movimento = 'S'
            form.save()
            formset = formset.save()
            dar_baixa_estoque(form)
            return redirect('estoque:estoque_saida_list')
    else:
        formset = Estoque_itens_formset(
            instance=estoque_form, prefix='estoque')
        form = EstoqueForm(instance=estoque_form, prefix='main')
    return render(request, 'estoque_itens/estoque_saida_form.html', {'form': form, 'formset': formset})
