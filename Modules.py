# modules are pieces of code that other people have written to fulfill common tasks,
# such as generating random number, performing mathematical operations.
print("RANDOM NUMBER")
import random
for i in range(5):
    value = random.randint(1,6)
    print(value)

print("\n\nmath")
from math import pi
print(pi)