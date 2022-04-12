# scrabble calculator

def scrabble_calculator():
    user_word = input("What is your favourite word?").lower()

    one = ['a', 'e', 'i', 'o', 'u', 'l', 'n', 'r', 's', 't']
    two = ['d', 'g']
    three = ['b', 'c', 'm', 'p']
    four = ['f', 'h', 'v', 'w', 'y']
    five = ['k']
    eight = ['j', 'x']
    ten = ['q', 'z']

    count = 0

    for char in user_word:
        if not char.isalpha():
            print("Please enter a valid word with alphabet characters")
        else:
            for char in user_word:
                if char in one:
                    count += 1
                elif char in two:
                    count += 2
                elif char in three:
                    count += 3
                elif char in four:
                    count += 4
                elif char in five:
                    count += 5
                elif char in eight:
                    count += 8
                elif char in ten:
                    count += 10

    print(f"Your final score is: {count} points!")


def open_and_print_file(file):
    try:
        scrabble_calculator()
        with open(file, "r") as file:
            for line in file.readlines():
                print(line.rstrip('\n'))
    except FileNotFoundError:
        print("File cannot be found")
        raise
    finally:
        print("\nExecution complete!")
        

def write_to_file(file, order_item):
    try:
        with open(file, "a") as file:
            file.write(order_item + '\n')
    except FileNotFoundError:
        print("File not found")
        raise







