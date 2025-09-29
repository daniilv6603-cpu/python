# Задача 1: проверить, совершеннолетний ли пользователь
age = int(input('Введите ваш возраст: '))
if age >= 18:
    print('Да')
else:
    print('Нет')

# Задача 2: определить, четное или нечетное число  2 4 6 8 10 12 14
number = int(input('Number: '))
if number % 2 == 0:
    print('четное')
else:
    print('нечетное')

'''
2%2=2-2=0
15 % 4 = 15 - 12 = 3
2 % 2 = 0
4 % 2 = 0
6 % 2 = 0

1 % 2 = 1
3 % 2 = 1
5 % 2 = 1
'''

# Задача 3: найти наибольшее из двух чисел
a = int(input('a='))
b = int(input('b='))
if a > b:
    print(a)
else:
    print(b)

# Задача 4: преобразовать баллы в оценку
'''
0-59 - 2
60-74 - 3
75-84 - 4
85-100 - 5
'''
a = int(input('a='))
if a >= 0 and a <= 59:
    print(2)
elif a >= 60 and a <= 74:
    print(3)
elif a >= 75 and a <= 84:
    print(4)
elif a >= 85 and a <= 100:
    print(5)
else:
    print('Error')

# Задача 5: по номеру месяца определить время года
a = int(input('a='))
if a == 1 or a == 2 or a == 12:
    print('зима')
elif a == 3 or a == 4 or a == 5:
    print('весна')
elif a == 6 or a == 7 or a == 8:
    print('лето')
elif a == 9 or a == 10 or a == 11:
    print('осень')
else:
    print('Error')

# Задача 6: определить, существует ли треугольник

a = int(input('a='))
b = int(input('b='))
c = int(input('c='))
if a + b > c and b + c > a and c + a > b:
    print('Ok')
    if a == b == c:
        print('Равностронний')
    elif a == b or a == c or c == b:
        print('Равнобедренный')
    else:
        print('Разносторонний')

