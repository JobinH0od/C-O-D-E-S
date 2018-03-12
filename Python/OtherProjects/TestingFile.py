from random import randrange

randomNum = randrange(1, 4)

health = 10



if randomNum == 1:
    print("")
    print("")
    print("You've been attacked by a furious horde of Orcs!")
    print("An Orc with a bow shoots you in the knee and you fall in a 20 foot deep trench...")
    health -= 9
    print("")
    print("Your health has gone down to", health)

if health == 10:
    print("")
    print("Your health is of ", health)

if health == 1:
    print("The Orcs start throwing rocks at you and after getting hit by them a few times you die of a painful death...")
    print("")

health -= 1

if health == 0:
    print("Game Over...")