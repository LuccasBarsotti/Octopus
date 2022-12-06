# Generated by Django 4.1.3 on 2022-12-01 18:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='img',
            field=models.CharField(default=django.utils.timezone.now, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='products',
            name='qtt',
            field=models.IntegerField(default=0),
        ),
    ]
