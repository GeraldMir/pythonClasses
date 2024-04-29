# task 1
# x1,y1,x2,y2 = float(input()),float(input()),float(input()),float(input())
# print(((x1-x2)**2+(y1-y2)**2)**0.5)

#task 2
# r = float(input())
# import math
# print(math.pi*r**2, 2*math.pi*r, sep='\n', end='')

# task 3
# a,b = float(input()),float(input())
# print((a+b)/2, (a*b)**0.5, 2*a*b/(a+b), ((a**2+b**2)/2)**0.5, 
#       sep='\n')

# task 4
# x = float(input())
# import math
# r = math.radians(x)
# print(math.sin(r)+math.cos(r)+math.pow(math.tan(r),2))

# task 5
# x = float(input())
# import math
# print(math.floor(x)+math.ceil(x))

# task 6
# task 5
a,b,c = float(input()),float(input()),float(input())
import math
disk = math.pow(b,2)-4*a*c
if disk == 0:
    print(-b/(2*a))
elif disk>0:
    x1=(-1*b+math.sqrt(disk))/(2*a)
    x2=(-1*b-math.sqrt(disk))/(2*a)
    if x1<x2:
        print(x1, x2, sep='\n')
    else:
        print(x2, x1, sep='\n')
elif disk<0:
    print('Нет корней')