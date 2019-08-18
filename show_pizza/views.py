from django.shortcuts import render
from django.http import request,HttpResponse
from pizza.settings import TIME_ZONE
# Create your views here.
from show_pizza.models import PizzaType,Pizza,Transactions
from django.db.models import Sum,Count
def index(request):
    time_zone=TIME_ZONE
    total_sold_amount=Transactions.objects.aggregate(total_sold_amount=Sum('pizza_amount'))
    total_sold_pizzas_count=Transactions.objects.values('pizza_id').distinct().annotate(total_sold_pizzas_count=Count('trans_id'))
    pizzas_sold_amount=Transactions.objects.values('pizza_id').annotate(total_sold_pizzas=Sum('pizza_amount')).order_by('-total_sold_pizzas')
    pizzas=[]
    for index,pizza in enumerate(pizzas_sold_amount):
        pizza.update({'pizza_name':Pizza.objects.filter(pizza_id=pizza['pizza_id']).first().name,
                      'pizza_type':Pizza.objects.filter(pizza_id=pizza['pizza_id']).first().pizza_type_id.name,
                      'price':Pizza.objects.filter(pizza_id=pizza['pizza_id']).first().price})
        pizzas.append(pizza)
    return  render(request,'index.html',{'pizzas':pizzas,'total_sold_amount':total_sold_amount,'time_zone':time_zone})
    
    