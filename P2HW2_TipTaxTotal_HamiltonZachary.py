# CTI-110
# P2HW2 - Tip Tax Total
# Zachary Hamilton
# June 17, 2018
#This program calculates the Tip Tax and Total of a bill at a restaurant.
foodCost = float(input("Enter the cost for the food: "))
tipAmount = 0.18 * foodCost
salesTax = 0.07 * foodCost
totalCost = foodCost + tipAmount + salesTax
print( "Cost of food: $" + format( foodCost, ",.2f"), "Tip: $"\
       + format(tipAmount, ",.2f"), "Sales Tax: $" +
       format( salesTax, ",.2f"), "Total: $" + format(totalCost, ",.2f"))
