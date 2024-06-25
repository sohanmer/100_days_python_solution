from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

while True:
    coffee_type = input(f"What would you like? {menu.get_items()}: ")
    if coffee_type == 'off':
        exit()
    elif coffee_type == 'report':
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(coffee_type)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
