s1 = "Look! Double quotes!"
s2 = 'Ooooh! Single quotes!'

print(s1, type(s1))
print(s2, type(s2))

single_in_double = "Eng 110 said 'Wow!'"
double_in_single = 'Eng 110 said "Wow!"'
backslash = 'Eng 110 said "Wow! \n\tThis is amazing!"'

print(single_in_double)
print(double_in_single)
print(backslash)

s = "Hello world!"
c = s[1]
print(c)
print(s[6])

print(s[::-1])
print(len(s))

print(type("Hello"))

s = "Engineering 110"

print(s.lower())
print(s.upper())


a = "there are"
number = 10
fruit = "apples"


# F-strings = Formatted strings

# d = f"F-String: {a} {b} {c}"

# Casting
to_print = f"{a} {number} {fruit}.".capitalize()
print(to_print)

# Input

last_name = input("What is your last name?\n")
number = input("Type in your favourite number:\n")
reply = f"Your last name is {last_name}.\nYour favourite number is {number}.\nWell done!"
print(reply)




