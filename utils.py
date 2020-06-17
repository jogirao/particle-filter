import math


def process_radians(angle):
    while abs(angle) > math.pi:
        angle += math.pi * (2 if angle < 0 else -2)
    return angle
