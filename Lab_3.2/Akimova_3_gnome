import random
import time

def gnomeSort(arr):
    i = 1
    while i < len(arr):
        if i > 0 and arr[i - 1] > arr[i]:
            arr[i - 1], arr[i] = arr[i], arr[i - 1]
            i -= 1
        else:
            i += 1

if __name__ == "__main__":
    N = 5000
    RANGE = 100

    print("Generating array...")
    arr = [random.randint(1, RANGE) for _ in range(N)]

    print("Original array (first 20 elements):")
    print(" ".join(map(str, arr[:20])))

    start_time = time.perf_counter()
    gnomeSort(arr)

    end_time = time.perf_counter()
    duration_ms = int((end_time - start_time) * 1000)

    print("Sorted array (first 20 elements):")
    print(" ".join(map(str, arr[:20])))

    print(f"Time taken by gnomeSort: {duration_ms} milliseconds")
