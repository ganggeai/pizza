from django.contrib import admin

# Register your models here.
from show_pizza import models
admin.site.register(models.PizzaType)
admin.site.register(models.Pizza)
admin.site.register(models.Transactions)
