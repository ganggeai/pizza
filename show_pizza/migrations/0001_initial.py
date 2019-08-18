# Generated by Django 2.2.4 on 2019-08-18 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('pizza_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=11)),
            ],
        ),
        migrations.CreateModel(
            name='PizzaType',
            fields=[
                ('pizza_type_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Transactions',
            fields=[
                ('trans_id', models.AutoField(primary_key=True, serialize=False)),
                ('price', models.DecimalField(decimal_places=2, max_digits=11)),
                ('pizza_id', models.ForeignKey(on_delete=False, to='show_pizza.Pizza')),
            ],
        ),
        migrations.AddField(
            model_name='pizza',
            name='pizza_type_id',
            field=models.ForeignKey(on_delete=False, to='show_pizza.PizzaType'),
        ),
    ]
