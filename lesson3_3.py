numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#1*2*3*...*9=
f = 1
s = 0
for number in numbers: #number=1 number=2 ... number=9
    f = f * number #f=1*1=1  f=1*2=2  f=2*3=6 f=6*4=24 ...
    s = s + number
print(f, s)

