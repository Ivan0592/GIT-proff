# Задача 6: Вы пользуетесь общественным транспортом? 
# Вероятно, вы расплачивались за проезд и получали билет с номером. 
# Счастливым билетом называют такой билет с шестизначным номером, 
# где сумма первых трех цифр равна сумме последних трех. 
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 
# Вам требуется написать программу, которая проверяет счастливость билета.
# 385916 -> yes
# 123456 -> no

n = input('Введите номер билета: ')
a = int(n[0])
b = int(n[1])
c = int(n[2])
d = int(n[3])
e = int(n[4])
f = int(n[5])
if (a + b +c) == (d + e + f):
    print('Yes')
else:
    print('No')


    # n = int(input('Введите номер билета: '))
    # a = n[0] + n[1] + n[2]
    # b = n[3] + n[4] + n[5]
    # if a == b:
    #   print("Yes")
    # else:
    #   print("No")