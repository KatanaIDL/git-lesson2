''' Programm calculator
'''
def calc_info():
    print('Калькулятор работает  только "+" ,"-" ,"*" ,"/" !!!!')

def input_operation():
   operations = ('+','-','*','/')
   while True:
         operation = (input('Enter the operation: '))

         if operation not in operations:
            print('Калькулятор не работает с этим операцией ')
            continue
         
         break
   
   return operation



def input_number(step):
    while True:
        number = (input(f'Выведите {step} число: '))

        if not number.isdigit():
            print('Введите число, повторите!!!')
            continue

        break

    return float(number)

def solve(number1 , number2 , operation):
    result = None

    if operation == '+':
        result = number1 + number2
    elif operation == '-':
        result = number1 - number2
    elif operation == '*':
        result = number1 * number2
    else:
        result = number1 / number2

    return result

def print_solve(number1 , number2 , operation , result):
    print(f'{number1} {operation} {number2} = {result}')


def main():
    calc_info()
    number1 = input_number('первое')
    number2 = input_number('второе')
    operation = input_operation()
    result = solve(number1, number2, operation)
    print_solve(number1,number2,operation,result)
    
    
if __name__ == '__main__':
    main()