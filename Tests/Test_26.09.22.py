#T1
cinemaName = "Tralee Movie House \n"

print(cinemaName)

#T2
fullName = input("Please enter your full name: ")
fullName = fullName.upper()
age = int(input("Enter your age: "))
numTickets = int(input("How many tickets would you like to buy? "))
priceTicket = float(input("How much is one ticket? "))
print("\n")

#T3
fee = 2
priceTotal = priceTicket*numTickets
priceFinal = priceTotal+fee
pricePerP = priceFinal/numTickets

#T4
modulo = numTickets%2

#T5
nameLen = len(fullName)

#T6
name3 = fullName[:3]

#7
ageStr = str(age)
bookingRef = name3+ageStr

#8
if (age < 13):
    ticket = "Child Ticket"
elif (age <= 17):
    ticket = "Teen Ticket"
else:
    ticket = "Adult Ticket"

print("--BOOKING SUMMARY--")
print("----------------")
print("Customer:", fullName)
print("Age: ", age)
print("----------------")
print("Number of tickets:€", numTickets)
print("Price per ticket:€", priceTicket, "\n")
print("Total ticket cost:€", priceTotal)
print("Booking Fee:€", fee)
print("Final cost:€", priceFinal)
print("Cost per person:€", pricePerP,)
print("----------------")
print("Name length:", nameLen)
print("First three characters:", name3)
print("----------------")
print("Booking reference:", bookingRef)
print("Ticket type:", ticket)

#Cont. T4
if modulo == 0:
    print("Tickets can be split evenly into pairs. \n")
else:
    print("There will be one ticket left over.")
