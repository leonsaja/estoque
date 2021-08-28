import datetime
from django.contrib.auth.models import User
from django.db import models
from core.models import DataCriacao
from produto.models import Produto

class Estoque(DataCriacao):

    CHOICES_MOVIMENTO = (
        ('E', 'Entrada'),
        ('S', 'Saida'),
    )

    Funcionario=models.ForeignKey(User,on_delete=models.CASCADE, blank=True)
    nf = models.PositiveIntegerField('Nota Fiscal',blank=True,null=True)
    movimento=models.CharField(max_length=1,choices=CHOICES_MOVIMENTO,blank=True)


    class Meta:
        verbose_name_plural = "Estoques"
        verbose_name = "Estoque"

    def __str__(self):
        return '{} - {} - {}'.format(self.pk, self.nf, self.created.strftime('%d-%m-%Y'))

class EstoqueItens(models.Model):

    estoque = models.ForeignKey(Estoque, on_delete=models.CASCADE,related_name='estoque')
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField(blank=True, null=True)
    saldo=models.PositiveIntegerField(default=0)

    class meta:
        ordering = ('pk',)

    def __str__(self):
        return '{} - {} - {}'.format(self.pk,self.estoque.pk, self.produto)