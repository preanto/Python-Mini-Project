import random
secret_number = random.randint(1,5)
chances = 3

while(chances!=0):
    guess = int(input("Guess A number between 1-5: "))
    if(guess == secret_number):
        print("You guessed it right! Congratulations")
        break
    else:
        chances = chances - 1
        print("WRONG GUESS. TRY AGAIN")
        print("Attempts Remaining: ", chances)

if(chances==0):
    print("You've lost the game. Do you want to play again?")
else:
    print("You are a champion")