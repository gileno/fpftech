# Generated by Django 2.0.2 on 2018-02-22 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_product_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='active',
            field=models.BooleanField(default=True, verbose_name='Ativo'),
        ),
    ]
