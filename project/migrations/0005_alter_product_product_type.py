# Generated by Django 5.0 on 2023-12-07 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0004_alter_product_product_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_type',
            field=models.CharField(choices=[('national', 'nacional'), ('imported', 'importado')], max_length=10),
        ),
    ]
