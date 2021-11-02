from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from django.shortcuts import redirect
from estoque.forms.estoque_form import EstoqueForm
from estoque.forms.estoque_itens_form import EstoqueItensForm, Itens_estoque_formset
from estoque.models import EstoqueItens, Estoque
from produto.models import Produto
from django.forms import inlineformset_factory


def dar_baixa_estoque(form):
    
    produtos = form.estoques.all()
    for item in produtos:
        produto = Produto.objects.get(pk=item.produto.id)
        produto.estoque = item.saldo
        produto.save()

def movimento_estoque(request,movimento):
    estoque_form = Estoque()
    if request.method == 'POST':
        formset = Itens_estoque_formset(request.POST, instance=estoque_form, prefix='estoque')
        form = EstoqueForm(request.POST, instance=estoque_form, prefix='form')
        if formset.is_valid() and form.is_valid():
            form = form.save(commit=False)
            form.funcionario = request.user
            form.movimento = movimento
            form.save()
            formset = formset.save()
            dar_baixa_estoque(form)
            return {'pk':form.pk}
    else:
        formset = Itens_estoque_formset(instance=estoque_form, prefix='estoque')
        form = EstoqueForm(instance=estoque_form, prefix='form')
    context={'form':form,'formset':formset}
    return context


@login_required
def add_entrada_estoque(request):
  #form_inline=EstoqueItens()
  template_name='estoque_itens/estoque_entrada_form.html'
  movimento='E'
  context=movimento_estoque(request, movimento)
  print(context)
  if context.get('pk'):
      return redirect('estoque:estoque_list')
  return render(request, template_name,context)

@login_required
def add_saida_estoque(request):
  template_name = 'estoque_itens/estoque_saida_form.html'
  movimento='S'
  context=movimento_estoque(request, movimento)
  print(context)
  if context.get('pk'):
      return redirect('estoque:estoque_list')
  return render(request, template_name,context)
