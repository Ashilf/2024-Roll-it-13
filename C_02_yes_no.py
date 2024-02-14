
#Checks users enter yes (y) or no (n)
def yes_no(question):

        while True:
            response = input(question).lower()
            print(f"You answered {response} to the question")

            if response == "yes" or response == "y":
                return "yes"

            elif response == "no" or response == "n":
                return "no"

            else:
                print("you did not choose a vaild response, please try again.")




#main routione

while True:
    want_instructions = yes_no ( "Do you wish to see the instruction?")
    print(f"You chose {want_instructions}")












