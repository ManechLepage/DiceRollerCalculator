import additive_rules
import score_rules
import dice


dice_set = dice.Dices([dice.Die(4), dice.Die(6), dice.Die(8), dice.Die(10), dice.Die(12), dice.Die(20)])
dice.print_dices(dice_set)

dice.add_barrier()

dice_set = additive_rules.add_closest_dice_if_prime(dice_set)
dice.print_dices(dice_set)

dice.score_barrier()

dice_set.roll_dices()
dice.print_dices(dice_set)

dice.score_barrier()

dice_set = score_rules.reroll_if_even(dice_set, 0)
dice.print_dices(dice_set)
