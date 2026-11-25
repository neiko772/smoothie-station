# smoothie_machine.py
# Runs the student cafe's smoothie station: takes orders, checks supplies, takes payment.
#
# Every drink lists the ounces of each ingredient it uses, and its price in dollars.
MENU = {
    "berry": {
        "ingredients": {"ice": 4, "juice": 6},
        "price": 2.50,
    },
    "mango": {
        "ingredients": {"ice": 4, "juice": 4, "yogurt": 4},
        "price": 3.25,
    },
    "tropical": {
        "ingredients": {"ice": 4, "juice": 4, "yogurt": 4},
        "price": 3.75,
    },
}

# What the machine holds at the start of each day, in ounces.
STARTING_SUPPLIES = {
    "ice": 20,
    "juice": 24,
    "yogurt": 12,
}

# What each kind of money is worth, in dollars.
MONEY_VALUES = {
    "dollar bills": 1.00,
    "quarters": 0.25,
    "dimes": 0.10,
    "nickels": 0.05,
}


def print_report(supplies, money):
    for item, amount in supplies.items():
        print(f"{item.capitalize()}: {amount}")
    print(f"Money: ${money:.2f}")

def has_enough(ingredients, supplies):
    for item, needed in ingredients.items():
        if needed > supplies[item]:
            print(f"Sorry, there is not enough {item}.")
            return False
    return True




def ask_count(money, name):
    """Ask how many of one kind of money, until the answer is a whole numeber 0 or more."""
    while True:
        answer = input(f"How many {name}? ")
        try:
            count = int(answer)
            if count >= 0:
                return count
            print("The count cannot be negative.")
        except ValueError: 
            print("Type a whole number, like 2.")

def take_payment():
    print("Please insert money.")
    total = 0.0

    for name, value in MONEY_VALUES.items():
        count = ask_count(name)
        total += count * value

    return round(total, 2)



def main():
    supplies = dict(STARTING_SUPPLIES)
    money = 0.0
    is_open = True 

    print("Smoothie station is open.")

    while is_open:
        choice = input("What would you like? (berry/mango/tropical): ").strip().lower()

        if choice == "close":
            is_open = False
        elif choice == "report":
            print_report(supplies, money)
        elif choice in MENU:
            drink = MENU[choice]
            if has_enough(drink["ingredients"], supplies):
                print("Supplies are fine.")
        else:
            print("That is not on the menu.")

    print("Smoothie station closed.")

if __name__ == "__main__":
    main()