class Money:
    def __init__(self):
        self.money = input("How many pounds do you have?")

    def __str__(self):
        return f"This is your amount: {self.money}!"

    def __format__(self):
        return format(self, ".2f")



my_money = Money()
print(my_money)





