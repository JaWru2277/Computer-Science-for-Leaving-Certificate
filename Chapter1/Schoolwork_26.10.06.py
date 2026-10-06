
print ("----AVERAGE SPEED CALCULATOR----")

def calculate(d, t): # calculates average speed
    speed = d / t
    return speed

def checkSpeedLimit(speed): # calculates if the speed limit has been broken
    limit = 30  # speed limit in m/s
    
    if limit < speed:
        print("DANGER BREAKING THE SPEED LIMIT!!!! WEEWOOWEEWOOWEEWOO CALL THE GUARDS")
    else:
        print("Safe travels!")

def travelTime(d,s): # calculates the travel time with the same speed but different distance
    time = round(d/s,1)
    print("It would take", time, "seconds to travel", distance, "metres.")

def kilometres(s): # converts m/s to km/h
    km = s*3.6
    print(s, "m/s is", round(km, 1), "km/h")

distance = float(input("Enter the distance travelled in metres: "))


time = float(input("Enter the time it took to complete the journey in seconds: "))
while time == 0:
    time = float(input("Enter a number other than 0, you can't divide by it!: ")) # Makes sure that nothing is divided by 0

avgSpeed = calculate(distance, time)
print("The average speed is:", round(avgSpeed, 2), "m/s")
print("-----------------------------------")  # Prints a divider line


#Challenge 1: Speed Limit Checker

checkSpeedLimit(avgSpeed)
print("-----------------------------------")

#Challenge 2: Travel Time Estimator

distance = float(input("Enter the new distance: "))
travelTime(distance, avgSpeed)
print("-----------------------------------")

#Challenge 3: Convert to km/h

kilometres(avgSpeed)
print("-----------------------------------")

#Challenge 4: What could crash the programme?
# Changed 'int' to 'float'
