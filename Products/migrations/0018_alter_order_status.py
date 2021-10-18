# Generated by Django 3.2.7 on 2021-10-11 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0017_auto_20211007_1100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Completed', 'Completed'), ('Ordered', 'Ordered'), ('Accepted', 'Accepted'), ('Out for Delivery', 'Out for Delivery'), ('Order Cancel', 'Order Cancel'), ('Customer Cancel', 'Customer Cancel'), ('Delivered', 'Delivered'), ('Added to Cart', 'Added to Cart'), ('Assigned to Driver', 'Assigned to Driver')], default='ordered', max_length=50, null=True),
        ),
    ]