import random
import math

lower = int(input("Enter Lower bound:- "))


upper = int(input("Enter Upper bound:- "))
x = random.randint(lower, upper)
total_chances = math.ceil(math.log(upper - lower + 1, 2))
print("\n\tYou've only ", total_chances, " chances to guess the integer!\n")

