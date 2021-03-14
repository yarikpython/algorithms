import random
import time


def quick_sort(a: list):
    if len(a) > 1:
        mid_value = a[random.randint(0, len(a) - 1)]
        low = [i for i in a if i < mid_value]
        eq = [i for i in a if i == mid_value]
        high = [i for i in a if i > mid_value]
        a = quick_sort(low) + eq + quick_sort(high)
    return a


unsort_a = [random.randint(-10000, 10000) for _ in range(1000000)]
print(unsort_a[:10])

start = time.time()
sort_a = quick_sort(a=unsort_a)
# sort_a = sorted(unsort_a)  # five times faster
finish = time.time()

print(sort_a[:10])
print(finish - start)
