# Generated by Django 4.1.3 on 2022-12-03 00:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse', '0004_employees_bar_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='bar_code',
            field=models.CharField(default=django.utils.timezone.now, max_length=255),
            preserve_default=False,
        ),
    ]
