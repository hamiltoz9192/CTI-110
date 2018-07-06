#CTI-110
#P4HW3 - Factorial
#Zachary Hamilton
#July 6, 2018
#Factorial program.

userInteger = int( input("Enter a nonnegative number:"))

while userInteger < 1:
    userInteger = int(input("Enter a nonnegative number:"))

factorial = 1

for currentNumber in range(1, userInteger + 1):
    factorial = factorial * currentNumber

print()
print("The factorial of", userInteger, "is", factorial)
