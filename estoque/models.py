from datetime import datetime
from django.contrib.auth.models import User
from django.db import models
from core.models import DataCriacao
from produto.models import Produto
from estoque.managers import EstoqueEntradaManager, EstoqueSaidaManager


class Estoque(DataCriacao):

    CHOICES_MOVIMENTO = (
        ('E', 'Entrada'),
        ('S', 'Saida'),
    )

    funcionario = models.ForeignKey(User, on_delete=models.CASCADE, blank=False)
    nf = models.PositiveIntegerField('Nota Fiscal', blank=True, null=True)
    movimento = models.CharField(
        max_length=1, choices=CHOICES_MOVIMENTO, blank=False)

    class Meta:
        verbose_name_plural = "Estoques"
        verbose_name = "Estoque"

    def __str__(self):
        data = self.created.strftime('%d-%m-%Y')
        return '{} - {} - {}'.format(self.pk, self.nf, data)


class EstoqueEntrada(Estoque):
    objects = EstoqueEntradaManager()

    class Meta:
        proxy = True
        verbose_name_plural = 'estoque entrada'
        verbose_name = 'estoque entrada'


class EstoqueSaida(Estoque):

    objects = EstoqueSaidaManager()

    class Meta:
        proxy = True
        verbose_name_plural = 'estoque saida'
        verbose_name = 'estoque saida'


class EstoqueItens(models.Model):

    estoque = models.ForeignKey(Estoque, on_delete=models.CASCADE, related_name='estoques')
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE, null=False,blank=False)
    quantidade = models.PositiveIntegerField(blank=False, null=False)
    saldo = models.PositiveIntegerField(blank=False)

    class meta:
        ordering = ('pk',)

    def __str__(self):
        return '{} - {} - {}'.format(self.pk, self.estoque.pk, self.produto)
