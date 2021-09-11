from datetime import  datetime
from django.contrib.auth.models import User
from django.db import models
from core.models import DataCriacao
from produto.models import Produto

class Estoque(DataCriacao):

    CHOICES_MOVIMENTO = (
        ('E', 'Entrada'),
        ('S', 'Saida'),
    )

    funcionario=models.ForeignKey(User,on_delete=models.CASCADE, blank=True)
    nf = models.PositiveIntegerField('Nota Fiscal',blank=True,null=True)
    movimento=models.CharField(max_length=1,choices=CHOICES_MOVIMENTO,blank=True)


    class Meta:
        verbose_name_plural = "Estoques"
        verbose_name = "Estoque"

    def __str__(self):
        data=self.created.strftime('%d-%m-%Y')
        return '{} - {} - {}'.format(self.pk, self.nf, data)
    
class EstoqueEntradaManager(models.Manager):
    def get_queryset(self):
        return super(EstoqueEntradaManager, self).get_queryset().filter(movimento='E')
    
class EstoqueEntrada(Estoque):
    objects= EstoqueEntradaManager()
    
    class Meta:
        proxy=True
        verbose_name_plural = 'estoque entrada'
        verbose_name = 'estoque entrada'

class EstoqueSaidaManager(models.Manager):
    def get_queryset(self):
        return super(EstoqueSaidaManager, self).get_queryset().filter(movimento='S')

class EstoqueSaida(Estoque):
    
    objects= EstoqueSaidaManager()
    class Meta:
        proxy=True
        verbose_name_plural = 'estoque saida'
        verbose_name = 'estoque saida'

    
class EstoqueItens(models.Model):

    estoque = models.ForeignKey(Estoque, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField(blank=True, null=True)
    saldo=models.PositiveIntegerField(default=0)

    class meta:
        ordering = ('pk',)

    def __str__(self):
        return '{} - {} - {}'.format(self.pk,self.estoque.pk, self.produto)



