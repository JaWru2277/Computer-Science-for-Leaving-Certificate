
#Question 16 (b)

x = int(input("Enter how many numbers you would like to calculate: "))
#Lets the user control how many items there will be in the list

numbers = [] #Empty list where all the numbers will be added to

for i in range(0,x):
    number = int(input("Enter a number: "))
    numbers.append(number) #Lets the user input the numbers they want to have calculated and saves it to the list "numbers"
print("The initial list of values is:", numbers) #Displays the list

if len(numbers) == 0: #If the list is empty
    print("Error, the list is empty. Cannot compute median") #Display an error message
else:
    numbers.sort() #Sorts the list from smallest to biggest
    print("The sorted list of values is:", numbers) #Displays the sorted list

    if x%2 == 1: #If there are an odd amount of numbers
        median = numbers[x//2] #The median is the centre value (calculated with floor divide)
        
    elif x%2 == 0: #If there are an even amount of numbers
        median1 = numbers[x//2] #The first median value (calculated with floor divide)
        median2 = numbers[(x//2-1)] #The second median value (The value before the first median value in the index)
        median = (median1+median2)/2 #Add the first and second median value together and divide them by 2 to get the final median
    
    print("The median is", median) #Prints the median of the number list

