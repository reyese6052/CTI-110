# Take 5 test grades, give letter grade for each
# and give average test score
# April 22, 2018
# CTI-110 P5HW1 - Test Average and Grade
# Evita Reyes
#

def main():
    test1 = float(input('Enter first test score.'))
    determine_grade(test1)
    test2 = float(input('Enter second test score.'))
    determine_grade(test2)
    test3 = float(input('Enter third test score.'))
    determine_grade(test3)
    test4 = float(input('Enter fourth test score.'))
    determine_grade(test4)
    test5 = float(input('Enter fifth test score.'))
    determine_grade(test5)
    average_grade =(test1+test2+test3+test4+test5)/5
    print('Your average test score is:', average_grade)
    calc_average(average_grade)

def determine_grade(test1):
    A_score = 90
    B_score = 80
    C_score = 70
    D_score = 60
    F_score = 50

    if test1 >= A_score:
        print('Your grade is: A')
    elif test1 >= B_score:
        print('Your grade is: B')
    elif test1 >= C_score:
        print('Your grade is: C')
    elif test1 >= D_score:
        print('Your grade is: D')
    else:
        print('Your grade is: F')

def determine_grade(test2):
    A_score = 90
    B_score = 80
    C_score = 70
    D_score = 60
    F_score = 50

    if test2 >= A_score:
        print('Your grade is: A')
    elif test2 >= B_score:
        print('Your grade is: B')
    elif test2 >= C_score:
        print('Your grade is: C')
    elif test2 >= D_score:
        print('Your grade is: D')
    else:
        print('Your grade is: F')

def determine_grade(test3):
    A_score = 90
    B_score = 80
    C_score = 70
    D_score = 60
    F_score = 50

    if test3 >= A_score:
        print('Your grade is: A')
    elif test3 >= B_score:
        print('Your grade is: B')
    elif test3 >= C_score:
        print('Your grade is: C')
    elif test3 >= D_score:
        print('Your grade is: D')
    else:
        print('Your grade is: F')

def determine_grade(test4):
    A_score = 90
    B_score = 80
    C_score = 70
    D_score = 60
    F_score = 50

    if test4 >= A_score:
        print('Your grade is: A')
    elif test4 >= B_score:
        print('Your grade is: B')
    elif test4 >= C_score:
        print('Your grade is: C')
    elif test4 >= D_score:
        print('Your grade is: D')
    else:
        print('Your grade is: F')

def determine_grade(test5):
    A_score = 90
    B_score = 80
    C_score = 70
    D_score = 60
    F_score = 50

    if test5 >= A_score:
        print('Your grade is: A')
    elif test5 >= B_score:
        print('Your grade is: B')
    elif test5 >= C_score:
        print('Your grade is: C')
    elif test5 >= D_score:
        print('Your grade is: D')
    else:
        print('Your grade is: F')

def calc_average(average_grade):
    A_score = 90
    B_score = 80
    C_score = 70
    D_score = 60
    F_score = 50
    
    if average_grade >= A_score:
        print('Your grade average is: A')
    elif average_grade >= B_score:
        print('Your grade average is: B')
    elif average_grade >= C_score:
        print('Your grade average is: C')
    elif average_grade >= D_score:
        print('Your grade average is: D')
    else:
        print('Your grade average is: F')
    
main()
