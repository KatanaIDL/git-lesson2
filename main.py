'''
Programm calculator
'''


number1 = float(input('Enter the firs num: '))
number2 = float(input('Enter the second num: '))

def input_info():
    print('Калькулятор работает  только ('+','-','*','/') !!!!')

def input_operation():
   operations = ('+','-','*','/')
   while True:
         operation = input('Enter the operation: ')

         if operation not in operations:
            print('Калькулятор не работает с этим операциям')
            continue
         break
   return operation

def input_number(step):
    while True:
        number = input(f'Введите {step} число: ')

        if not number.isdigit():
            print('Введите число, повторите!!!')
            continue

        break

    return number

def main():
    input_info()
    number1 = input_number('Enter the firs num: ')
    number2 = input_number('Enter the second num: ')
    operation = input('Enter the operation: ')
    print(f'{number1} {operation} {number2} = result')
    
if __name__ == '__main__':
    main()