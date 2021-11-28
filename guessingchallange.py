import random

highest = 10
answer = random.randint(1, highest)

guess = ""
tries = 0
print("Please guess a number between 1 and {}".format(highest))
while guess != answer:
    guess = int(input())
    if guess == 0:
        print("You have quit the game")
        break
    elif guess == answer:
        if tries == 0:
            print("You got it first time")
            break
        else:
            print("Well done, you got it on the {} guess".format(tries))
            break
    elif guess < answer:
        print("Please guess higher")
    elif guess > answer:
        print("please guess lower")
    tries += 1


