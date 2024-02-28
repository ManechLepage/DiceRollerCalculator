import condition_rules


def reroll_if_even(dices, odd_or_even):
    for die in dices.dices:
        if die.value % 2 == odd_or_even:
            die.value = die.generate_value()
    return dices
