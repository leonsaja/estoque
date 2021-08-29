from django.shortcuts import redirect
from django.views.generic import  CreateView
from estoque.forms.estoque_itens_form.estoque_itens_form import EstoqueItensForm,Estoque_itens_formset
from estoque.models import EstoqueItens



class AddEntradaEstoqueView(CreateView):
    form_class = EstoqueItensForm
    template_name = 'estoque_itens/estoque_entrada_form.html'

    def get_context_data(self, **kwargs):
        context=super(AddEntradaEstoqueView, self).get_context_data(**kwargs)

        if self.request.POST:
            context['form']= EstoqueItensForm(self.request.POST or None)
            context['formset']= Estoque_itens_formset(self.request.POST or None)
        else:
            context['form'] = EstoqueItensForm()
            context['formset'] = Estoque_itens_formset()

        return context

    def form_valid(self, form):

        context=self.get_context_data()
        form=context['form']
        form_formset=context['formset']

        if form.is_valid() and form_formset.is_valid():

            self.object=form.save()
            form.instance = self.object
            form_formset.instance = self.object
            form.save()
            form_formset.save()

            return redirect('estoque:estoque_entrada_list')
        else:
            return self.render_to_response(self.get_context_data(form=form))