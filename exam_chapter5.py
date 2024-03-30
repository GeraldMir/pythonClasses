# Задача 1
# a = int(input())
# if a%100 == 0:
#     print('YES')
# else: print('NO')

#Задача 2
a1,a2,b1,b2= int(input()),int(input()),int(input()),int(input())
if a1%2 !=0:
    if a2%2 !=0:
        color1=1 # белая клетка
    else: color1=2 # черная клетка
elif a2%2 !=0:
    color1=2
else: color1=1
if b1%2 !=0:
    if b2%2 !=0:
        color2=1 # белая клетка
    else: color2=2 # черная клетка
elif b2%2 !=0:
    color2=2
else: color2=1
if color1 == color2:
    print('YES')
else: print('NO')