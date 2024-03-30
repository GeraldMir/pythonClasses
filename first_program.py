# # Задача 7 раздела 4.3
a,b = input(), input() # принимаем на ввод название цвета
if (a == 'красный' or a == 'синий') and (b == 'синий' or b == 'красный')  : # сравниваем с базовыми цветами
    print(a if a == b else 'фиолетовый') # если смешались два базовых цвета выдаём вторичный, если два одинаковых цвета - то выводим его
elif (a == 'красный' or a == 'желтый') and (b == 'желтый' or b == 'красный') : # см. стр. 3
    print(a if a == b else 'оранжевый') # см. стр. 4
elif (a == 'синий' or a == 'желтый') and (b == 'желтый' or b == 'синий') : # см. стр. 3
    print(a if a == b else 'зеленый') # см. стр. 4
else:
    print('ошибка цвета')

# # Задача 8 раздела 4.3

number = int(input()) # принимаем номер кармана рулетки
if  1<=number<=10 or 19<=number<=28:
    print('красный' if number%2 !=0 else 'черный')
elif 11<=number<=18 or 29<=number<=36:
    print('черный' if number%2 !=0 else 'красный')
elif number==0:
    print('зеленый')
else:
    print('ошибка ввода')

# Задача 9 раздела 4.3

a1,b1,a2,b2=int(input()),int(input()),int(input()),int(input())
if b1==a2 or a1==b2:
    print(b1 if b1==a2 else a1)
elif b1 < a2 or b2 < a1:
    print('пустое множество')
elif a1<=a2:
    if b1<=b2:
        print(a2,b1)
    else: print(a2, b2)
elif a1>a2:
    if b1>b2:
        print(a1, b2)
    else: print(a1, b1)