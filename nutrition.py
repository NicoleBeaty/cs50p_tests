frt = input("Fruit: ").capitalize()
fruits = {"fruit":"calories","Apples": "130 calories", "Avocados": "50 calories",
"Bananas":"110 calories", "Grapes":"90 calories"
}

if frt in fruits:
    print(f"{fruits[frt]}")
else:
    print(f"{frt} not found in list")
