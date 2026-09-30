#Question 16 (a)

def get_grade(result):
    grade = "Unsuccessful"
    
    if result >= 80:
        grade = "Distinction"
    elif result >= 65:
        grade = "Upper Merit"
    elif result >= 50:
        grade = "Lower Merit"
    elif result >= 40:
        grade = "Pass"
    else:
        grade = "Unsuccesful"
        
    return grade

# Calculate and disokay the mean of a list of resuts
results = [39, 32, 62, 88, 51, 62, 64, 81, 77] # Initialise the list
N = len(results) # Initialise N to the number of results
total = 0 # Initialise the running total to 0

# Loop N times
for i in range(N):
    total = total+results[i] # Running total
    
# Divide by the total number of results to give the mean
arithmatic_mean = round(total/N, 2)

# Display the answer
print("The mean percentage mark is", arithmatic_mean)

#(iv)
grade = get_grade(arithmatic_mean)
print("The grade for the average result is", grade)

#(v)
highest = max(results)
lowest = min(results)
print("The lowest score is", lowest)
print("The highest score is", highest)

#(vi)
count1 = 0 #<40
count2 = 0 #50-79

for i in results:
    if i < 40:
        count1 += 1
    elif i >=50 and i <=79:
        count2 += 1
print("The number of scores below 40 is", count1)
print("The number of scores between 50 and 79 inclusive is", count2)

#(vii)
longest = []
current = [results[0]]
for i in range(1, N):
    if results[i] > results [i-1]:
        current.append(results[i])
    else:
        if len(current) > len(longest):
            longest = current
        current = [results[i]]
        
if len(current) > len(longest):
    longest = current
    
print("Longest run of result increase is", longest)

#----------------------------------------------------------------------

#Question 16 (b)

x = int(input("Enter how many numbers you would want to calculate: "))
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

