#Basic while loops
counter = 0
while counter <7:
    print(counter)
    counter +=1
print("I'm glad that loop is finished!")

#Infinite loops
#while True:
    #print("Let's just loop for ever.")
 
#Other uses of while loops
mark = float(input("Enter exam mark between 0 and 100: "))

while mark <0 or mark > 100:
    print("Error, mark outside range.")
    mark = float(input("Re-enter mark: "))
print("You entered", mark, "- well done")


num = int(input("Enter a number, 0 to finish: "))
total = num
while num != 0:
    num = int(input("Enter another number, 0 to finish: "))
    total+=num
print("The total is: ",total)

#While loops for menus

print("1 Calculate the area of the circle")
print("2 Calculate volume of a sphere")
print("3 Exit")

option = int(input("Enter option (1-3): "))

while(option !=3):
    if option == 1:
        r = float(input("Enter radius: "))
        area = 3.14*(r**2)
        print("Area is: ", area)
        option = 0
    elif(option == 2):
        r = float(input("Enter radius: "))
        vol = (4/3)*(3.14*(r**3))
        print("Volume is: ", vol)
        option = 0
    else:
        print("Invalid choice")
    print("1 Calculate the area of the circle")
    print("2 Calculate volume of a sphere")
    print("3 Exit")
    option = int(input("Enter option (1-3): "))

print("Time for a rest.")
