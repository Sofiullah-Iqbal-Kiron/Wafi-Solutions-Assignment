# Generated by Django 5.1.1 on 2024-09-12 16:33

import phonenumber_field.modelfields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0003_alter_employee_mobile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='mobile',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=14, region='BD', unique=True),
        ),
    ]
