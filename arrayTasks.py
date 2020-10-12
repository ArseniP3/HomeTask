# 1. Заполнить массив нулями, кроме первого и последнего элементов, которые должны быть равны единице.

def fillingTheArray ():
    arr = list()
    arr.append(1)
    for i in range(18):
        arr.append(0)
    arr.append(1)
    print('Task #1 - ',arr)
fillingTheArray()

# 2. Заполнить массив нулями и единицами, при этом данные значения чередуются, начиная с нуля.

def alternationFiling():
    arr = list()
    for i in range(24):
        arr.append(0)
        arr.append(1)
    print('Task #2 - ',arr)
alternationFiling()

# 3. Заполнить массив последовательными нечетными числами, начиная с единицы.

def doArrayOfOddNumbers():
    arr = list()
    a=1
    for i in range(44):
        if a % a == 0 and a % 1 == 0 and a % 2 !=0:
            arr.append(a)
        a=a+1
    print('Task #3 - ',arr)
doArrayOfOddNumbers()

# 4. Сформировать массив из элементов арифметической прогрессии с заданным первым элементом x и разностью d.

def doArithmeticProgresion(x,d):
    arr = list()
    arr.append(x)
    for i in range (22):
        x=x+d
        arr.append(x)
    print('Task #4 - ', arr)
doArithmeticProgresion(2,12)

# 5. Сформировать возрастающий массив из четных чисел.

def doArrayOfEvenNumbers ():
    arr = list()
    a = 1
    for i in range(61):
        if a % 2 == 0:
            arr.append(a)
        a=a+1
    print('Task #5 - ',arr)
doArrayOfEvenNumbers()

# 6. Сформировать убывающий массив из чисел, которые делятся на 3.

def decreasingArray():
    arr = list()
    a = 1000
    while a >= 3:
        if a % 3 == 0:
            arr.append(a)
        a=a-1
    print('Task #6 - ', arr)
decreasingArray()

# 7. Создать массив из n первых чисел Фибоначчи

def fibbonachiArr(n):
    arr = list()
    a=0
    b=1
    arr.append(a)
    arr.append(b)
    for i in range(n):
        a,b = b, b+a
        arr.append(b)
    print('Task #7 - ', arr)
fibbonachiArr(11)

# 8. Заполнить массив заданной длины различными простыми числами. Натуральное число,
# большее единицы, называется простым, если оно делится только на себя и на единицу.

print('- Task #8 - Не решена. Не понятно как определять простоту числа')

# 9. Создать массив, каждый элемент которого равен квадрату своего номера.

import random
def doArrayWithSquaresOfIndex():
    arr = list()
    arr1 = list()
    for i in range (4):
        x = random.randint(0,15)
        arr.append(x)
    print('Task #9 - ', arr)
    for j in arr:
        arr1.append(j**j)
    print('          ',arr1)
doArrayWithSquaresOfIndex()

# 10. Создать массив, на четных местах в котором стоят единицы, а нанечетных
# местах - числа, равные остатку от деления своего номера на 5.

def doStripedArray ():
    arr =[]
    j=0
    for i in range(20):
        arr.append(1)
        j=j+1
        arr.append(j%5)
        j=j+1
    print('Task #10 -',arr)
doStripedArray()

# 11. Создать массив, состоящий из троек подряд идущих одинаковых элементов.

def doListSeunce ():
    arr = list()
    for i in range (10):
        x = random.uniform(1,100)
        z = round(x, 2)
        for j in range (3):
            arr.append(z)
    print('Task #11 -',arr)
doListSeunce()

# 12. Создать массив, который одинаково читается как слева направо, так и справа налево.

def doPalindrome ():
    arr = list()
    str = 'abcdefghijklmnopqrstuvwxyz'
    stringArray = list(str)
    z = random.choice(stringArray)
    z1=z.upper()
    arr.append(z1)
    for i in range (5):
        x = random.choice(stringArray)
        arr.append(x)
        arr.insert(0, x)
    print('Task #12 -',arr)
doPalindrome()

# 13. Сформировать массив из случайных чисел, в которых ровно две единицы, стоящие на случайных позициях.

def doArrayOfNumbersWithOnes ():
    arr = list()
    while len(arr) <= 10:
        x = random.randint(0,10000000000)
        str1 = str(x)
        j=0
        for i in str1:
            if i == '1':
                j = j+1
        if j == 2:
            arr.append(x)
    print('Task #13 -', arr)
doArrayOfNumbersWithOnes()

# 14. Заполните массив случайным образом нулями и единицами так, чтобы количество единиц было больше количества нулей.

def doArrayWithZeroAndOnes ():
    arr = list()
    for i in range (15):
        x = random.randint(0,1)
        arr.append(x)
    if arr.count(1)<arr.count(0):
        for i in range(5):
            arr.append(1)
    print('Task #14 -', arr)
doArrayWithZeroAndOnes()

# 15. Сформировать массив из случайных целых чисел от 0 до 9 , в котором единиц от 3 до 5 и двоек больше троек.

def doArr15 ():
    arr = []
    for i in range(10):
        arr.append(random.randint(0,9))

    if arr.count(1)<3:
        arr.append(1)
    while arr.count(1)>5:
        arr.remove(1)
    while arr.count(2)<arr.count(3):
        arr.remove(3)
    print ('Task #15 -',arr)
doArr15()

# 16. Создайте массив, в котором количество отрицательных чисел равно количеству положительных и
# положительные числа расположены на случайных местах в массиве.

def doArray16 ():
    arr = list()
    for i in range (40):
        arr.append(random.randint(-100,100))
    positiveCount = 0
    negativCount = 0

    for i in arr:
        if i < 0:
            negativCount = negativCount + 1
        elif i >= 0:
            positiveCount = positiveCount + 1

    difference = abs(positiveCount-negativCount)
    count = 0
    for j in arr:
        if count < difference:
            if negativCount > positiveCount:
                if j < 0:
                    arr.remove(j)
                    count = count +1
            elif negativCount < positiveCount:
                if j >= 0:
                    arr.remove(j)
                    count = count +1
        else:
            break
    print('Task #16 -',arr)
doArray16()

# 17. Заполните массив случайным образом нулями, единицами и двойками так, чтобы первая двойка в массиве
# встречалась раньше первой единицы, количество единиц было в точности равно суммарному количеству нулей и двоек.

def doArray17():
    arr = []
    for i in range (15):
        arr.append(random.randint(0,2))
    print(arr)

doArray17()