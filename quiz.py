# Spanish quiz to help me practice spanish vocabulary words and Python
# Two birds with one stone
# Made it so I don't deal with Duolingo ads

print("Welcome to the Spanish Learning Quiz")

playing = input("Wanna Play? ")

if playing.lower() != "yes":
    quit()


print("Alright Lets Go")

score = 0

answer = input("What is hello in spanish? ")
if answer.lower() == "hola":
    print("Correct")
    score += 1
else:
    print("Incorrect")
    
answer = input("What is good morning in spanish? ")
if answer.lower() == "buenos dias":
    print("Correct")
    score += 1
else:
    print("Incorrect")

answer = input("What is good bye in spanish? ")
if answer.lower() == "adios":
    print("Correct")
    score += 1
else:
    print("Incorrect")

answer = input("What is good afternoon in spanish? ")
if answer.lower() == "buenos tardes":
    print("Correct")
    score += 1
else:
    print("Incorrect")
    

print("You got " + str(score) + " questions right")

print("You got " + str((score/4) * 100) + "%")