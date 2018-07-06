#CTI-110
#P4HW2 - Running Total
#Zachary Hamilton
#July 6, 2018
#This program creates a running total ending when a negative number is entered.

total = 0
userNumber = float(input("Enter a number?:"))

while userNumber > -1:
    total = total + userNumber
    userNumber = float(input("Enter a number?:"))
print()
print("Total:",total)
