# n= int(input())
# invN = ''
# while n !=0:
#     invN += str(n%10)
#     n //=10
# print(invN)

# n= int(input())
# nummin=n
# maxnum=0
# while n >0:
#     if n%10 > maxnum:
#         maxnum = n%10
#     if n%10 < nummin:
#         nummin = n%10
#     n //=10
# print(f'Максимальная цифра равна {maxnum}\nМинимальная цифра равна {nummin}')

# n= int(input())
# countNum = 0
# summdig = 0
# totaldig = 1
# frstdg = 0
# lstdig = n%10
# while n != 0:
#     countNum +=1
#     summdig += n%10
#     totaldig *= n%10
#     n //=10
#     if n != 0:
#         frstdg = n%10
# print(summdig, countNum, totaldig, (summdig/countNum), frstdg, frstdg+lstdig, sep='\n')

# Дано натуральное число n (n>9) Напишите программу, которая определяет его вторую (с начала) цифру.
# n= int(input())
# secnum =0
# while n !=0:
#     if 10 < n < 100:
#         secnum= n%10
#     n //= 10
# print(secnum)

# Дано натуральное число. Напишите программу, которая определяет, состоит ли указанное число из одинаковых цифр.
# n= int(input())
# flag = True
# num = n%10
# while n != 0 and flag == True:
#     if n%10 == num:
#         n //=10
#     else:
#         flag = False
#         print('NO')
# if flag == True: print('YES')

# Дано натуральное число. Напишите программу, которая определяет, является ли последовательность его цифр при просмотре справа налево упорядоченной по неубыванию.
# n= int(input())
# flag = 'YES'
# num = n%10
# while n != 0:
#     if n%10 >= num:
#         num = n%10
#         n //= 10
#     else:
#         flag = 'NO'
#         break
# print(flag)

# На вход программе подается число n>1. Напишите программу, которая выводит его наименьший отличный от 1 делитель.
# n= int(input())
# for i in range(2,n+1):
#     if n%i ==0:
#         print(i)
#         break

n= int(input())
for i in range(1,n+1):
    if 5 <= i <=9 or 17 <= i <= 37 or 78 <= i <=87:
        continue
    print(i)