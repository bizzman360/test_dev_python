def add(num1, num2):
    return num1+num2
def subtract(num1, num2):
    return num1-num2
def multiply(num1, num2):
    return num1*num2
def divide(num1, num2):
    try:
        return num1/num2
    except ZeroDivisionError:
        print('You cannot divide by 0. Please enter a correct number')
        num2 = float(input('Enter the second number again: '))
        return divide(num1, num2)
        # return main()

def main():
    operators = ['/','*','-','+']
    num1 = float(input('Enter a number: '))
    action = ''
    while action not in operators:
        action = input('Enter operator (*/-+)')
    num2 = float(input('Enter a number: '))
    
    if action == '/':
        print(divide(num1,num2))
    if action == '*':
        print(multiply(num1,num2))
    if action == '-':
        print(subtract(num1,num2))
    if action == '+':
        print(add(num1,num2))

main()