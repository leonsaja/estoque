# Generated by Django 3.2.6 on 2021-08-25 00:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('produto', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estoque',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('nf', models.PositiveIntegerField(blank=True, null=True, verbose_name='Nota Fiscal')),
                ('movimento', models.CharField(blank=True, choices=[('E', 'Entrada'), ('S', 'Saida')], max_length=1)),
                ('Funcionario', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='EstoqueItens',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.PositiveIntegerField(blank=True, null=True)),
                ('saldo', models.PositiveIntegerField(default=0)),
                ('estoque', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='estoques', to='estoque.estoque')),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produto.produto')),
            ],
        ),
    ]
