# Generated by Django 3.2.6 on 2021-11-02 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estoque', '0010_auto_20211024_1701'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estoqueitens',
            name='quantidade',
            field=models.PositiveIntegerField(default=3),
            preserve_default=False,
        ),
    ]
