# Generated by Django 3.2.7 on 2021-10-06 17:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0014_rename_a_product_id_addtocart_a_product'),
    ]

    operations = [
        migrations.RenameField(
            model_name='addtocart',
            old_name='a_product',
            new_name='aproduct',
        ),
        migrations.RenameField(
            model_name='addtocart',
            old_name='a_user',
            new_name='auser',
        ),
    ]