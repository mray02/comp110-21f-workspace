"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730383911"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


# Begin your solution here...
print("Your fortune cookie says... ")

fortune: int = randint(1, 4)
if fortune > 3:
    print("You are about to have a great week ahead.")
else:
    if fortune > 2:
        print("All your troubles are soon to melt away.")
    else:
        if fortune > 1:
            print("A big dream of yours is about to come true.")
        else:
            print("You are so close to inner peace.")

print("Now, go spread positive vibes!")