''' 
a simple python calculator by teniola.
femi this one's for you lmao
'''

def calculator():
    def subtraction(num1, num2):
        return num1 - num2 

    def addition(num1, num2):
        return num1 + num2

    def multiplication(num1, num2):
        return num1 * num2

    def division(num1, num2):
        return num1 / num2  
    
    print('select operation:\n'\
      '1.subtraction\n'\
        '2.addition\n'\
            '3.multiplication\n' \
                '4.division\n')
    
    select = int(input('select operation:\n'))

    num1 = int(input('enter first number:'))
    num2 = int(input('enter second number:'))

    if select == 1:
        print(num1, "-", num2, "=",
                        subtraction(num1, num2))
    
    elif select == 2:
        print(num1, "+", num2, "=",
                        addition(num1, num2))
    
    elif select == 3:
        print(num1, "*", num2, "=",
                        multiplication(num1, num2))
    
    elif select == 4:
        print(num1, "/", num2, "=",
                        division(num1, num2))
    else:
        print("Invalid input")


calculator()