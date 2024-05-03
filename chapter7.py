# task 3
# import math
# n = int(input())
# asimpt=0
# for i in range(1,n+1):
#     asimpt +=1/i
# print(asimpt-math.log(n))

# task 4
n = int(input())
summ=0
for i in range(1,n+1):
    if (i**2)%10 ==2 or (i**2)%10 == 5 or (i**2)%10 == 8:
        summ +=i
print(summ)