"""Showing how the four operations work together in Python"""

__author__ = 730383911

left_hand_side: int = int(input("Left-hand side: "))
right_hand_side: int = int(input("Right-hand side: "))
less_than = bool(left_hand_side < right_hand_side)
is_at_least = bool(left_hand_side >= right_hand_side)
equals = bool(left_hand_side == right_hand_side)
does_not_equal = bool(left_hand_side != right_hand_side)

print(str(left_hand_side) + " < " + str(right_hand_side) + " is " + str(less_than))
print(str(left_hand_side) + " >= " + str(right_hand_side) + " is " + str(is_at_least))
print(str(left_hand_side) + " == " + str(right_hand_side) + " is " + str(equals))
print(str(left_hand_side) + " != " + str(right_hand_side) + " is " + str(does_not_equal))