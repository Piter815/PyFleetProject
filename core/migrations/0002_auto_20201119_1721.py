# Generated by Django 3.1.3 on 2020-11-19 16:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='billing_address',
            new_name='address',
        ),
    ]
