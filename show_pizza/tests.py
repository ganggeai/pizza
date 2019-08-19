import unittest
from show_pizza.models import Pizza,PizzaType,Transactions
import os
import django
import random

# Create your tests here.

class TestPizza(unittest.TestCase):
    def testInsertPizza(self):
        pizza_types=[1,2,3]
        make_methods=['raw','fried']
        main_reciepts=['beef','chiken','pork']
        condiments=['peper','ketchup','butter']
        random_pizza_name=random.choice(make_methods)+' '\
            +random.choice(main_reciepts)+' '\
            +random.choice(condiments)
        random_pizza_type=PizzaType.objects.filter(pizza_type_id=random.choice(pizza_types)).first()
        random_price=random.randrange(10.00,100.00)
        try:
            new_pizza=Pizza()
            new_pizza.name=random_pizza_name
            new_pizza.pizza_type_id=random_pizza_type
            new_pizza.price=random_price
            new_pizza.save()
            print('insert random pizza data one row.')
        except models.Expression as err:
            print(err.args)
    def testAccesstoWeb(self):
        import requests
        res=requests.get('http://127.0.0.1:8000')
        assert res.status_code==200
if __name__=='__main__':
    unittest.main()

        
