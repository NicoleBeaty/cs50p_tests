deep = input("What's the answer to the Great Question of Life.the universe and Eeverything?")

if deep == 42 or deep == "forty-two" or deep == "forty two":
    print("Yes")
else:
    print("No")

#alternative code
deep = input("What's the answer to the Great Question of Life.the universe and Eeverything?")

if deep in ("42", "forty-two", "forty two"):
    print("Yes")
else:
    print("No")
