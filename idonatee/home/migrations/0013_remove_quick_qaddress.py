# Generated by Django 4.0.6 on 2023-03-09 09:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_quick'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quick',
            name='qaddress',
        ),
    ]
