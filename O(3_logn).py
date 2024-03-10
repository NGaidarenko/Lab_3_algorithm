a = list(map(int, input('Введите числа в массив: ').split(' ')))
arr_x = list(map(int, input('Введите 3 числа, которые необходимо найти: ').split(' ')))


def search(x):
    res = len(a) // 2
    low = 0
    high = len(a) - 1

    while a[res] != x and low <= high:
        if x > a[res]:
            low = res + 1
        else:
            high = res - 1
        res = (low + high) // 2

    if low > high:
        print("Число не находится в массиве.")
    else:
        print("Найденное число " + str(a[res]) + ", стоит на " + str(res + 1) + " месте в массиве.")


for x in arr_x:
    search(x)
