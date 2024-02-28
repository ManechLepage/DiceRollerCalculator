import condition_rules
import dice


def dupe_dice_type_prime_numbers(dices):
    dices.roll_dices()
    for die in dices.dices:
        if condition_rules.is_prime(die.value):
            dices.dices.append(dice.Die(len(die.faces)))
    return dices


def add_closest_dice_if_prime(dices):
    dices.roll_dices()
    for die in dices.dices:
        if condition_rules.is_prime(die.value):
            dices.dices.append(dice.Die(condition_rules.find_closest_dice_type(die.value)))
    return dices