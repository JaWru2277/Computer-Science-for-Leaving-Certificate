#Tasks page 25

#Question 1
artist = input("Please enter your favourite artist/band: ")
if artist == "Taylor Swift":
    compliment = " is a horrible artist."
else:
    compliment = " is brilliant!"
    
sentence = artist + compliment
print(sentence, "\n")

#Question 2
name = input("Please enter your full name: ")
spaceLoc = (name.index(" "))
fName = name[:spaceLoc]
sName = name[spaceLoc:]

print(fName)
print(sName, "\n")

#Question 3
time = input("Please enter your time as [hours: minutes: seconds]: ")
list1 = time.split(":")
hours = int(list1[0])
minutes = int(list1[1])
seconds = int(list1[2])

secondsH = hours*3600
secondsM = minutes*60
timeFinal = secondsH+secondsM+seconds

print(timeFinal, "\n")

#Question 4
seconds = int(input("Please enter any five-digit number to represent seconds: "))
minutes = seconds // 60
print(minutes, "\n")

#Question 5
listTemp = list(range(0,5))
for i in listTemp:
    character = input("Please enter your character: ")
    print(character, "is", ord(character), "as an ASCII decimal value.", "\n")



#Question 6
unit = int(input("Please enter how many units of electricity you've used this month: "))
rate = 0.19
standingCharge = 26.20
due = round((unit*rate)+standingCharge, 2)

print("Your total due payment is", due, "Euro.", "\n")



#Question 7
fish = 4.50
chips = 2.80
vat = 0.09

numberF = int(input("Number of portions of fish ordererd: "))
numberC = int(input("Number of portions of chips ordered: "))

total = (fish*numberF)+(chips*numberC)
totalVat = round((total*0.09)+total, 2)

print("Al's Chipper")

if numberF > 0:
    print(numberF, "x Fish - €", numberF*fish)
    
if numberC > 0:
    print(numberC, "x Chips - €", numberC*chips)
    
print("Total (including VAT):", totalVat)
print("Thank you for dining with us!", "\n")


#Question 8
word = input("Please enter the 5 letter word you want to encrypt: ")
key = int(input("Please enter your key: "))

number = 0
letters = []

for letter in word:
    character = word[number]
    ascii = ord(character)
    encryptedLetter = chr((ascii - ord("a") + key) % 26 + ord("a"))
    number += 1
    letters.append(encryptedLetter)

final = "".join(letters)
print(final)
