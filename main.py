from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# 1. Print report
# 2. Check resources sufficient
# 3. Process coins
# 4. Check transaction is successful
# 5. Make coffee

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

# quick function to print report
def reporttt():
     coffee_maker.report(), money_machine.report()


is_on = True
while is_on:

    choice = input(f"What would you like to have? {menu.get_items()}: ")

    if choice == "off":
        is_on = False
    elif choice == "report":
        reporttt()
    else:
        order = menu.find_drink(choice)
        res = coffee_maker.is_resource_sufficient(order)

        if res:
            drink_cost = order.cost
            print(drink_cost)
            if money_machine.make_payment(drink_cost):
                coffee_maker.make_coffee(order)

