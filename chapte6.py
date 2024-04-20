# task 1
# a, b = float(input()), float(input())
# print(0.5 * a * b)

# task 2
# s, v1, v2 = float(input()), float(input()), float(input())
# print(s/(v1+v2))

# task 3
# n = float(input())
# print(1/n if n != 0 else 'Обратного числа не существует')

# task 4
# f = float(input())
# print((5/9)*(f-32))

# task 5
# n=float(input())
# print(n*10.5 if 0<=n<=2 else 4*(n-2)+21)

# task 6
# a = float(input())
# print(int(((a-int(a))*10)))

# task 7
# a, b, c, d, e = int(input()),int(input()),int(input()),int(input()),int(input())
# print('Наименьшее число = ', min(a, b, c, d, e),'\nНаибольшее число = ', max(a, b, c, d, e), sep ='')

# task 8
# a,b,c=int(input()),int(input()),int(input())
# sum = a+b+c
# print( max(a,b,c),'\n', (sum-max(a,b,c)-min(a,b,c)),'\n', min(a,b,c), sep='')

# task 9
# a = int(input())
# frst = a//100
# sec = a//10%10
# lst = a%10
# # print('Число интересное' if (max(frst, sec, lst)-min(frst, sec, lst))== (frst+sec+lst-max(frst, sec, lst)-min(frst, sec, lst)) else 'Число неинтересное')
# print('Число интересное' if (2*max(frst, sec, lst))== (frst+sec+lst) else 'Число неинтересное')

# task 10
# a, b, c, d, e = float(input()),float(input()),float(input()),float(input()),float(input())
# print(abs(a)+abs(b)+abs(c)+abs(d)+abs(e))

# task 11
# a, b, c, d= int(input()),int(input()),int(input()),int(input())
# print(abs(a-c)+abs(b-d))

# task 12
# a= '"Python is a great language!", said Fred. '
# b= '"I don\'t ever remember having this much fun before."'
# print(a+b)

# task 13
# print(f'Hello {input()} {input()}! You have just delved into Python')

# task 14
# a=input()
# print(f'Футбольная команда {a} имеет длину {len(a)} символов')

# task 15
# a, b, c = input(),input(), input()
# lenmax= max(len(a), len(b), len(c))
# lenmin = min(len(a), len(b), len(c))
# if lenmax==len(a):
#     max=a
#     if lenmin == len(b):
#         min = b
#     else: min = c
# elif lenmax == len(b):
#     max=b
#     if lenmin == len(a):
#         min = a
#     else: min = c
# elif lenmax == len(c):
#     max=c
#     if lenmin == len(a):
#         min = a
#     else: min = b
# print(min, max, sep='\n')

# task 16
# a, b, c = input(),input(), input()
# lenmax= max(len(a), len(b), len(c))
# lenmin = min(len(a), len(b), len(c))
# lenav= len(a+b+c)-lenmax-lenmin
# if lenav == (lenmin+lenmax)/2:
#     print('YES')
# else: print('NO')

# task 17
# print('YES' if 'синий' in input() else 'NO')

# task 18
# a = input()
# if ('суббота' in a) or ('воскресенье' in a):
#     print('YES')
# else: print('NO')

# task 19
a = input()
if ('@' in a) and ('.' in a):
    print('YES')
else: print('NO')
