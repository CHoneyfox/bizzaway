# Generated by Django 4.2.6 on 2023-10-29 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webinterface', '0004_alter_pizza_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='pizza',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]
