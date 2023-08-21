def main():
    info = input("How was your day?")
    new_info = convert(info)
    print(new_info)

def convert(input_str): 
    new_str = input_str.replace(":)","🙂").replace(":(", "🙁")
    return new_str
    
if __name__ == "__main__":
    main()
