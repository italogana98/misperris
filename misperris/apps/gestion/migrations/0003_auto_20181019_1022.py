# Generated by Django 2.1.2 on 2018-10-19 13:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0002_auto_20181019_1019'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuarios',
            old_name='tlefono',
            new_name='telefono',
        ),
    ]