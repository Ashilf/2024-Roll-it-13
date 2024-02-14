
#Title
print("🎲🎲 Roll it 13! 🎲🎲")


#Question asking to see the rules of the game.


# loop for testing purposes
while True:
    want_instructions = input("Do you wish to see the instruction?").lower()
    print(f"You answered {want_instructions} to the question")

    if want_instructions == "yes" or want_instructions == "y":
        print("you chose yes")

    elif want_instructions =="no" or want_instructions == "no":
        print("you chose no")

    else:
        print("you did not choose a vaild response, please try again.")















