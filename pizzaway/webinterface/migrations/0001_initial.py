# Generated by Django 4.2.6 on 2023-10-28 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('name', models.CharField(max_length=20, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('name', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('ingredients', models.ManyToManyField(to='webinterface.ingredient')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('notes', models.CharField(max_length=300)),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('pizzas', models.ManyToManyField(to='webinterface.pizza')),
            ],
        ),
    ]
