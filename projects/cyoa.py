"""Choose Your Own Adventure."""

__author__ = "730383911"

points: int = 0
player: str
going_again: int = 0


NORTHWEST: str = '\U0001F332'
MIDWEST: str = '\U0001F922'
SOUTH: str = '\U0001F69C'
NORTHEAST: str = '\U0001F5FD'
SOUTHWEST: str = '\U00002600'


def main() -> None:
    """Main function that player follows through."""
    greet()
    global points
    points = 0
    game()
    point_total()
    continuing()


def greet() -> None:
    """Introduction message."""
    message: str = str("In this game, you will be told what region of the country you shoud live in based on your answers to a series of statements. ")
    print(message)
    name: str = str(input("To begin, enter your name here: "))
    global player
    player = name
    
   
def game() -> None:
    """Choosing your path."""
    cold_weather()


def exit_game() -> None:
    """Printing goodbye message."""
    global points
    global player
    print(f"Dang, {player}, was my game not good enough for you? Oh well, your lost. You got {points} points. ")


def cold_weather() -> None:
    """Ask the player what their weather preference is."""
    global points
    global player
    print(f"Hi, {player}. To start, choose which weather you like most. ")
    print("a. Cold")
    print("b. Hot")
    print("c. Exit the quiz")
    fav_weather: str = str(input("Enter your prefered weather as a, b, or c to exit the quiz. "))
    if fav_weather == "a":
        points += 1
        option_one()
    else:
        if fav_weather == "b":
            points += 2
            option_two(points)
        else:
            if fav_weather == "c":
                exit_game()


def option_one() -> None:
    """Player chose 1st path."""
    print("You like cold weather? Better you then me. How do you feel about historic charm? ")
    print("a. I want to live somewhere historic. ")
    print("b. I am more into the newer vibe. ")
    history: str = str(input("Enter your preference for how important history is to you with either a or b. "))
    global points
    if history == "a":
        points += 1
        location()
    else:
        if history == "b":
            points += 4
            location()


def option_two(points: int) -> int:
    """Player chose 2nd path."""
    global player
    print(f"So, {player}, you like hot weather! Do you like urban or rural environments? ")
    print("a. Urban")
    print("b. Rural")
    environment: str = str(input("Enter your prefered environment as a or b. "))
    if environment == "a":
        points += 1
        location()
    else:
        if environment == "b":
            points += 2
            location()
    return points
        

def location() -> None:
    """Main question 2."""
    global player
    print(f"As you probably know {player}, this country is massive. Do you need to be close to the ocean...let's say...within a three hour drive? ")
    print("a. I need to be within a few hours drive of the ocean. ")
    print("b. The ocean is great, but maybe only once a year at the most. ")
    ocean: str = str(input("Answer a or b! "))
    global points
    if ocean == "a":
        points += 1
        scenery()
    else:
        points += 50
        scenery()


def scenery() -> None:
    """Final question."""
    global player
    print(f"Let's be honest. 99 percent of people don't wanna live in the midwest. Are you the 1 percent, {player}? ")
    print("a. No, I am normal. ")
    print("b. Miles of corn fields excite me. Considering myself a buckeye or a Missourian doesn't cause me shame. ")
    final_answer: str = str(input("You know the drill. Answer a or be for the answer. "))
    global points
    if final_answer == "a":
        points += 1
    else:
        points += 1000


def point_total() -> None:
    """Adding up final points."""
    global points
    if points <= 4:
        print(f"You got {points} points, you should move to the Northeast {NORTHEAST}! ")
    else:
        if points <= 5:
            print(f"You got {points} points, you should move to the Southwest {SOUTHWEST}! ")
        else:
            if points <= 6:
                print(f"You got {points} points, you should move to the South {SOUTH}! ")
            else:
                if points <= 9:
                    print(f"You got {points} points, you should move to the Pacific Northwest {NORTHWEST}! ")
                else:
                    print(f"You got {points} points, you should move to the Midwest {MIDWEST}. You are a trooper. ")


def continuing() -> None:
    """Asking the player if they want to continue the game."""
    global going_again
    going_again = int(input("Well, you finished the game. Wasn't it fun! If you want to keep playing, enter the number 5. "))


if __name__ == "__main__":
    main()