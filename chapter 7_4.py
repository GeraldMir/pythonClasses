# count=-1
# txt = ''
# while txt != 'стоп' and txt != 'хватит' and txt != 'достаточно':
#     txt = input()
#     count += 1
# print(count)

# n = int(input())
# k =''
# while n%7==0:  
#     k = k + str(n) + '\n'
#     n = int(input())
# print(k, end='')    

# n = int(input())
# while n % 7 == 0:
#     print(n)
#     n = int(input())

# txt=''
# while txt != 'КОНЕЦ' and txt != 'конец':
#     print(txt)
#     txt = input()

# summa = 0
# n = int(input())
# while n > 0 and n < 6:
#     if n == 5:
#         summa += 1
#     n = int(input())
# print(summa)

price = int(input())
coins = 0
while price >= 25:
    coins += 1
    price -= 25
while price >= 10:
    coins += 1
    price -= 10
while price >= 5:
    coins += 1
    price -= 5
print(coins+price)