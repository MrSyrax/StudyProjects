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
    "money": 0
}


def calculate_resources(choice, dictionary_given, resources_available):
    """calculates the resources used and returns the new totals"""
    if choice == 'report':
        print(f"water: {resources_available['water']}ml\nmilk: {resources_available['milk']}ml")
        print(f"coffee: {resources_available['coffee']}g\nmoney: ${resources_available['money']}")
    elif choice == 'espresso':
        coffee = resources_available['coffee']
        dict_coffee = dictionary_given[choice]['ingredients']['coffee']
        water = resources_available['water']
        dict_water = dictionary_given[choice]['ingredients']['water']
        if coffee > dict_coffee and water > dict_water:
            total_water = resources_available['water'] - dictionary_given[choice]['ingredients']['water']
            total_coffee = resources_available['coffee'] - dictionary_given[choice]['ingredients']['coffee']
            total_cost = dictionary_given[choice]['cost']
            return total_water, total_coffee, total_cost
        else:
            print('not enough coffee and water')
    elif choice == 'latte' or choice == 'cappuccino':
        coffee = resources_available['coffee']
        dict_coffee = dictionary_given[choice]['ingredients']['coffee']
        water = resources_available['water']
        dict_water = dictionary_given[choice]['ingredients']['water']
        milk = resources_available['milk']
        dict_milk = dictionary_given[choice]['ingredients']['milk']
        if coffee > dict_coffee and water > dict_water and milk > dict_milk:
            total_water = resources_available['water'] - dictionary_given[choice]['ingredients']['water']
            total_milk = resources_available['milk'] - dictionary_given[choice]['ingredients']['milk']
            total_coffee = resources_available['coffee'] - dictionary_given[choice]['ingredients']['coffee']
            total_cost = dictionary_given[choice]['cost']
            return total_water, total_milk, total_coffee, total_cost
        else:
            return 'not enough coffee and milk and water'
    else:
        print('Powering Off')


COINS = {"penny": 0.01, 'nickle': 0.05, 'dime': 0.10, 'quarter': 0.25}

quarter = COINS['quarter']
dime = COINS['dime']
nickle = COINS['nickle']
penny = COINS['penny']

power = True

while power:
    coffee_choice = input('What would you like? espresso: $1.5, latte: $2.5, cappuccino: $3.0\n').lower()
    calculated_totals = calculate_resources(coffee_choice, MENU, resources)
    if calculated_totals == 'not enough coffee and milk and water':
        print('not enough coffee or milk or water, refill before trying again')
        continue
    if coffee_choice in MENU or coffee_choice == 'report' or coffee_choice == 'off':
        if coffee_choice == 'espresso':
            resources['water'] = calculated_totals[0]
            resources['coffee'] = calculated_totals[1]
            resources['money'] = MENU[coffee_choice]['cost']
            quarter = int(input('how many quarters?: '))
            dime = int(input('how many dimes?: '))
            nickle = int(input('how many nickles?: '))
            penny = int(input('how many pennies?: '))
        elif coffee_choice == 'latte' or coffee_choice == 'cappuccino':
            resources['water'] = calculated_totals[0]
            resources['milk'] = calculated_totals[1]
            resources['coffee'] = calculated_totals[2]
            resources['money'] = MENU[coffee_choice]['cost']
            quarter = int(input('how many quarters?: '))
            dime = int(input('how many dimes?: '))
            nickle = int(input('how many nickles?: '))
            penny = int(input('how many pennies?: '))
        elif coffee_choice == 'off':
            break
    else:
        print('incorrect input please chose from the list')

    coin_list = [COINS['quarter'] * quarter, COINS['dime'] * dime, COINS['nickle'] * nickle]
    total = sum(coin_list)
    if coffee_choice != 'report':
        if total - MENU[coffee_choice]['cost'] >= 0:
            total -= MENU[coffee_choice]['cost']
            print(f'your change: ${round(total, 2)}')
        else:
            print('not enough money')
            resources = resources

