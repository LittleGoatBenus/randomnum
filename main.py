import random

num = 1,2,3,4,5,6,7,8,9,10

randnum = random.choice(num)


usrin = int(input("number guesser, choose a number between range 1 -10: "))


if usrin == randnum:
    print("Correct guess")

else:
    print("wrong guess correct number was:", randnum)
