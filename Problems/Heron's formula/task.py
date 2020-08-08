# put your python code here
from math import sqrt
x = int(input())
y = int(input())
z = int(input())
p = (x + y + z) / 2
print(sqrt(p * (p - x) * (p - y) * (p - z)))
