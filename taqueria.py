menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
total_cost = 0.00
while True:
    try:
        order = input("Place your order(press ctrl-D when finished): ").title()
        if not order:
            break

        if order in menu:
            total_cost += menu[order]
            print(f"Total Cost is ${total_cost:.2f}")
        else:
            print("Item not found")
            


    except EOFError:
        print(f"\nFinal total cost:${total_cost:.2f}")
    except KeyError:
        print("Item not found")
        break
