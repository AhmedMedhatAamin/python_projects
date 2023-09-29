def get_number():
    while True:
        n = int(input("Enter a number to iterate: "))
        if n > 0:
            break
    return n

def get_word():
    user_input = input("Enter the word you want to be repeated: ")
    return user_input

def main():
    number_input = get_number()
    word_input = get_word()

    for _ in range(number_input):
        print(word_input)

if __name__ == "__main__":
    main()