'''
1 2 3 4 ... 100
100 99 98 97 ... 1
шаг = -1
нач. условие = 100
кон. условие =  1
'''
a = 100
while a > 0:
    print(a)
    a -= 10
'''
and or not
'''
a = 1
while a <= 100:
    if a % 2 == 0 and a % 5 == 0:
        print(a)
    a += 1

'''
for
функции
'''
i = 1
while i <= 100:
    print(i)
    i += 1

for i in 'hello world':
    print(i)


#range(1, 101) 1 2 3 ... 10
#range(1, 101, 5) 1 6 11 ...

for a in range(10):
    print(a)

for i in range(10, 101, 2):
    print(i)

#range(100, -1, -1)
for i in range(10, 0, -1):
    print(i)


'''
таблицы умножения
1 * 1 = 1   2 * 1 = 2
1 * 2 = 2   2 * 2 = 4
1 * 3 = 3

1 * 10 = 10
'''

for i in range(1, 11): #i=1 2 3 4 5 6 7 8 9 10
    for j in range(1, 11): #i=1 j=1 2 3 4 5 6 7 8 9 10  i=2 j=1 2 3 4 5 6 7 8 9 10 i=3 j=1 2 3 4 5 6 7 8 9 10
        print(j, ' * ', i, ' = ', i * j, end='\t')
    print()

i = 1
print()
while i <= 10:
    j = 1
    while j <= 10:
        print(j, ' * ', i, ' = ', i * j, end='\t')
        j += 1
    print()
    i += 1

