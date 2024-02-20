

#funtions area

#Checks users enter yes (y) or no (n)
def yes_no(question):

        while True:
            response = input(question).lower()

            #Checks user responcse, question
            #Repeats if users don't enter yes / no
            print(f"You answered {response} to the question")

            if response == "yes" or response == "y":
                return "yes"

            elif response == "no" or response == "n":
                return "no"

                print("Program")

            else:
                print("you did not choose a vaild response, please try again.")




def instruction():
    print('''
   
---------------------------------- Instructions ---------------------------------
   
  To begin, decide on a score goal (eg: the first one to get a score of 50 Wins!)
  
  
  for each round of the game, you win points by rolling dice 
  The winner of the end of the round is the one who gets 13 (or slightly less)
  
  
  If you win the round, then your score will increase by the number of points 
  that you earn.
  If your first roll of two dice is a double (eg: both dice show a three), 
  then your score will be DOUBLE the number of points.
  
  
  If you lose the round, then you don't get any points.
  
  If you and the computer tie (eg: you both get a score of 11), then you
   will have 11 points added to your score.
 -------------------------------------------------------------------------------
    ''')


#Main routine


print()
print("🎲🎲 Roll it 13! 🎲🎲")
print()
print("❤️")

#Question asking to see the rules of the game.


# loop for testing purposes

want_instructions = input("Do you wish to see the instruction?").lower()
print(f"You answered {want_instructions} to the question")


#Check users enter yes (y) or no (n)
if want_instructions == "yes" or want_instructions == "y":
    instruction()

print("Program")














