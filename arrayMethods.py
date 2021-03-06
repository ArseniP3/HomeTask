# список - это упорядоченая, итерируемая, мутабельная структура данных, предназначеная для хранения различных объектов.
# При объявлении переменной списка создается ссылка на так называемый контейнер, в котором храняться ссылки на объекты.

#Список можно создать одним из двух способов:
# - Литеральный:
#   arr = []
# - Через функцию list():
#   arr = list()

#Создать копию списка можно несколькими способами:
# - arr[1,2,3,4,5]
#   arr1 = arr[:]
# - arr[1,2,3,4,5]
#   arr1 = list(arr)
# - arr[1,2,3,4,5]
#   arr1 = arr.copy()

#Методы списка и их объяснение:
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Конь ходит буквой Г', [[11],[12],[14],[15]], {'key' : 123}, ((11),(12),(14),(15))]
print(0, arr)

#1 - Метод list.append(х) добавляет элемент х в конец списка
arr.append('x')
print(1,arr)

#2 - Метод list.extend(list1) расширяет список путем добавления всех элементов из списка №2 (можно исп. срезы, чтобы добавить часть списка)
arr1 = [111,555]
arr.extend(arr1)
print(2,arr)

#3 - Метод list.insert(i,x) добавляет элемент x в позицию i
arr.insert(0,123)
print(3, arr)

#4 - Метод list.remove(x) удаляет первое вхождение значения х из списка. Если такого значения нет, выбрасывает ошибку
arr.remove(123)
arr.remove('x')
arr.remove(111)
arr.remove(555)
print(4, arr)

#5 - Метод list.pop(i) удаляет эллемент из позиции i и возвращает его. Если аргумент не задан, удаляет последний эллемент.
z = arr.pop(7)+1
print(5, z)

#6 - Метод list.clear() удаляет все элементы из списка, аналогичен выражению del list[:]
arr2 = list(arr)
arr3 = list(arr)
arr2.clear()
del arr3 [:]
print(6, arr2, arr3)

#7 - Метод list.index(x) возвращает индех элемента х
print(7, arr.index(1))

#8 - Метов list.count(x) возвращает кол-во вхождений элемента x в списке
print(8, arr.count(3))

#9 - Метот list.reverse() изменяет порядок расположения элементов списка на обратный
print(9,arr)
arr.reverse()
print(" ",arr)

#10 - Метод list.copy(list1) создает копию списка, механизм расписан выше.

#11 - Метод list.sort(key=None, revers = False) метод по дефолту сортирует список по возрастанию, если флаг revers присвоить
# значение True будет происходить реверсия, для какой-либо другого метода сортировки меняется значение key

arr4 = [1,11,44,3,5,88,6,0,65,4,33,45,666,777,666]
print(11, arr4)
arr4.sort()
print('  ', arr4)