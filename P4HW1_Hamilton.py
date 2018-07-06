#CTI-110
#P4HW1 - Distance Traveled
#Zachary Hamilton
#July 6, 2018
#Distance Traveled Program.

speed = float(input("What is the speed of the vehicle in mph?:"))
timeTraveled = int(input("How many hours has it traveled?:"))

print()

print("Hour","\tDistance Traveled")
for currentHour in range(1,timeTraveled + 1):
    distanceTraveled = speed * currentHour
    print(currentHour,"\t",distanceTraveled)
