def complexity_nlogn(arr):
    # Сортируем массив, используя сортировку слиянием
    sorted_arr = merge_sort(arr)

    # Печать отсортированного массива
    print(sorted_arr)


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # Разделение массива пополам
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Рекурсивное слияние и сортировка левой и правой половин массива
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # Слияние отсортированных половин
    return merge(left_half, right_half)


def merge(left, right):
    result = []
    left_idx, right_idx = 0, 0

    # Слияние двух отсортированных массивов
    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1

    # Добавление оставшихся элементов, если такие есть
    result.extend(left[left_idx:])
    result.extend(right[right_idx:])

    return result


# Пример использования
arr = [12, 11, 13, 5, 6, 7, -1]
complexity_nlogn(arr)
