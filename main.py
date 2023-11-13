from data import *

def display_resources():
    for key,value in resources.items():
        print(f"{key}: {value}")
    print(f"money: ${money}")

def check_order():
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
    price = MENU[drink]["cost"]

    if check_ingredients():
        print(f"Your order's Price is: ${price}")
        print("Please Insert Coins.")
        if count_change():
            print(f"Here is Your {drink}, Enjoy!!!")
            return True
    return False

def check_ingredients():
    ingredients = MENU[drink]["ingredients"]

    for key,value in ingredients.items():
        if resources[key] < value:
            print(f"Sorry There is not Enough {key}.")
            return False
    
    for key,value in ingredients.items():
        resources[key] -= value
    return True

def count_change():
    quarters = float(input("\tquarters: $")) * 0.25
    dimes = float(input("\tdimes: $")) * 0.10
    nickels = float(input("\tnickels: $")) * 0.05
    pennies = float(input("\tpennies: $")) * 0.01
    price = MENU[drink]["cost"]
    received_pay = quarters + dimes + nickels + pennies

    if received_pay > price:
        print(f"Here is Your Change: ${round(received_pay - price, 2)}")
        return True
    elif received_pay < price:
        ingredients = MENU[drink]["ingredients"]
        for key,value in ingredients.items():
            resources[key] += value
        
        print(f"Sorry, That's Not Enough Money.")
        print(f"Here is Your Inserted Money: ${round(received_pay, 2)}")
        print(f"Please Re-order and Insert The Required Money.")
        return False
    else: return True


money = 0
while True:
    drink = input("What would you like? (Espresso/Latte/Cappuccino): ").lower()
    if drink == "off":
        break
    money += check_order()