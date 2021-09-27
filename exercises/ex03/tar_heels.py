"""An exercise in remainders and boolean logic."""

__author__ = "730383911"

# Begin your solution here...
number: int = int(input("Enter an int: "))
divide_two: int = int(number % 2)
divide_seven: int = int(number % 7)

if divide_two != 0 and divide_seven != 0:
    print("CAROLINA")

if divide_two == 0 and divide_seven == 0:
    print("TAR HEELS")

if divide_two == 0 and divide_seven != 0:
    print("TAR")

if divide_seven == 0 and divide_two != 0:
    print("HEELS")