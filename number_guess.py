import random
EASY_LEVEL_TURNS=10
HARD_LEVEL_TURNS=5
def check_answer(guess,number,turns):
    if guess>number:
        print("Too high")
        return turns-1
    elif guess<number:
        print("Too low")
        return turns-1
    else:
        print(f"You got it! The answer was {number}")
        
def set_difficulty():
    level=input("Choose between 'easy' or 'hard': ").lower()
    if level=="easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS
        


def game():
    print("Welcome to the guessing game!")
    print("I'm thinking of a number between 1 and 100")
    number=random.randint(1, 100)
    print(f"Pssst, the correct answer is {number}")
    turns=set_difficulty()
    
    guess=0
    while guess!=number:
       print(f"You have {turns} attempts remaining")
       guess=int(input("Make a guess: "))
       turns=check_answer(guess,number,turns)
       if turns==0:
           print("You've run out of guesses, you lose!")
           return

game()