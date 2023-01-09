import random

top_range = input("Choose a number: ")

if top_range.isdigit():
    top_range = int(top_range)
    
    if top_range <= 0:
        print("Please enter a number larger than 0")
        quit()
else:
    print("Please enter a number")
    quit()

random_num = random.randint(0, top_range)
guesses = 0


while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please enter a number")
        continue

    if user_guess == random_num:
        print("You win")
        break
    elif user_guess > random_num:
        print("You were above the number")
    else:
        print("You were below the number")
        
print("It took you", guesses, "guesses to get the right answer" )
        


    







