'''i = 1
while i <= 100: #1 <= 100 -> True
    if i == 51:
        break
    print(i)
    i += 1


while True:
    a = int(input())
    if a == 0:
        break
    print(a)'''

users = []
while True:
    login = input('Login: ')
    password = input('Password: ')
    if login == "admin" and password == "admin":
        break
    users.append((login, password))
print(users)