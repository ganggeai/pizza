# Generated by Django 2.2.4 on 2019-08-18 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('show_pizza', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='transactions',
            name='pizza_amount',
            field=models.IntegerField(default=1),
        ),
    ]