# Generated by Django 3.2.6 on 2021-09-21 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0007_delete_user_model'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
