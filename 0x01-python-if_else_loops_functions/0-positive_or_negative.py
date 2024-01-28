#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number > 0:
    print("{}is positive".format(number))
elif number == 0:
    print("{}is zero".format(number))
else:
<<<<<<< HEAD
    print("{}is negative".format(number))
=======
    print(f"{number} is negative")
>>>>>>> 499c7e1a6732e0051ca86e032776507d2026a7dc
