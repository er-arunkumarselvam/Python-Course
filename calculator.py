# Basic Calculator

# user should give the first number
# user enter the operators like (+ - * / %)
# user should give the second number
# user press equal to operator
print("BASIC CALCULATOR")
repeat = 'Y'
while repeat == 'Y':
    firstNumber: float = float(input("Enter the first number : "))
    print("""Operator :
                + --> Addition
                -  --> Subtraction
                *  --> Multiplication
                /   --> Division
                %  --> Modulus
                //   --> Floor Division
                **  --> Power""")
    chooseOperator = input(" Enter your operator any one (your choice) : ")
    secondNumber = float(input("Enter the second number : "))

    if chooseOperator == '+':
        result = firstNumber + secondNumber
        print(firstNumber, "+", secondNumber, "=", result)
    elif chooseOperator == '-':
        result = firstNumber - secondNumber
        print(firstNumber, "-", secondNumber, "=", result)
    elif chooseOperator == '*':
        result = firstNumber * secondNumber
        print(firstNumber, "*", secondNumber, "=", result)
    elif chooseOperator == '/':
        result = firstNumber / secondNumber
        print(firstNumber, "/", secondNumber, "=", result)
    elif chooseOperator == '%':
        result = firstNumber % secondNumber
        print(firstNumber, "%", secondNumber, "=", result)
    elif chooseOperator == '//':
        result = firstNumber // secondNumber
        print(firstNumber, "//", secondNumber, "=", result)
    elif chooseOperator == '**':
        result = firstNumber ** secondNumber
        print(firstNumber, "**", secondNumber, "=", result)
    else:
        print("Invalid Operator, Please Enter Listed Operator.")
    y_or_n = input("Press 'Y' continue another calculation. otherwise not. ")
    repeat = y_or_n.upper()

    if repeat != 'Y':
        print("Thank You. Visit Again.")
