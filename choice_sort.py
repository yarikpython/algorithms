import random


def choice_sort(a: list):
    for i in range(len(a) - 1):
        for j in range(i + 1, len(a)):
            if a[j] < a[i]:
                a[j], a[i] = a[i], a[j]


a = [random.randint(-100, 100) for _ in range(10)]
choice_sort(a)
print(a)
