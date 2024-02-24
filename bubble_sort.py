from random import randint

"""
Сортировка пузырьком (bubble sort) - один из самых простых для понимания методов 
сортировки массивов.
Описание алгоритма сортировки пузырьком

Алгоритм заключается в циклических проходах по массиву, за каждый проход 
элементы массива попарно сравниваются и, если их порядок не правильный, то 
осуществляется обмен. Обход массива повторяется до тех пор, пока массив не 
будет упорядочен.
"""


def bubble_sort(array):
    length = len(array)
    for i in range(0, length):
        for j in range(0, length - i - 1):
            if array[j] > array[j + 1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp


def get_arr(len_arr):
    arr = []
    for _ in range(0, len_arr):
        arr.append(randint(1, 1000))
    return arr


if __name__ == "__main__":
    arr = get_arr(100)
    print("Сортировка пузырьком")
    bubble_sort(arr)
    print("Отсортированный массив: ")
    print(arr)
