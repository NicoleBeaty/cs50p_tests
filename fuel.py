def main():
    while True:
        try:
            level = input("Enter fuel level(fraction):")
            x,y = level.split("/")
            x = int(x)
            y = int(y)
            gauge = round((x/y) *100 )
            
            if x > y or y == 0:
                raise ValueError

            print(f"Fuel level is {gauge}%")

            if gauge <= 1:
                print("Empty")
            elif gauge >= 99:
                print("Full")
            break
        except(ValueError):
            print("Invalid input. Please enter a valid fraction")
        except(ZeroDivisionError):
            print("Invalid input. Denominator is 0")
    

if __name__ =="__main__":
    main()
