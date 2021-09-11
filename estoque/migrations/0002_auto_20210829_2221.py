# Generated by Django 3.2.6 on 2021-08-30 01:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('estoque', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estoque',
            name='nf',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Nota Fiscal'),
        ),
        migrations.AlterField(
            model_name='estoqueitens',
            name='estoque',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='estoques', to='estoque.estoque'),
        ),
        migrations.AlterField(
            model_name='estoqueitens',
            name='quantidade',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
