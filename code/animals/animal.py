import random
from globals import G_turn

class Animal:
    def __init__(self):
        self.weight = None
        self.age = 0
        self.gender = self.set_gender()
        self.spawnTurn = G_turn

    def set_gender(self):
        #set male or female
        rand = random.randint(0, 1)
        gender = ""
        if rand == 0:
            gender = "male"
        else:
            gender = "female"
        return gender

    def set_age(self):
        # Every 12 turn the animal aged one year
        turnLived = G_turn - self.age
        yearLived = 0
        i = 0
        while i < turnLived:
            if turnLived % 12 == 0:
                yearLived += 1
        return yearLived


