
#Task 1
numbers = []
for i in range (5):
    number = int(input("Enter a number: "))
    numberAdded = int(number+1)
    numbers.append(numberAdded)
    
print(numbers)

#Task 2
hours = [12, 7, 9, 9, 6, 8, 2]
hoursInput = []

"""
#Optional prompts
for i in range(7):
    h = int(input("How many hours were you at home?"))
    hoursInput.append(h)
   """

N = len(hours)
totalL = 0
for i in hours:
    litres = i*0.5
    totalL += litres

print("Stephen drinks a total of", totalL, "litres in 7 days.")

totalM = round(totalL*1.35, 2)
print("Stephen owes his father €", totalM)

#Task 3
rainfall = []
for i in range(7):
    rain = float(input("How many cm of rainfall have you recorded today? "))
    rainfall.append(rain)

print("The rainfall in cm each day was as follows:", rainfall)

totalRain = 0
length = len(rainfall)
for i in rainfall:
    totalRain += i
    totalRain = round(totalRain, 2)
    average = round(totalRain/length, 2)
    
print("There has been a total of", totalRain, "cm of rainfall this week with an average of", average, "cm.")

for i in rainfall:
    if i > 3.5:
        print("There has been more than 3.5 cm of rainfall a day")      

#Task 4

sales = [
    ["danny", 12.5, 23.2, 5.2],
    ["sarah", 7.85, 2, 1],
    ["jacqueline", 15.2, 17.3, 43.6],
    ["ruaidhri", 23.19, 8.3, 17.5]
]


name = input("Enter your name: ")
name = name.lower()

for row in sales:
    if row[0] == name:
        sale = float(input("Enter the value of your last sale: "))
        row.append(sale)
        
        saleValues = row[1:]
        saleMax = max(saleValues)
        saleMin = min(saleValues)
        saleTotal = sum(saleValues)
        saleAverage = saleTotal/len(saleValues)
        
        print("Maximum sale:", saleMax)
        print("Total sales:", saleTotal)
        print("Minimum sale:", saleMin)
        print("Average sale:", saleAverage)
        print("Updated sales:", sales)

        break
else:
    print("Error, salesperson not found")

