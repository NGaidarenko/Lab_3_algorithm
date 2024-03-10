import itertools


def permutations_n_factorial(arr):
    permutations = itertools.permutations(arr)
    for perm in permutations:
        print(perm)


# Пример использования
arr = [1, 2, 3]
permutations_n_factorial(arr)
