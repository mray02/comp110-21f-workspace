"""Counting letters in a string."""

__author__ = "730383911"


# Begin your solution here...

from typing import Counter


letter: str = input("What letter do you want to search for? ")
word: str = input("Enter a word: ")

i: int = 0
final: str = ""

Counter(word)