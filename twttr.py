s_input = input("Enter a string: ")
vowels = "AEIOUaeiou"
output = ""

for char in s_input:
    if char not in vowels:
        output += char

print(f"New string is {output}")
