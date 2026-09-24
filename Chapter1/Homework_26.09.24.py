#Iteration for loops
"""
#T1
for i in range(1, 11):
    print(i)

counter = 1
while counter <= 10:
    print(counter)
    counter += 1
    
    
#T2
number = int(input("Enter a number: "))

for i in range(1, number, 2):
    print(i)
    
    
#T3
sentence = input("Enter a sentence: ")
sentence = sentence.lower()
vowels = 0

for i in sentence:
    if (i == "a" or i == "e" or i == "i" or i == "o" or i == "u"):
        vowels += 1
print("Vowels: ", vowels)
"""

#T4
sentence = input("Enter a sentence: ")
reverse = ""
for i in sentence:
    reverse = i + reverse
print(reverse)
