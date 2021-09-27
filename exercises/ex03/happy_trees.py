"""Drawing forests in a loop."""

__author__ = "123456789"

# The string constant for the pine tree emoji
TREE: str = '\U0001F332'

depth: int = int(input("Enter an integer: ")) 

i = 0
horizontal: str = ""
if depth > 0: 
    while i < depth:
        horizontal = horizontal + TREE
        i = i + 1
        print(horizontal)
       
