import random


def chance(likelyhood):
    number = random.uniform(0, 1)

    return number >= likelyhood
