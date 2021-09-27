"""Repeating a beat in a loop."""

__author__ = "730383911"


# Begin your solution here...
beat: str = input("What beat do you want to repeat? ")

times: int = int(input("How many times do you want to repeat it? "))

i: int = 0
final: str = ""

if times <= 0:
    print("No beat...")
else:
    while i < times:
        if i == 0:
            final = final + beat
            i = i + 1
        else:
            i = i + 1
            final = final + " " + beat
    print(final)