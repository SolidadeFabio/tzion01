# Generated by Django 5.0 on 2023-12-07 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0005_alter_product_product_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='cas_number',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='purch_cod',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='product',
            name='sell_cod',
            field=models.CharField(max_length=50),
        ),
    ]
