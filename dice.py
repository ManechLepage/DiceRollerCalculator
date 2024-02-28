import random


class Die:
    def __init__(self, faces):
        self.faces = [i for i in range(1, faces + 1)]
        self.value = 0

    def generate_value(self):
        return random.choice(self.faces)


class Dices:
    def __init__(self, dices):
        self.dices = dices
        self.score = 0

    def roll_dices(self):
        for die in self.dices:
            die.value = die.generate_value()

    def calculate_score(self):
        self.score = 0
        for die in self.dices:
            self.score += die.value


def print_dices(dices):
    for die in dices.dices:
        print(f"Dice: {len(die.faces)}, Score: {die.value}")
    dices.calculate_score()
    print(f"FINAL SCORE: {dices.score}")


def add_barrier():
    print("=========================Adding Dices=========================")


def score_barrier():
    print("=========================Scoring Dices=========================")
