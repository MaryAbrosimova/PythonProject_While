'''
Факториал числа. Напишите программу, которая вычисляет факториал числа n (n вводится с клавиатуры).
'''

n = int(input('Введите число: '))
factorial = 1
for i in range(1, n + 1):
    factorial *= i
print(f"Факториал числа {n} равен {factorial}")
