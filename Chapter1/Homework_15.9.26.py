#Question 4

print("Congratulations! You have the won a free Luas trip. Please choose either A,B, or C to see your destination:")
letter = input("Please enter for to destination you'd like to go to: ")
letter = letter.upper()

if letter == "A":
    print("WOW! You have won a free trip to Dundrum Shopping Centre!")
elif letter == "B":
    print("Amazing! You have won a free trip to Tallaght!")
elif letter == "C":
    print("Cool! You have won a free trip to Boombridge!")
else:
    print("Invalid entry, please select either A,B, or C")
    

#Question 5
    
percentage = int(input("Welcome, please enter your computer science grade as whole number: "))

if 90 <= percentage <= 100:
    grade = "H1"
elif 80 <= percentage < 90:
    grade = "H2"
elif 70 <= percentage < 80:
    grade = "H3"
elif 60 <= percentage < 70:
    grade = "H4"
elif 50 <= percentage < 60:
    grade = "H5"
elif 40 <= percentage < 50:
    grade = "H6"
elif 30 <= percentage < 40:
    grade = "H7"
elif 0 <= percentage < 30:
    grade = "H8"
else:
    grade = "Invalid entry"
    
print("Your grade is:", grade)
