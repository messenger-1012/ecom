# Generated by Django 3.2.7 on 2021-10-07 05:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0016_dbwishlist'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dbwishlist',
            old_name='aproduct',
            new_name='wproduct',
        ),
        migrations.RenameField(
            model_name='dbwishlist',
            old_name='auser',
            new_name='wuser',
        ),
    ]