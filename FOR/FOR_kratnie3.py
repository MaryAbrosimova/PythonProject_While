'''
Числа, кратные 3
Условие: Напишите программу, которая выводит все числа от 1 до N, кратные 3.
'''

n = int(input('Введите число N: '))
for i in range(1, n+1):
    if i%3==0:
        print(i)