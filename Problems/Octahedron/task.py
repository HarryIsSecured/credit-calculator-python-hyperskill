import math

x = int(input())

area = 2 * math.sqrt(3) * (x ** 2)
volume = (1 / 3) * math.sqrt(2) * (x ** 3)

print(round(area, 2), round(volume, 2))
