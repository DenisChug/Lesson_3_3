def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print('Функция с параметрами по умолчанию:')
print_params()
print_params(b = 25)
print_params(c = [1,2,3])
print()

print('Распаковка параметров:')
values_list = (4, [5, 6], True)
print_params(*values_list)
values_dict = {'a': 22, 'b': 33, 'c': 44}
print_params(**values_dict)
print()

print('Распаковка + отдельные параметры:')
values_list_2 = [54.32, 'Строка' ]
print_params(*values_list_2, 42)