# Generated by Django 4.2.6 on 2023-11-04 12:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webinterface', '0008_rename_pizza_pizzaorder_pizzas'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pizzaorder',
            name='pizzas',
        ),
        migrations.AddField(
            model_name='pizzaorder',
            name='pizza',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='order', to='webinterface.pizza'),
            preserve_default=False,
        ),
    ]