# Generated by Django 3.2.7 on 2021-10-06 17:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0013_addtocart_quantity'),
    ]

    operations = [
        migrations.RenameField(
            model_name='addtocart',
            old_name='a_product_id',
            new_name='a_product',
        ),
    ]