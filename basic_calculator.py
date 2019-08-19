# Title: Basic Calculator using Python
# Description: Basic calculator with addition, subtraction, multiplication and division.
# Author: Shakirulmuez
# Date: August 19, 2019

print "Welcome to Basic Calculator"
operation = 1

while operation > 0:
    print "1. Addition"
    print "2. Subtraction"
    print "3. Multiplication"
    print "4. Division"
    print "Enter 0 to exit\n"
    operation = input('Select operation:')

    if operation == 0:
        break
    elif operation == 1:
        int1 = input('Enter first integer: ')
        int2 = input('Enter second integer: ')
        print int1, "+", int2, "=", int1 + int2, "\n"
    elif operation == 2:
        int1 = input('Enter first integer: ')
        int2 = input('Enter second integer: ')
        print int1, "-", int2, "=", int1 - int2, "\n"
    elif operation == 3:
        int1 = input('Enter first integer: ')
        int2 = input('Enter second integer: ')
        print int1, "x", int2, "=", int1 * int2, "\n"
    elif operation == 4:
        int1 = input('Enter first integer: ')
        int2 = input('Enter second integer: ')
        print int1, "/", int2, "=", int1 / int2, "\n"
    else:
        print "WRONG INPUT!!\n"
