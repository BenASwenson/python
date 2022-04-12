from animal import Animal

class Reptile(Animal):

    def __init__(self):
        super().__init__()
        self.cold_blooded = True
        self.tetrapod = None
        self.heart_chambers = [3, 4]
        self.amniotic_eggs = None

    def seek_heat(self):
        print("It's too cold, I need heat!")

    def hunt(self):
        print("I'm hunting my prey")

    def use_venom(self):
        print("I am injecting/squirting venom")

    def attract_mate_through_scent(self):
        print("I'm looking for a relationship")

# jeremy = Reptile()
# jeremy.breathe()

