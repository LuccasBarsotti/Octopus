# Generated by Django 4.1.3 on 2022-12-03 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse', '0005_products_bar_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='img',
            field=models.ImageField(upload_to='static/'),
        ),
    ]