'''
Другой тип циклов представляет конструкция for.
Этот цикл пробегается по набору значений, помещает каждое значение в переменную,
и затем в цикле мы можем с этой переменной производить различные действия. Формальное определение цикла for:

for переменная in набор_значений:
    инструкции

После ключевого слова for идет название переменной, в которую будут помещаться значения. Затем после оператора in указывается набор значений и двоеточие.
А со следующей строки располагается блок инструкций цикла, которые также должны иметь отступы от начала цикла.
При выполнении цикла Python последовательно получает все значения из набора и передает их переменную.
Когда все значения из набора будут перебраны, цикл завершает свою работу.
В качестве набора значений, например, можно рассматривать строку, которая по сути представляет набор символов.
Посмотрим на примере:

message = "Hello"

for c in message:
    print(c)

В цикле определяется переменную c, после оператора in в качестве перебираемого набора указана переменная message,
которая хранит строку "Hello". В итоге цикл for будет перебираеть последовательно все символы из строки message
и помещать их в переменную c. Блок самого цикла состоит из одной инструкции, которая выводит значение переменной с на консоль.
Консольный вывод программы:

H
e
l
l
o

Нередко в связке с циклом for применяется встроенная функция range(), которая генерирует числовую последовательность:

for n in range(10):
    print(n, end=" ")

Если функцию range передается один параметр, то он означает максимальное значение диапазона чисел.
В данном случае генерируется последовательность от 0 до 10 (не включительно). В итоге мы получим следующий консольный вывод:

0 1 2 3 4 5 6 7 8 9

Также в функцию range() можно передать минимальное значение диапазона

for n in range(4, 10):
    print(n, end=" ")

Здесь генерируется последовательность от 4 до 10 (не включая).
Консольный вывод:
4 5 6 7 8 9

Также в функцию range() можно передать третий параметр, который указывает на приращение:

for n in range(0, 10, 2):
    print(n, end=" ")

Здесь генерируется последовательность от 0 до 10 (не включая) с приращением 2.
Консольный вывод:
0 2 4 6 8

Цикл for также может иметь дополнительный блок else, который выполняется после завершения цикла:

message = "Hello"
for c in message:
    print(c)
else:
    print(f"Последний символ: {c}. Цикл завершен");
print("Работа программы завершена")  # инструкция не имеет отступа, поэтому не относится к else

В данном случае мы получим следующий консольный вывод:
H
e
l
l
o
Последний символ: o. Цикл завершен
Работа программы завершена

Блок else имеет доступ ко всем переменным, которые определены в цикле for.
'''