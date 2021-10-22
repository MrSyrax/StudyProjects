from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

cash_machine = MoneyMachine()
coffee_machine = CoffeeMaker()
choices = Menu()
drinks = choices.get_items()
more_coffe = True
profit  = cash_machine.profit

while  more_coffe:
    user_choice = input(f'what drink would you like? {drinks}: ')
<<<<<<< HEAD
    if user_choice == 'off':
        more_coffe = False
        break
    elif user_choice == 'report':
=======
   
    if user_choice == 'report':
>>>>>>> 7cba774d7b86f6fb2bdd98cdd02405ff775d93d1
      print(cash_machine.report())
      print(coffee_machine.report())
    else:
       drink_chosen = choices.find_drink(user_choice)
       resources_sufficient = coffee_machine.is_resource_sufficient(drink_chosen)
       paid = cash_machine.make_payment(drink_chosen.cost)
<<<<<<< HEAD

    if resources_sufficient and paid:
      coffee_machine.make_coffee(drink_chosen)

    ask_again = input('would you like more coffee?: y or n ')
    if ask_again == 'n':
        print("thank you enjoy your {user_choice}")
        more_coffe = False
=======

    if resources_sufficient and paid:
      coffee_machine.make_coffee(drink_chosen)

    ask_again = input('would you like more coffee?: y or n ')
    if ask_again == 'n':
        print("thank you enjoy your {user_choice}")
        more_coffe = False
    
    

#how to put it all together.

>>>>>>> 7cba774d7b86f6fb2bdd98cdd02405ff775d93d1
