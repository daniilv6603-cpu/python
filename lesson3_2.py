numbers = [5, 13, 5, 6]
#          0  1   2  3  4
#          -5 -4  -3  -2  -1
print(numbers[0])
numbers[0] = 10
print(numbers)
print(numbers[-1])

print(len(numbers))
print(sum(numbers))
print(min(numbers))
print(max(numbers))
print(sorted(numbers))
print(sorted(numbers, reverse=True))

'''
функции для работы со списками len sum min max sorted
'''

#методы
q = []
q.append(1)
print(q)
q.append(2)
print(q)
q.extend([4,5,5,6,5])
print(q)
q.insert(0, 10)
print(q)
q.insert(4, 11)
print(q)


#tuple (кортеж)
a = [1,2,3,4] #list (список)
b = (1,2,3,4) #tuple (кортеж)
a[0] = 1
#b[0] = 1
print(len(b))
print(sum(a))
print(min(a))
print(max(a))
print(sorted(a))


'''
list [] список
tuple () кортеж
dict {} словарь
set() множества
'''

users_list = ['user1', '12345']
users = {'login': 'user1', 'password': '12345'}
print(users['password'])

print(users)
print(len(users))
print(sorted(users))


users_new = [
    {'login': 'user1', 'password': '12345'},
    {'login': 'user2', 'password': 'sgsdg'}
]
print(users_new[0]['password'])
users_new[0]['password'] = '<PASSWORD>'
print(users_new)



matrix = [
   # 0  1  2
    [1, 2, 3], #0
    [4, 5, 6], #1
    [7, 8, 9] #2
]

print(matrix[1][2])
print(matrix[0][0] + matrix[1][1] + matrix[2][2])
m = [
    [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ],
]

print(m[0][2][2])



