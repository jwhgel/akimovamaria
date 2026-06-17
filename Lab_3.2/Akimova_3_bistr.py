import random
import time

def partition(arr, low, high):
    pivot = arr[high]

    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quickSort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        quickSort(arr, low, pivot_index - 1)
        quickSort(arr, pivot_index + 1, high)

if __name__ == "__main__":
    N = 20
    RANGE = 100

    print("Generating array...")
    arr = [random.randint(1, RANGE) for _ in range(N)]

    print("Original array (first 20 elements):")
    print(" ".join(map(str, arr[:20])))

    start_time = time.perf_counter()

    quickSort(arr, 0, len(arr) - 1)

    end_time = time.perf_counter()
    duration_ms = int((end_time - start_time) * 1000)

    print("Sorted array (first 20 elements):")
    print(" ".join(map(str, arr[:20])))

    print(f"Time taken by quickSort: {duration_ms} milliseconds")