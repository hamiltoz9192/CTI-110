#CTI-110
#P3HW1 - Age Classifier
#Zachary Hamilton
#June 24, 2018
#This program will determine the age classification of a person.

def main():
    #Enter the person's age.
    age = int(input('Enter the age of the person: '))

    #If the person is 1 year old or less, he or she is an infant.
    #If the person is older than one year, but younger than 13, he or she is a child.
    #If the person is at least 13 years old, but less than 20 years old, he or she is a teenager.
    #If the person is 20 years old, he or she is an adult.
    if age <= 1:
        print('This person is an infant.')
    elif age > 1 or age < 13:
        print('This person is a child.')
    elif age > 13 or age < 20:
        print('This person is a teenager.')
    else:
        print('This person is an adult.')
main()
