import numpy as np
from matplotlib import pyplot as plt

def roll_dice():
    return (np.random.randint(1, 7) + np.random.randint(1, 7))
