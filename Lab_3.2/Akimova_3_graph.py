import random
import time
import matplotlib.pyplot as plt


def combineBuckets(buckets):
    combinedArray = []
    for bucket in buckets:
        combinedArray.extend(bucket)
    return combinedArray

def sortByDigit(arr, digitPlace):
    buckets = [[] for _ in range(10)]
    for num in arr:
        bucketIndex = (num // digitPlace) % 10
        buckets[bucketIndex].append(num)
    arr[:] = combineBuckets(buckets)

def radixSort(arr):
    if not arr: return arr
    maxVal = max(arr)
    digitPlace = 1
    while maxVal // digitPlace > 0:
        sortByDigit(arr, digitPlace)
        digitPlace *= 10
    return arr

def gnomeSort(arr):
    i = 1
    while i < len(arr):
        if i > 0 and arr[i - 1] > arr[i]:
            arr[i - 1], arr[i] = arr[i], arr[i - 1]
            i -= 1
        else:
            i += 1
    return arr

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quickSortHelper(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        quickSortHelper(arr, low, pivot_index - 1)
        quickSortHelper(arr, pivot_index + 1, high)

def quickSort(arr):
    quickSortHelper(arr, 0, len(arr) - 1)
    return arr

sizes = [100, 500, 1000, 2000, 5000, 10000, 50000]
RANGE = 100

radix_times = []
gnome_times = []
quick_times = []

for N in sizes:
    base_arr = [random.randint(1, RANGE) for _ in range(N)]

    arr_radix = base_arr.copy()
    start = time.perf_counter()
    radixSort(arr_radix)
    radix_times.append(time.perf_counter() - start)

    arr_quick = base_arr.copy()
    start = time.perf_counter()
    quickSort(arr_quick)
    quick_times.append(time.perf_counter() - start)

    if N <= 5000:
        arr_gnome = base_arr.copy()
        start = time.perf_counter()
        gnomeSort(arr_gnome)
        gnome_times.append(time.perf_counter() - start)
    else:
        gnome_times.append(None)

plt.figure(figsize=(10, 6))

plt.plot(sizes, radix_times, label="Поразрядная сортировка", color="green", marker="o", linewidth=2)
plt.plot(sizes, quick_times, label="Быстрая сортировка", color="blue", marker="s", linewidth=2)

gnome_sizes = [sizes[i] for i in range(len(sizes)) if gnome_times[i] is not None]
gnome_valid_times = [t for t in gnome_times if t is not None]
plt.plot(gnome_sizes, gnome_valid_times, label="Гномья сортировка (до N=5000)", color="crimson", marker="^", linewidth=2)

plt.title("Время выполнения алгоритмов при разном количестве элементов", fontsize=14)
plt.xlabel("Количество элементов в массиве (N)", fontsize=12)
plt.ylabel("Время выполнения (секунды)", fontsize=12)
plt.xscale('log')
plt.xticks(sizes, labels=[str(s) for s in sizes])
plt.grid(True, which="both", linestyle="--", alpha=0.5)
plt.legend(fontsize=11)

plt.show()