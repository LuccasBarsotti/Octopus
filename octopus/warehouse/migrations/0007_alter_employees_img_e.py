# Generated by Django 4.1.3 on 2022-12-03 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse', '0006_alter_products_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employees',
            name='img_e',
            field=models.ImageField(upload_to='static/'),
        ),
    ]
