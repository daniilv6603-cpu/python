# Задача 7: простейшая система авторизации
users = [
    ('user1', '12345'),
    ('user2', 'sdgsdg'),
    ('user3', 'afasf')
]
login = input('Login: ')
password = input('Password: ')
for user in users:
    if user[0] == login and user[1] == password:
        print('Ok')
        break

# Задача 8: простой калькулятор
a = int(input('A: '))
b = int(input('B: '))
c = input('C: ') #+ - / *
if c == '+':
    print(a + b)
elif c == '-':
    print(a - b)
elif c == '*':
    print(a * b)
elif c == '/':
    if b == 0:
        print('Error')
    else:
        print(a / b)

