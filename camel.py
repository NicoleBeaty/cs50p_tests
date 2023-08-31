#Converts camel case to snake case
def camel_to_snake(camel):
    snake = [camel[0].lower()]
    for char in camel[1:]:
        if char.isupper():
            snake.extend(['_',char.lower()])
        else:
            snake.append(char)
    return ''.join(snake)

def main():
    camel_case = input("Enter a camel case variable name: ")
    snake_case = camel_to_snake(camel_case)
    print("Snake case variable name: ",snake_case)

if __name__ == "__main__":
    main()
