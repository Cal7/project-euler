import math
import numpy

def get_intersection(n): #returns the first point of intersection between the line y=x/n and the circle (x-1)^2+(y-1)^2=1
    a = 1 + (1 / (n ** 2))
    b = -2 - (2 / n)
    c = 1

    x = min(numpy.roots([a, b, c]))
    y = x / n

    return {"x": x, "y": y}

def get_concave_triangle_area(n):
    intersection = get_intersection(n)

    return (intersection["x"] * intersection["y"] / 2)\
        + 1\
        - intersection["x"]\
        + (math.sin(2 * math.asin(intersection["x"] - 1)) / 4)\
        + (math.asin(intersection["x"] - 1) / 2)

def get_l_section_proportion(n):
    return get_concave_triangle_area(n) / (1 - (math.pi / 4))

n = 1
while True:
    proportion = get_l_section_proportion(n)
    print("n={} gives a proportion of {}".format(n, proportion))

    if proportion < 0.001:
        break

    n += 1