# task 3
# import math
# n = int(input())
# asimpt=0
# for i in range(1,n+1):
#     asimpt +=1/i
# print(asimpt-math.log(n))

# task 4
# n = int(input())
# summ=0
# for i in range(1,n+1):
#     if (i**2)%10 ==2 or (i**2)%10 == 5 or (i**2)%10 == 8:
#         summ +=i
# print(summ)

# task 5
# import math
# print(math.factorial(int(input())))

# task 6
# total = 1
# for i in range(10):
#     n = int(input())
#     if n != 0:
#         total *= n
# print(total)

# task 7
# n, summ = int(input()), 0
# for i in range(1,n+1):
#     if n%i==0:
#         summ += i
# print(summ) 

# task 8
# n, summ = int(input()), 0
# for i in range(n+1):
#     summ += ((-1)**(i+1))*i
# print(summ)

# task 9
# n, big1, big2 = int(input()), 0, 0
# for i in range(1,n+1):
#     num = int(input())
#     if num > big1:
#             big2 = big1
#             big1 = num
#     if num > big2 and num < big1:
#         big2 = num
# print(big1,big2,sep='\n')

# task 10
# flag = True
# for i in range(10):
#     n = int(input())
#     if n%2 != 0:
#         flag = False
# print('YES' if flag else 'NO')

# task 11
# n, n0, n1, n2 = int(input()),0,1,0
# fib = str(n1)+' '
# for i in range(n-1):
#     n2=n0+n1
#     n0, n1 = n1, n2
#     fib+= str(n2)+ ' '
# print(fib)
