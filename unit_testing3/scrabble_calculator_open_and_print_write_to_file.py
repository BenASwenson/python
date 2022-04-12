from scrabble_calculator import scrabble_calculator


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