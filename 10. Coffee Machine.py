
# VIRTUAL COFFEE MACHINE

"""
COFFEE MACHINE REQUIREMENTS

1. Ask from user for Coffee type by prompting?
   "What would you like to have? (latte/expresso/cappuccino):"
    Once the drink is dispensed this prompt should be shown to serve the next customer.
2. When user enters "report" as input then a report should be generated
   that shows the current resources value:
   e.g: Water = 200ml
        Milk = 100ml
        Coffee = 100g
        Money = Rs. 150
3. If user enters "off" as an input then your program should end execution.
4. Check sufficient resources are available or not.
5. If sufficient resources are available then machine should ask to insert
   coins and calculate total money received.
   [Coffee machine only accepts Rs.5, Rs.10 and Rs.20 coins]
6. Check payment is successful or not
   --If user has entered sufficient money,
     the cost of drink gets added to the coffee machine as profit.
   --If user has entered too much money,
      machine should offer change to the user.
   --If money is not sufficient to purchase the drink user has selected,
     it should print a message "Sorry! Thats not enough money"
7. Make Coffee
   If payment is successful, ingredients to make selected drink should be deducted from
   the coffee machine resources.
   And it will print the message
   "Here is your latte" - (If latte was ordered)
"""

# Requirements of each coffee type
menu = {
    "latte": {
        "ingredients": {"water": 250, "milk": 150, "coffee": 24},
        "cost": 150
    },
    "expresso": {
        "ingredients": {"water": 50, "coffee": 18},
        "cost": 100
    },
    "cappuccino": {
        "ingredients": {"water": 250, "milk": 100, "coffee": 20},
        "cost": 200
    }
}

# currently available resources
resources = {
    "water": 500,
    "milk": 500,
    "coffee": 100
}

profit = 0


# Function to check if resources ar available for an ordered item
def check_resources(order_ingredient):
    for item in order_ingredient:
        if order_ingredient[item] > resources[item]:
            print(f"Sorry! There is not enough {item}")
            return False
    return True


# Function to calculate total cost of order
def process_coins():
    print("Please insert coins")
    total = 0
    coins_five = int(input("How many 5rs coins: "))
    coins_ten = int(input("How many 10rs coins: "))
    coins_twenty = int(input("How many 20rs coins: "))

    total = coins_five * 5 + coins_ten * 10 + coins_twenty * 20
    return total


# Function to check if payment i successful or not
def is_payment_successful(money_received, coffee_cost):
    if money_received >= coffee_cost:
        global profit
        profit += coffee_cost
        change = money_received - coffee_cost
        print(f"Here is your change of Rs.{change}")
        return True
    else:
        print("There is not enough money. Money refunded")
        return False


# Function to make coffee i.e., to deduct the quantity of resources that are used to make coffee
def make_coffee(coffee_name, coffee_ingredient):
    for item in coffee_ingredient:
        resources[item] -= coffee_ingredient[item]
    print(f"Here is your {coffee_name}")


# Main method
is_on = True

while is_on:
    choice = input("What would you like to have? (latte/expresso/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water = {resources['water']} ml ")
        print(f"Milk = {resources['milk']} ml ")
        print(f"Coffee = {resources['coffee']} g ")
        print(f"Money = Rs.{profit}")
    else:
        coffee_type = menu[choice]
        print(coffee_type)
        if check_resources(coffee_type['ingredients']):
            payment = process_coins()
            if is_payment_successful(payment, coffee_type['cost']):
                make_coffee(choice, coffee_type['ingredients'])
