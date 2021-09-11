from django.contrib import admin
from .models import EstoqueEntrada,EstoqueSaida, EstoqueItens

class EstoqueItensInlene(admin.TabularInline):
    model=EstoqueItens
    extra=0

@admin.register(EstoqueEntrada)
class EstoqueEntradaAdmin(admin.ModelAdmin):
    inlines= (EstoqueItensInlene,)
    list_display= ('__str__','nf','funcionario',)
    search_fields=('nf',)
    list_filter=('funcionario',)
   
    
@admin.register(EstoqueSaida)
class EstoqueSaidaAdmin(admin.ModelAdmin):
    inlines= (EstoqueItensInlene,)
    list_display= ('__str__','nf','funcionario',)
    search_fields=('nf',)
    list_filter=('funcionario',)
  
