from django.db import models

# Create your models here.

class PizzaType(models.Model):
    pizza_type_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=255)
    def __str__(self):
        return self.name
    
class Pizza(models.Model):
    pizza_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=255)
    price=models.DecimalField(max_digits=11,decimal_places=2)
    pizza_type_id=models.ForeignKey('PizzaType',on_delete=False)
    def __str__(self):
        return self.name
    
class Transactions(models.Model):
    trans_id=models.AutoField(primary_key=True)
    pizza_id=models.ForeignKey('Pizza',on_delete=False)
    pizza_amount=models.IntegerField(default=1)
    price=models.DecimalField(max_digits=11,decimal_places=2)
    def __str__(self):
        return str(self.pizza_id)
    