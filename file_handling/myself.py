def open_and_print_file(file):
    try:
        with open(file, "r") as file:
            for line in file.readlines():
                print(line.rstrip('\n'))

    except FileNotFoundError:
        print("File cannot be found")
    finally:
        print("\nExecution complete")


open_and_print_file("myself.txt")
