# Generated by Django 4.1.3 on 2022-12-01 18:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse', '0003_employees_img_e'),
    ]

    operations = [
        migrations.AddField(
            model_name='employees',
            name='bar_code',
            field=models.CharField(default=django.utils.timezone.now, max_length=255),
            preserve_default=False,
        ),
    ]
