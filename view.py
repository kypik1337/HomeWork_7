

def input_number():
    number = int(input('введите число:  '))
    return number

def input_operation():
    operation = input('введите операцию(+, -, *, /, = :  ')
    return operation

def print_result(smth):
    print(smth)

def input_string():
    calc_string = input('Введите строку:  ')
    calc_string = calc_string.replace(' ', '')
    if '=' in calc_string:
        calc_string = calc_string[:calc_string.find('=')]
    calc_string = calc_string.replace('*', ' * ').replace('/', ' / ').replace('+', ' + ').replace('-', ' - ')
    return calc_string

def input_calc_type():
    answer = input('Выберите тип калькулятора: \n О - для последовательного введения частей выражения, \n 1  - для введения выражения строкой  \n')
    while answer not in ['0', '1']:
        answer = input('Неккоректный ввод. Повторите: \n О - для последовательного введения частей выражения, \n 1  - для введения выражения строкой \n')
    return int(answer)
