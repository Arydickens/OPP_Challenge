class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5
        self.energy = 5
        self.happiness = 5
        self.tricks = []

    def eat(self):
        self.hunger = self.hunger - 3
        if self.hunger < 0:
            self.hunger = 0

        self.happiness = self.happiness + 1
        if self.happiness > 10:
            self.happiness = 10

        print(
            f"{self.name} eats. Hunger is now {self.hunger}. Happiness is now {self.happiness}.")

    def sleep(self):
        self.energy = self.energy + 5
        if self.energy > 10:
            self.energy = 10
        print(f"{self.name} sleeps. Energy is now: {self.energy}")

    def play(self):
        if self.energy >= 2:
            self.energy = self.energy - 2
            self.happiness = self.happiness + 2
            if self.happiness > 10:
                self.happiness = 10

            self.hunger = self.hunger + 1
            if self.hunger > 10:
                self.hunger = 10

            print(
                f"{self.name} plays! Energy: {self.energy}, Happiness: {self.happiness}, Hunger: {self.hunger}")
        else:
            print(f"{self.name} is too tired to play.")

    def get_status(self):
        print(f"--- {self.name}'s Status ---")
        print(f"Hunger: {self.hunger}/10")
        print(f"Energy: {self.energy}/10")
        print(f"Happiness: {self.happiness}/10")

    def train(self, trick):
        self.tricks.append(trick)
        print(f"{self.name} learned a new trick: {trick}!")

    def show_tricks(self):
        if self.tricks:
            print(f"{self.name} knows the following tricks: {', '.join(self.tricks)}")
        else:
            print(f"{self.name} hasn't learned any tricks yet.")
