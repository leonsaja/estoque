# Generated by Django 3.2.6 on 2021-10-21 19:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('estoque', '0006_estoqueentrada_estoquesaida'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estoqueitens',
            name='estoque',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='estoques', to='estoque.estoque'),
        ),
    ]