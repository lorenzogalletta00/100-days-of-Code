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
total_money = 0.00
# Coins
PENNY = 0.01 # $ : 1 cent
DIME = 0.10 # $ : 10 cents
NICKEL = 0.05 # $ : 5 cents
QUARTER = 0.25 # $ : 25 cents

# Process Coins
def insert_coins():
    """This function converts coins in the equivalent money amount in dollars"""
    print("Please insert coins.")
    nr_of_quarters = int(input("How many quarters?: "))
    nr_of_nickels = int(input("How many nickels?: "))
    nr_of_dimes = int(input("How many dimes?: "))
    nr_of_pennies = int(input("How many pennies?: "))
    return PENNY * nr_of_pennies + DIME * nr_of_dimes + NICKEL * nr_of_nickels + QUARTER * nr_of_quarters

def is_transaction_successful(money_paid,actual_cost):
    """The function returns False if money is insufficient"""
    if money_paid < actual_cost:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        global total_money
        total_money += actual_cost
        if money_paid > actual_cost:
            change = round(money_paid - actual_cost, 2)
            print(f"Here is ${change} in change.")
        return True

# TODO: 2. Check resources sufficient to make drink order
def is_out_of_order():
    """This function return True if there are not enough resources for any drink in the list."""
    min_coffee = min([MENU["espresso"]["ingredients"]["coffee"], MENU["latte"]["ingredients"]["coffee"], MENU["cappuccino"]["ingredients"]["coffee"]])
    min_milk = min([MENU["latte"]["ingredients"]["milk"], MENU["cappuccino"]["ingredients"]["milk"]])
    min_water = min([MENU["espresso"]["ingredients"]["water"], MENU["latte"]["ingredients"]["water"], MENU["cappuccino"]["ingredients"]["water"]])
    if resources["water"] < min_water or resources["milk"] < min_milk or resources["coffee"] < min_coffee:
        return True
    else:
        return False

def check_resources(choice):
    """The function checks the remaining resources. If there's not enough of a certain resource, the function return False."""
    if is_out_of_order():
        return "Out of order!"
    else:
        for item in MENU[choice]["ingredients"]:
            if resources[item] < MENU[choice]["ingredients"][item]:
                print(f"Sorry there is not enough {item} for making {choice}.")
                return False
        return True

# TODO: 5. Make Coffee
# Manage the drink selection
def make_coffee(choice, ingredients):
    """The function makes coffee and deducts the ingredients from resources"""
    for item in ingredients:
        resources[item] -= ingredients[item]
    print(f"Here is your {choice} ☕. Enjoy!")
# Coffee Machine
def coffee_machine():
    # Ask the user what they want to drink
    turn_off = False
    while not turn_off:
        drink = input("What would you like? (espresso/latte/cappuccino): ")
        if drink == "off":
            #turn off the coffee machine
            turn_off = True
        # TODO: 1. Print report of all coffee machine resources
        elif drink == "report":
            print(f"Water: {resources["water"]}ml")
            print(f"Milk: {resources["milk"]}ml")
            print(f"Coffee: {resources["coffee"]}g")
            print(f"Money: ${total_money}")
        elif drink == "espresso" or drink == "latte" or drink == "cappuccino":
            # create a function to manage the selection
            if check_resources(drink):
                # TODO: 3. Verify what type of coins the user insert into the coffee machine
                dollars_inserted = insert_coins()
                # TODO: 4. Check the transaction
                if is_transaction_successful(dollars_inserted, MENU[drink]["cost"]):
                    make_coffee(drink, MENU[drink]["ingredients"])
        else:
            print("Error! Not Valid Selection!")

coffee_machine()
