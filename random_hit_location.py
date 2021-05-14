import random

HIT_LOCATIONS = [
    'Skull',             #  1.85%
    'Face',              #  2.78%
    'Right Leg',         # 11.57%
    'Right Arm',         #  9.72%
    'Upper Right Torso', #  9.14%
    'Upper Left Torso',  #  9.14%
    'Lower Left Torso',  #  9.14%
    'Lower Right Torso', #  9.14%
    'Left Arm',          # 11.57%
    'Left Leg',          # 16.67%
    'Left Hand',         #  2.31%
    'Right Hand',        #  2.31%
    'Left Foot',         #  1.39%
    'Right Foot',        #  1.39%
    'Neck'               #  1.39%
]

HIT_LOCATION_WEIGHTS = [
    18519,
    27778,
    115741,
    97222,
    91435,
    91435,
    91435,
    91435,
    115741,
    166667,
    23148,
    23148,
    13889,
    13889,
    18519
]


def provide_random_hit_locations(sample_size):
    return random.choices(HIT_LOCATIONS, weights=HIT_LOCATION_WEIGHTS, k=sample_size)
