#CTI-110
#P3HW2 - Software Sales
#Zachary Hamilton
#June 24, 2018
#This program determines the discount and total cost of the packages purchased.

#Quantity 10-19 = 10% discount
#Quantity 20-49 = 20% discount
#Quantity 50-99 = 30% discount
#Quantity 100+ = 40% discount

def main():
    Quantity = int(input("Enter the number of packages bought: "))
    
    if Quantity < 10:
        print('The amount of the discount is 0% and the total amount of the purchase'
              'after the discount is $', 99 * Quantity, sep='')
    elif Quantity < 20:
        print('The amount of the discount is 10% and the total amount of the purchase'
              'after the discount is $', 99 * Quantity * 0.9, sep='')
    elif Quantity < 50:
        print('The amount of the discount is 20% and the total amount of the purchase'
              'after the discount is $', 99 * Quantity * 0.8, sep='')
    elif Quantity < 100:
        print('The amount of the discount is 30% and the total amount of the purchase'
              'after the discount is $', 99 * Quantity * 0.7, sep='')
    else:
        print('The amount of the discount is 40% and the total amount of the purchase'
              'after the discount is $', 99 * Quantity * 0.6, sep='')
main()
