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


def print_report():
    print(f"Water: {resources['water']}mL")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money}")


def check_levels(order):
    ingredients = ["water", "milk", "coffee"]
    for ingredient in ingredients:
        if ingredient in MENU[order]["ingredients"]:
            if MENU[order]["ingredients"][ingredient] > resources[ingredient]:
                print(f"Sorry, the machine is out of {ingredient}")
                return False
    return True


def take_order():
    ordering = True
    while ordering:
        order = input("What would you like to order, an espresso, a latte or a cappuccino? ")
        if order == "report":
            print_report()
        elif order == "off":
            ordering = False
            return False
        elif order in MENU:
            if check_levels(order) == True:
                ordering = False
                return order
        else:
            print("I'm sorry I don't understand")


def payment(order):
    print(f"The cost is ${MENU[order]['cost']}.  Please insert coins.")
    quarters = float(input("Number of quarters: "))
    dimes = float(input("Number of dimes: "))
    nickels = float(input("Number of nickels: "))
    pennies = float(input("Number of pennies: "))
    total = quarters * 0.25 + dimes * 0.1 + nickels * 0.5 + pennies * 0.1
    return total

def update_resources():
    ingredients = ["water", "milk", "coffee"]
    for ingredient in ingredients:
        if ingredient in MENU[order]["ingredients"]:
            resources[ingredient] -= MENU[order]["ingredients"][ingredient]

money = 0

machine_on = True
while machine_on:
    order = take_order()
    if order == False:
        machine_on = False
    else:
        total = payment(order)
        print(type(total))
        if total < MENU[order]['cost']:
            print("Insufficient funds. Your money is returned.")
        else:
            change = total - MENU[order]['cost']
            print(f"Your change is ${change}")
            update_resources()
            money += MENU[order]['cost']
