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
            print(f"You picked {choice}.")
        else:
            print("That is not on the menu.")

    print("Smoothie station closed.")

if __name__ == "__main__":
    main()