def complexity_n_cubed(matrix):
    n = len(matrix)

    # Итерация по всем элементам матрицы
    for i in range(n):
        for j in range(n):
            for k in range(n):
                print(matrix[i][j][k])


# Пример использования
matrix = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
          [[10, 11, 12], [13, 14, 15], [16, 17, 18]],
          [[19, 20, 21], [22, 23, 24], [25, 26, 27]]]

complexity_n_cubed(matrix)
