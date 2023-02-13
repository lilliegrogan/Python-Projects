name = input("Type your name ")
print("Welcome", name, "to the start of your journey!")

answer = input("You come to a fork in the road... Do you choose right or left? ").lower()

if answer == "left":
    
    answer = input("You have come to a long winding river... Do you choose to walk around or swim? walk/swim ").lower()
    if answer == "swim":
        print("You forgot you can't swim and drowned!")
        
    elif answer == "walk":
        print("Did you miss the part where it is a LONG winding river... You walked too long and died of exhaustion!")
        
    else:
        print("not a valid answer you lose")

elif answer == "right":
    
    answer = input("After walking for awhile you come to a bridge... Do you choose to cross or to turn back? cross/turn back ").lower()
    if answer == "cross":
        answer = input("You cross the bridge safely and then encounter a stranger... Do you choose to talk or walk past? talk/walk past ")
        
        if answer == "talk":
            print("The stranger gives you gold for the rest of your journey, you win.")
        elif answer == "walk past":
            print("You get shot with an arrow for trespassing.")
            
        else:
            print("not valid you lose")
            
    elif answer == "turn back":
        print("You end up back where you started. Game Over.")
    else:
        print("not a valid answer you lose")
    

else:
    print("you lose")
    
print("Thank you for playing.", name, "goodbye.")