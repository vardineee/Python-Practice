from menu_data import MENU, resources

water = resources['water']
milk = resources["milk"]
coffee = resources["coffee"]
coffee_machine_money = 0



def report():
    return f"Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}g\nMoney: ${coffee_machine_money}"


def check_resources(user_ingredients):
    for item in user_ingredients:
        if user_ingredients[item] > resources[item]:
            print(f"Sorry, there is not enough {item}")
            return False
        else:
            return True


def process_coins():
    total = 0
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.1
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total


def check_transaction(money_received, drink_cost):
    if money_received >= drink_cost:
        change = round(money_received-drink_cost, 2)
        print(f"Here is ${change} in change.")
        global coffee_machine_money
        coffee_machine_money += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):

    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}  Enjoy!")


turn_off = False
while not turn_off:

    user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_input == "off":
        turn_off = True
    elif user_input == "report":
        print(report())
    else:
        user_choice = MENU[user_input]
        if check_resources(user_choice["ingredients"]):
            payment = process_coins()
            if check_transaction(payment, user_choice['cost']):
                make_coffee(user_input, user_choice["ingredients"])





