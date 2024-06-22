MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def check_resource_availability(coffee_type):
    if resources['water'] < MENU[coffee_type]['ingredients']['water']:
        print("Sorry there is not enough water.")
        return 0
    if resources['coffee'] < MENU[coffee_type]['ingredients']['coffee']:
        print("Sorry there is not enough coffee.")
        return 0
    if 'milk' in MENU[coffee_type]['ingredients'] and resources['milk'] < MENU[coffee_type]['ingredients']['milk']:
        print("Sorry there is not enough milk.")
        return 0
    return 1

def process_coins(quarter, dimes, nickle, pennies):
    return 0.25 * quarter + 0.10 * dimes + 0.05 * nickle + 0.01 * pennies

def make_coffee(coffee_type, total_earnings):
    resources['water'] = resources['water'] - MENU[coffee_type]['ingredients']['water']
    resources['coffee'] = resources['coffee'] - MENU[coffee_type]['ingredients']['coffee']
    if 'milk' in MENU[coffee_type]['ingredients']:
        resources['milk'] = resources['milk'] - MENU[coffee_type]['ingredients']['milk']
    
    total_earnings += MENU[coffee_type]['cost']
    return {
        "resources": resources, 
        "total_earnings": total_earnings
    }

def generate_report():
    print(f"Water: {resources['water']}")
    print(f"Milk: {resources['milk']}")
    print(f"Coffee: {resources['coffee']}")
    print(f"Money: ${total_earnings}")

total_earnings = 0.00

while True:
    coffee_type = input("What would you like? (espresso/latte/cappuccino): ")
    if coffee_type == 'off':
        exit()
    
    if coffee_type == 'report':
        generate_report()
        continue

    is_resource_available = check_resource_availability(coffee_type)

    if not is_resource_available:
        continue
    else:
        print("Please insert the coins.")
        quarter = float(input("How many quarters?: "))
        dimes = float(input("How many dimes?: "))       
        nickle = float(input("How many nickles?: "))       
        pennies = float(input("How many pennies?: "))       

        total_money = process_coins(quarter, dimes, nickle, pennies)
        if MENU[coffee_type]['cost'] > total_money:
            print("Sorry that's not enough money. Money refunded.")
            continue
        elif MENU[coffee_type]['cost'] < total_money:
            print(f"Here is ${round(total_money - MENU[coffee_type]['cost'], 2)} in change")
            total_earnings = make_coffee(coffee_type, total_earnings)['total_earnings']
            print(f"Here is your {coffee_type} ☕ Enjoy!")
