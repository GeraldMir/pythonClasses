# Задача 1
# a = int(input())
# if a%100 == 0:
#     print('YES')
# else: print('NO')

# Задача 2
# a1,a2,b1,b2= int(input()),int(input()),int(input()),int(input())
# if a1%2 !=0:
#     if a2%2 !=0:
#         color1=1 # белая клетка
#     else: color1=2 # черная клетка
# elif a2%2 !=0:
#     color1=2
# else: color1=1
# if b1%2 !=0:
#     if b2%2 !=0:
#         color2=1 # белая клетка
#     else: color2=2 # черная клетка
# elif b2%2 !=0:
#     color2=2
# else: color2=1
# if color1 == color2:
#     print('YES')
# else: print('NO')

# Задача 3
# old, sex = int(input()), input()
# if 10<=old<=15 and sex == 'f':
#     print('YES')
# else: print('NO')

# Задача 4
# a=int(input())
# if 1<=a<=10:
#     if a ==1:
#         print('I')
#     elif a==2:
#         print('II')
#     elif a==3:
#         print('III')
#     elif a==4:
#         print('IV')
#     elif a==5:
#         print('V')
#     elif a==6:
#         print('VI')
#     elif a==7:
#         print('VII')
#     elif a==8:
#         print('VIII')
#     elif a==9:
#         print('IX')
#     elif a==10:
#         print('X')
# else: print('ошибка')

# Задача 5
# a = int(input())
# if a%2 !=0:
#     print("YES")
# elif 2<=a<=5:
#     print('NO')
# elif 6<=a<=20:
#     print('YES')
# elif a>20:
#     print('NO')

# Задача 7
# a1,a2,b1,b2 = int(input()),int(input()),int(input()),int(input())
# if abs(a1-b1)==abs(a2-b2):
#     print('YES')
# else: print('NO')

# Задача 7
a1,a2,b1,b2 = int(input()),int(input()),int(input()),int(input())
if (abs(a1-b1) == 2 and abs(a2-b2)==1) or (abs(a1-b1)==1 and abs(a2-b2)==2):
    print('YES')
else: print('NO')