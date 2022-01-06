from config import *


def to_pygame(coord):
    return (coord[0] + WIDTH/2, (HEIGHT - coord[1]))


def to_cartesian(coord):
    return (coord[0] - WIDTH/2, (HEIGHT - coord[1]))
