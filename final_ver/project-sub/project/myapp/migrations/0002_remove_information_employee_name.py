# Generated by Django 4.2.5 on 2023-09-13 00:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='information',
            name='employee_name',
        ),
    ]
