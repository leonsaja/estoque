# Generated by Django 3.2.6 on 2021-08-28 23:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('estoque', '0008_alter_estoqueitens_estoque'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estoqueitens',
            name='estoque',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estoque.estoque'),
        ),
    ]