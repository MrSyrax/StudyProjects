from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

cash_machine = MoneyMachine()
coffee_machine = CoffeeMaker()
choices = Menu()
drinks = choices.get_items()
more_coffe = True
profit  = cash_machine.report()

print(profit)

# while  more_coffe:
#     user_choice = input(f'what drink would you like? {drinks}: ')
#     drink_chosen = choices.find_drink(user_choice)
#     resources_sufficient = coffee_machine.is_resource_sufficient(drink_chosen)


#     if resources_sufficient:
#       coffee_machine.make_coffee(drink_chosen)


#     ask_again = input('would you like more coffee?: y or n ')
#     if ask_again == 'n':
#         print("thank you enjoy your {user_choice}")
#         more_coffe = False
    
    

#how to put it all together.

