from snake import Snake

class Python(Snake):

    def __init__(self):
        super().__init__()
        self.large = True
        self.two_lungs = True
        self.venom = True

    def digest_large_prey(self):
        print("Ok, hand me the stretchy pants")

    def constrict(self):
        print("and .. squeeeeze")

    def climb(self):
        print("I am climbing")

    def shed_skin(self):
        print("I'm growing out of this now")

    def breathe(self):
        print("I am breathing really slowly because I am a python")

peter = Python()
peter.breathe()