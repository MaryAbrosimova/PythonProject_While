'''
Факториал числа. Напишите программу, которая вычисляет факториал числа n (n вводится с клавиатуры).
'''

number = int(input('Введите число: '))
i = 1
factorial = 1
while i <= number:
    factorial*=i
    i += 1
print ('Факториал числа', number, 'равен', factorial)