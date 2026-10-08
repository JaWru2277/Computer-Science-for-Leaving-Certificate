from random import randint

#Challange 1

def randomList(): # makes a list of ten random numbers
    numbers = []
    
    for i in range(10):
        numbers.append(randint(1,200))
    return numbers

def numberChecker(user, random): #Checks if the numbers entered by the user are in the random list
    counter = 0
    for i in user:
        if i in random:
            counter += 1
            
    if counter == 3: # Prints if winner or loser
        print("\nWE HAVE A WINNER!")
        print("Amount won: €0.1")
    else:
        print("\nSwing and a miss!")
        print("The secret numbers were:", randomNumbers)
        print("\nTry again?")

def sequenceChecker(user, random): #Checks if the numbers entered by the user are in the random list
    counter1 = 0                   #in that exact sequence
    counter2 = 3                   #Also checks for the jackpot
    winner = 0
    
    firstThree = random[0:3]
    
    for i in range(7): # If the numbers appeared in the sequence the winner counter goes up by one
        sequence = random[counter1:counter2]
        
        if user == firstThree: #Checks if the user guess the jackpot
            winner += 10
            break
        elif sequence == user: #if not, checks if the sequence appears at all
            winner += 1
       
        counter1 += 1
        counter2 += 1
    
    if winner <= 3 and winner >= 1: #If the winner counter is greater or equal to three, a winning message is printed. I said three instead of one to account for the unlikely event that the sequence appears twice or maybe three times. 
        print("\n**CONGRATULATIONS**")                         
        print("Your numbers appeared in that exact sequence!")
        print("Special Prize: €0.5")
    elif winner == 10: # If the jackpot was achieved
        print("\n****JACKPOT****")
        print("JACKPOT PRIZE: €5")
    else: #If neither hapened
        print("\nSwing and a miss!")
        print("The secret numbers were:", randomNumbers)
        print("\nTry again?")


print("*****Lottery*****\n") # Introduction
print("Welcome, proceed below:")

randomNumbers = randomList() #makes a list

print(randomNumbers) #only here for debugging

userNumbers = [] #prompts the user to input 3 numbers
number = 0
while number < 3:
    numberInput = int(input("	Input a number between 1 and 200: "))
    if numberInput >= 1 and numberInput <= 200: # checks if the numbers are within range
        userNumbers.append(numberInput)
        number += 1
    else: #if not it prompts the user to repeat the input
        print("	 Enter a valid number")
        
#numberChecker(userNumbers, randomNumbers) #Calls the numberChecker
sequenceChecker(userNumbers, randomNumbers) #Calls the sequenceChecker + jackpot


#-------------------------------#
"""
Challange 1: Check if the user's numbers exist inside the computer's list.
Create a function that generates a list of 10 random numbers.
Write a block of code (or a new function) that checks if all 3 of the user's numbers
can be found inside the 10 random numbers.
If they match, print "You Won!"If any are missing, print "Try Again!" and display the computer's hidden list.

Challange 2: Order matters!
Check if the user's 3 numbers appear together in the exact order they typed them.
Extend your program to inspect the computer's list for a matching sequence.
Hint: Use a loop to check three-number groups (slices) of the computer's list,
like index 0:3, then 1:4, then 2:5, and so on.
Print a special victory message if the user successfully guesses a consecutive sequence.

Challange 3: Compare the user's inputs directly with the of the computer's list.
Modify your code to extract a sub-list containing only the first 3 elements of the computer's list.
Compare this sub-list directly to the user's list.
Print a jackpot message if they are a perfect match in both value and position.
"""
