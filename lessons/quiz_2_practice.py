"""Loops Practice!"""


def one() -> int:
    x: int = three(2)
    print("one")
    return x + 1


def two() -> int:
    x: int = 2
    print("two")
    return x


def three(x: int) -> int:
    x = x + two()
    print("three")
    return x


print(one())