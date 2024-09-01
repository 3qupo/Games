from random import randint

print("Hello, you need to choose a number from 0 to 9")
result_bot = randint(1, 9)
while(True):
    result = int(input('Number: '))
    if result == result_bot:
        print("You win")
        break
    else: print("Try again")

