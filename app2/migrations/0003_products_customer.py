# Generated by Django 4.1.5 on 2023-01-10 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app2', '0002_products_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='customer',
            field=models.ManyToManyField(to='app2.customer'),
        ),
    ]
