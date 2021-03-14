import random

a = [random.randint(-100, 100) for _ in range(10)]


def bubble_sort(a: list):
    for i in range(len(a) - 1):
        for j in range(len(a) - 1 - i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]


bubble_sort(a=a)
print(a)
