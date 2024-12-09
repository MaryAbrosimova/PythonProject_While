'''
Цикл while проверяет истинность некоторого условия, и если условие истинно, то выполняет инструкции цикла.
Он имеет следующее формальное определение:

while условное_выражение:
    инструкции
После ключевого слова while указывается условное выражение, и пока это выражение возвращает значение True,
будет выполняться блок инструкций, который идет далее.
Все инструкции, которые относятся к циклу while, располагаются на последующих строках и должны иметь отступ от начала ключевого слова while.
'''

number = 1

while number < 5:
    print(f"number = {number}")
    number += 1
print("Работа программы завершена")

'''
В данном случае цикл while будет выполняться, пока переменная number меньше 5. Сам блок цикла состоит из двух инструкций:
'''
print(f"number = {number}")
number += 1

'''
Обратите внимание, что они имеют отступы от начала оператора while - в данном случае от начала строки.
Благодаря этому Python может определить, что они принадлежат циклу. В самом цикле сначала выводится значение переменной number,
а потом ей присваивается новое значение.
Также обратите внимание, что последняя инструкция print("Работа программы завершена") не имеет отступов от начала строки, поэтому она не входит в цикл while.

Весь процесс цикла можно представить следующим образом:

1. Сначала проверяется значение переменной number - меньше ли оно 5.
И поскольку вначале переменная равна 1, то это условие возвращает True, и поэтому выполняются инструкции цикла
Инструкции цикла выводят на консоль строку number = 1.
И далее значение переменной number увеличивается на единицу - теперь она равна 2.
Однократное выполнение блока инструкций цикла называется итерацией. Таким образом, в цикле выполняется первая итерация.

2. Снова проверяется условие number < 5. Оно по прежнему равно True, так как number = 2, поэтому выполняются инструкции цикла
Инструкции цикла выводят на консоль строку number = 2.
И далее значение переменной number опять увеличивается на единицу - теперь она равна 3.
Таким образом, выполняется вторая итерация.

3. Опять проверяется условие number < 5. Оно по прежнему равно True, так как number = 3, поэтому выполняются инструкции цикла
Инструкции цикла выводят на консоль строку number = 3.
И далее значение переменной number опять увеличивается на единицу - теперь она равна 4. То есть выполняется третья итерация.

4. Снова проверяется условие number < 5. Оно по прежнему равно True, так как number = 4, поэтому выполняются инструкции цикла
Инструкции цикла выводят на консоль строку number = 4.
И далее значение переменной number опять увеличивается на единицу - теперь она равна 5. То есть выполняется четвертая итерация.

5. И вновь проверяется условие number < 5. Но теперь оно равно False, так как number = 5, поэтому выполняются выход из цикла.
Все цикл - завершился. Дальше уже выполняются действия, которые определены после цикла.
Таким образом, данный цикл произведет четыре прохода или четыре итерации

В итоге при выполнении кода мы получим следующий консольный вывод:

number = 1
number = 2
number = 3
number = 4
Работа программы завершена

Для цикла while также можно определить дополнительный блок else, инструкции которого выполняются, когда условие равно False:
'''
number = 1

while number < 5:
    print(f"number = {number}")
    number += 1
else:
    print(f"number = {number}. Работа цикла завершена")
print("Работа программы завершена")

'''
То есть в данном случае сначала проверяется условие и выполняются инструкции while.
Затем, когда условие становится равным False, выполняются инструкции из блока else.
Обратите внимание, что инструкции из блока else также имеют отступы от начала конструкции цикла.
В итоге в данном случае мы получим следующий консольный вывод:

number = 1
number = 2
number = 3
number = 4
number =5. Работа цикла завершена
Работа программы завершена

Блок else может быть полезен, если условие изначально равно False, и мы можем выполнить некоторые действия по этому поводу:
'''

number = 10

while number < 5:
    print(f"number = {number}")
    number += 1
else:
    print(f"number = {number}. Работа цикла завершена")
print("Работа программы завершена")

'''
В данном случае условие number < 5 изначально равно False,
поэтому цикл не выполняет ни одной итерации и сразу переходит в блоку else.
'''