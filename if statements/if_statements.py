# write a program that prints the numbers from 1 to 100.  But for multiples of three print "Fizz"
# and for the multiples of five print "Buzz".  For numbers which are multiples of both three and five
# print "FizzBuzz".

def prints_to_hundred():
    mults_3 = [3, 6, 9, 12, 15, 18, 21, 24, 27, 31, 34, 37, 40, 43, 46, 49, 52, 55,
               58, 61, 64, 67, 70, 73, 76, 79, 82, 85, 88, 91, 94, 97, 100]
    mults_5 = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]

    for num in range(101):
        if num in mults_3 and num not in mults_5:
            print("Fizz")
        elif num in mults_3 and num in mults_5:
            print("FizzBuzz")
        elif num in mults_5 and num not in mults_3:
            print("Buzz")
        else:
            print(num)

prints_to_hundred()








