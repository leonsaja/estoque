from django.db import models


class Produto(models.Model):

    importado = models.BooleanField(default=False)
    ncm = models.CharField('NCM', max_length=8,blank=False,null=False)
    produto = models.CharField(max_length=100, unique=True)
    preco = models.DecimalField('Preço', max_digits=7, decimal_places=2)
    estoque = models.IntegerField('Estoque atual')
    estoque_minimo = models.PositiveIntegerField('Estoque mínimo', default=0)
    data = models.DateField(null=True, blank=True)
    categoria = models.ForeignKey(
        'Categoria',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    class Meta:
        ordering = ('produto',)
    
    def total(self):
        soma=self.preco*self.estoque
        
        return soma
    def to_dict_json(self):
        return{
            'id':self.id,
            'produto': self.produto,
            'estoque':self.estoque,

        }

    def __str__(self):
        return self.produto




class Categoria(models.Model):
    categoria = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ('categoria',)

    def __str__(self):
        return self.categoria