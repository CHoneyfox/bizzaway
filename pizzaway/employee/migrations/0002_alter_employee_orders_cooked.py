# Generated by Django 4.2.6 on 2023-10-16 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='orders_cooked',
            field=models.IntegerField(default=0),
        ),
    ]
