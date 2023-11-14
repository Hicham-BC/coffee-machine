from data import *

def display_resources():
    """
    Display the current status of available resources and money.
    """
    for key,value in resources.items():
        print(f"{key}: {value}")
    print(f"money: ${money}")

def make_drink():
    """
    Deduct the required ingredients from available resources to prepare the ordered drink.
    """
    ingredients = MENU[drink]['ingredients']

    for key,value in ingredients.items():
        resources[key] -= value

def check_order():
    """
    Check if the requested drink is available and process the order.
    
    Returns:
    - The profit earned from the order (zero if the order is not available).
    """
    orders = ["espresso", "latte", "cappuccino", "report"]

    if drink in orders:
        if drink == "report":
            display_resources()
        else:
            if deliver_order():
                profit = MENU[drink]["cost"]
                return profit
    else:
        print("Sorry, Your Order is not Available.")
    
    return 0

def deliver_order():
    """
    Handle the payment process, deliver the ordered drink, and manage change.

    Returns:
    - True if the order is successfully delivered; False otherwise.
    """
    price = MENU[drink]["cost"]

    if ingredients_sufficient():
        print(f"Your order's Price is: ${price}")
        print("Please Insert Coins.")
        if transaction_successful():
            make_drink()
            print(f"Here is Your {drink}, Enjoy!!!")
            return True
    return False

def ingredients_sufficient():
    """
    Check if there are enough ingredients for the requested drink.

    Returns:
    - True if there are enough ingredients; False otherwise.
    """
    ingredients = MENU[drink]["ingredients"]

    for key,value in ingredients.items():
        if resources[key] < value:
            print(f"Sorry There is not Enough {key}.")
            return False
    
    return True

def process_coins():
    """
    Prompt the user to insert coins and calculate the total amount received.

    Returns:
    - The total amount received from the user as coins.
    """
    coins = int(input("\tquarters: $")) * 0.25
    coins += int(input("\tdimes: $")) * 0.10
    coins += int(input("\tnickels: $")) * 0.05
    coins += int(input("\tpennies: $")) * 0.01

    return coins

def transaction_successful():
    """
    Calculate change based on the coins inserted and handle insufficient payment.

    Returns:
    - True if the Transaction is successful; False otherwise.
    """
    price = MENU[drink]["cost"]
    money_received = process_coins()

    if money_received > price:
        print(f"Here is Your Change: ${round(money_received - price, 2)}")
        return True
    elif money_received < price:
        print(f"Sorry, That's Not Enough Money.")
        print(f"Here is Your Inserted Money: ${round(money_received, 2)}")
        print(f"Please Re-order and Insert The Required Money.")
        return False
    else: return True

# Initialize money variable
money = 0
# Main loop for coffee machine operations
while True:
    # Prompt the user to enter their drink choice
    drink = input("What would you like? (Espresso/Latte/Cappuccino): ").lower()
    # Check if the user wants to turn off the coffee machine
    if drink == "off":
        break
    
    # Process the user's order and update the money variable
    money += check_order()