"""Practicing numeric operators, type conversions, and string concatenation."""

__author__ = "730383911"

left_hand_side: int = int(input("Left-hand side: "))
right_hand_side: int = int(input("Right-hand side: "))

exponent = left_hand_side ** right_hand_side
division = left_hand_side / right_hand_side
integer = left_hand_side // right_hand_side
remainder = left_hand_side % right_hand_side
print(str(left_hand_side) + " ** " + str(right_hand_side) + " is " + str(exponent))
print(str(left_hand_side) + " / " + str(right_hand_side) + " is " + str(division))
print(str(left_hand_side) + " // " + str(right_hand_side) + " is " + str(integer))
print(str(left_hand_side) + " % " + str(right_hand_side) + " is " + str(remainder))