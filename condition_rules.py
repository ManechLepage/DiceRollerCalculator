def is_prime(score):
    if score > 1:
        for i in range(2, int(score / 2) + 1):
            if (score % i) == 0:
                return False
        else:
            return True
    else:
        return False


def find_closest_dice_type(score):
    if score in [0, 1, 2, 3, 4]:
        return 4
    elif score in [5, 6]:
        return 6
    elif score in [7, 8]:
        return 8
    elif score in [9, 10]:
        return 10
    elif score in [11, 12, 13, 14, 15]:
        return 12
    else:
        return 20
