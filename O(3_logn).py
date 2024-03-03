def search_3_parts(arr, x):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid1 = low + (high - low) // 3
        mid2 = low + 2 * (high - low) // 3

        if arr[mid1] == x:
            return mid1
        elif arr[mid2] == x:
            return mid2
        elif x < arr[mid1]:
            high = mid1 - 1
        elif x > arr[mid2]:
            low = mid2 + 1
        else:
            low = mid1 + 1
            high = mid2 - 1

    return -1


# Пример использования
arr = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
x = 12
index = search_3_parts(arr, x)

if index != -1:
    print(f"Число {x} найдено на позиции {index}.")
else:
    print("Число не найдено.")
