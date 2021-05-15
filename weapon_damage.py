import random


def provide_weapon_damage(dice_count, damage_bonus, rand: random):
    dice_results = [rand.randint(1, 6) for _ in range(dice_count)]
    return sum(dice_results) + damage_bonus
