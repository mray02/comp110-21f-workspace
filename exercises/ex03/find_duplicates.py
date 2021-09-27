"""Finding duplicate letters in a word."""

__author__ = "730383911"

word: str = input("Enter a word: ")
i: int = 0
answer: bool = False
while i < len(word): 
    m = word[i]
    j = i + 1
    while j < len(word):
        if word[j] == m:
            answer = True
        j = j + 1
    i = i + 1
print("Found duplicate: " + str(answer))