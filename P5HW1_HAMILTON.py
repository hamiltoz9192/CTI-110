# This program gives the letter grade for a test score and the average of 5 test scores.
# July 8, 2018
# CTI-110 P5HW1 - Test Average and Grade
# ZACHARY HAMILTON
#

def main():
    score1 = int(input('Enter score 1: '))
    score2 = int(input('Enter score 2: '))
    score3 = int(input('Enter score 3: '))
    score4 = int(input('Enter score 4: '))
    score5 = int(input('Enter score 5: '))

    total = (score1 + score2 + score3 + score4 + score5)

    def calc_average(total):
        average = total / 5
        return average
    
    def determine_grade(userScore):
        if(userScore < 60):
            return 'F'
        elif(userScore < 70):
            return 'D'
        elif(userScore < 80):
            return 'C'
        elif(userScore < 90):
            return 'B'
        elif(userScore < 101):
            return 'A'

    userScore = total
    avg = calc_average(total)
    
    print('Score 1 is: ', determine_grade(score1))
    print('Score 2 is: ', determine_grade(score2))
    print('Score 3 is: ', determine_grade(score3))
    print('Score 4 is: ', determine_grade(score4))
    print('Score 5 is: ', determine_grade(score5))
    print('The letter grade average is: ' + determine_grade(avg))
    print('The grade point average is: ' + str(avg))
main()
