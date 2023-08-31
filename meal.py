def main():
    t = input("Enter the time in 24-hour format (hh:mm): ")
    time = convert(t)

    if 7 <= time <=8:
        print("Breakfast time")
    elif 12<= time <= 13:
        print("Lunch time")
    elif 18<= time <= 19:
        print("Dinner time")


def convert(t):
    hours, min = t.split(":")
    hours = int(hours)
    min = int(min)
    return float(hours + min/60)


if __name__ == "__main__":
    main()
