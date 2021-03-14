import random


def insert_sort(a: list):
    for i in range(1, len(a)):
        j = i
        while j > 0 and a[j] < a[j - 1]:
            a[j], a[j - 1] = a[j - 1], a[j]
            j -= 1


def insert_sort_v2(a: list):
    for i in range(1, len(a)):
        for j in range(i, 0, -1):
            if a[j] < a[j - 1]:
                a[j], a[j - 1] = a[j - 1], a[j]
            else:
                break


a = [random.randint(-100, 100) for _ in range(10)]
insert_sort_v2(a)
print(a)
