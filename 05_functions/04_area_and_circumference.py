import math


def circle_stats(radius):
    area = round(math.pi * radius * radius, 2)
    circumference = round(2 * math.pi * radius, 2)
    return area, circumference


area, circumference = circle_stats(5)

print("area", area, "circumference", circumference)
