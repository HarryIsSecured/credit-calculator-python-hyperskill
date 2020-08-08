import math

x = int(input())

print(round((1 / (1 + math.exp(-x))), 2))
